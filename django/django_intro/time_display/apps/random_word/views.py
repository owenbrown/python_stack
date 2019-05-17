from django.shortcuts import render
from django.utils.crypto import get_random_string


# Create your views here.

def random_word(request):
    # increment session
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    counter = request.session['counter']

    word = get_random_string()
    context = dict(word=word, counter=counter)
    print('set random word to {word}')
    return render(request, "random_word/index.html", context)


def reset(request):
    request.session['counter'] = 0
    return render(request, "random_word/index.html", dict())
