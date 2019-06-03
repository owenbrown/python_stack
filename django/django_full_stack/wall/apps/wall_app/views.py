import bcrypt
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from . import forms
from .models import Comment, Message, User


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
            return render(request, 'wall_app/login.html', context=context)
        user = users[0]

        password = login_form.cleaned_data["password"]
        if not bcrypt.checkpw(password.encode(), user.password_hash.encode()):
            messages.error(request, "The password is incorrect")
            return render(request, 'wall_app/login.html', context=context)

        messages.success(request, f"Welcome back {user.first_name}!")
        return redirect(to=reverse("index"))

    login_form = forms.Login()
    register_form = forms.Register()
    context = dict(login_form=login_form, register_form=register_form)
    return render(request, "wall_app/login.html", context=context)


def register(request):
    print("register hit")
    if request.method == "POST":
        form = forms.Register(request.POST)
        # I COULD ADD EXTRA VALIDATION
        # errors = User.objects.extra_validation(request.POST)
        # if errors:
        #     for _, v in errors.items():
        #         messages.error(request, v)
        #         return render(request, 'store/login.html', dict(register_form=form))

        if form.is_valid():
            password = form.cleaned_data["password"]
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode(), salt)
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


def message(request):
    # REMINDER - messages is a reserved word in Django
    if request.method == "GET":
        return HttpResponse("You can't render message. If you could it would require a pk.")
    if request.method == "POST":
        form = forms.Message(request.POST)
        if form.is_valid():
            m = Message(
                user_id=request.session['user_id'],
                message=form.cleaned_data["message"],
            )
            m.save()
        else:
            # TODO add message failure logic
            return HttpResponse("add message failure logic")
        return redirect("index")


def comment(request):
    # REMINDER - messages is a reserved word in Django
    if request.method == "GET":
        return HttpResponse("Error - get request called on comment")
    if request.method == "POST":
        form = forms.Message(request.POST)
        if form.is_valid():
            m = Comment(
                user_id=request.session['user_id'],
                message_id=form.cleaned_data["message_id"],
                comment=form.cleaned_data["comment"]
            )
            m.save()
        else:
            # TODO add failure logic
            return HttpResponse("Add comment failure logic")
        return redirect("index")


def index(request):
    if 'user_id' not in request.session:
        print("user not logged in, redirecting")
        return redirect(reverse('login'))
    else:
        print("user logged in, redirecting")
        user_id = request.session['user_id']
        return redirect(reverse('wall', user_id))


def wall(request, user_id):
    if 'user_id' not in request.session:
        # force users to register
        return redirect(reverse('login'))
    print("user_id was not in session")

    # Users can post to their own wall, but not to others walls
    if request.session["user_id"] == user_id:
        new_message_form = forms.Message()
    else:
        new_message_form = None

    # TODO double check that this is working
    wall_messages = Message.objects.all().order_by('-created_at')
    for m in wall_messages:
        form = forms.Comment()
        m.form = form
        # TODO Check if this works
        # I added an attribute to the Message object. I'm going to try to render this form in Django. It may or may not
        # work

    context = dict(new_message_form=new_message_form, wall_messages=wall_messages)

    return render(request, "wall_app/wall.html", context)


def logout(request):
    if 'email' in request.session:
        del request.session['email']

    messages.success(request, "Come back soon")
    return redirect(to=reverse('index'))
