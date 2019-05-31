import bcrypt
from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from . import forms
from .models import Order, Product, User


def login(request):
    print("login")
    print(request.method)
    if request.method == "POST":
        print("method was post")
        login_form = forms.Login(request.POST)
        context = dict(login_form=login_form, register_form=forms.Register())
        if login_form.is_valid():
            email = login_form.cleaned_data["email"]
        else:
            messages.error("hmm...something was wrong with your login")
            return redirect(reverse('login'))
        users = User.objects.filter(email=email)
        print("printing users")
        print(users)
        if not users:
            messages.error(request, "This user does not exist")
            return render(request, 'store/login.html', context=context)
        user = users[0]

        password = login_form.cleaned_data["password"]
        if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
            messages.error(request, "The password is incorrect")
            return render(request, 'store/login.html', context=context)

        messages.success(request, f"Welcome back {user.first_name}!")
        return redirect(to=reverse("index"))

    login_form = forms.Login()
    register_form = forms.Register()
    context = dict(login_form=login_form, register_form=register_form)
    return render(request, "store/login.html", context=context)


def register(request):
    print("register hit")
    if request.method == "POST":
        form = forms.Register(request.POST)
        errors = User.objects.extra_validation(request.POST)
        if errors:
            for _, v in errors.items():
                messages.error(request, v)
                return render(request, 'store/login.html', dict(register_form=form))

        if form.is_valid():
            password = form.cleaned_data["password"]
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
            print("salt is ", salt)
            user = User.objects.create(
                email=form.cleaned_data['email'],
                password_hash=password_hash.decode(),
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            request.session["email"] = form.cleaned_data['email']
            return redirect('index')
    else:
        return redirect(to=reverse('login'))


def index(request):
    if 'email' not in request.session:
        return redirect(reverse('login'))
    print("email was in session")
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def logout(request):
    if 'email' in request.session:
        del request.session['email']

    messages.success(request, "Come back soon")
    return redirect(to=reverse('index'))


def checkout(request):
    if 'email' not in request.session:
        return redirect(reverse('login'))

    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        try:
            price = float(Product.objects.get(id=product_id).price)
        except Product.DoesNotExist:
            return Http404("product does not exist")

        quantity_from_form = int(request.POST["quantity"])
        last_charge = quantity_from_form * price
        request.session['last_charge'] = last_charge
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=last_charge)
        if 'running_total_charges' in request.session:
            request.session['running_total_charges'] += last_charge
        else:
            request.session['running_total_charges'] = last_charge

        if 'running_total_quantity' in request.session:
            request.session['running_total_quantity'] += quantity_from_form
        else:
            request.session['running_total_quantity'] = quantity_from_form

        return redirect(to=reverse('checkout'))

    context = dict(
        total_charge=request.session['last_charge'],
        running_total_charges=request.session['running_total_charges'],
        running_total_quantity=request.session['running_total_quantity']
    )

    return render(request, "store/checkout.html", context)
