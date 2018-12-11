from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def image(request, id):
    try:
        image = Image.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    return render(request, 'images.html', {"image": image})


