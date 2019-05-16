from time import strftime, gmtime

from django.shortcuts import render


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "first_app/index.html", context)
