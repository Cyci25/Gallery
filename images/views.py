from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'image.html')

def image(request, id):
    try:
        image = Image.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    return render(request, 'images.html', {"image": image})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"picture": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


