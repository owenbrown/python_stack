from django.shortcuts import HttpResponse


def index(_):
    return HttpResponse("this is the equivalent of @app.route('/')!")
