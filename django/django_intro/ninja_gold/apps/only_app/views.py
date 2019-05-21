import datetime

from django.shortcuts import render, redirect

from .places import places


def index(request):
    print("index view")
    print("request.method: ", request.method)
    gold = request.session.get('gold', 0)
    messages = request.session.get('messages', list())
    context = dict(gold=gold, places_list=places.values(), messages=messages)
    return render(request, "only_app/index.html", context)


def process_money(request):
    print("process_money view")

    place_name = request.POST.get('building')
    delta = places[place_name].find_gold()
    request.session['gold'] = request.session.get('gold', 0) + delta

    msg = f"Your earned {delta} gold at the {place_name}. " \
        f"Total gold is {request.session['gold']} ({datetime.datetime.utcnow().strftime('%I:%M')} UTC)"
    if 'messages' in request.session:
        request.session['messages'].append(msg)
    else:
        request.session['messages'] = [msg]

    return redirect("/")
