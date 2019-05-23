from django.http import HttpResponse
from django.shortcuts import redirect


def register(request):
    if request.method == 'GET':
        # display form to create a new user
        print("GET users/register")
        return HttpResponse("placeholder for users to create a new user record")
    if request.method == 'POST':
        # create new user
        print("POST users/register")
        return redirect("users")


def login(request):
    if request.method == 'GET':
        # display form to login a user
        print("GET users/login")
        return HttpResponse("placeholder for users to login")
    if request.method == 'POST':
        # create new user
        print("POST users/login")
        return redirect("users")


def users(request):
    return HttpResponse("placeholder to later display all the list of users")
