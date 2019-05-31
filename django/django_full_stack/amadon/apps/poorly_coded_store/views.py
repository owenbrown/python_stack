from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import Http404

from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout(request):
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
