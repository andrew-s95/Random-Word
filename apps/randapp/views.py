from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("Erik likes Spiders")

def rando(request):
    if 'counter' not in request.session:
        request.session['counter'] = -1
    request.session['randy'] = get_random_string(length=14)
    request.session['counter'] += 1
    return render(request, "randapp/index.html")

def reset(request):
    if "reset" in request.POST:
        request.session.clear()
    return redirect('/random_word')
