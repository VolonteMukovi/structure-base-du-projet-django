from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,"home.html")
    # return HttpResponse("Hello world")

def contact_view(request):
    return render(request,"contact.html")
    # return HttpResponse("Contactez nous ! ")