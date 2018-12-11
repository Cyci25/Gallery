from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt


# Create your views here.
# def welcome(request):
#     return HttpResponse('image.html')
def welcome(request):
    return render(request, 'images.html')

# def news_of_day(request):
#     date = dt.date.today()
#     # html = f'''
#     #     <html>
#     #         <body>
#     #             <h1> {date.day}-{date.month}-{date.year}</h1>
#     #         </body>
#     #     </html>
#     #         '''
#     return render(request, 'images.html')


