from django.shortcuts import HttpResponse, redirect


def index(_):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(_):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(_):
    return redirect("/")


def show(_, number):
    return HttpResponse(f"placeholder to display blog {number}")


def update(_, number):
    return HttpResponse(f"placeholder to update blog {number}")


def delete(_, number):
    return HttpResponse(f"placeholder to delete blog {number}")
