from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is our homepage")

def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("This is services page")
    return render(request, 'services.html') 
def ecommerce(request):
    #return HttpResponse("This is ecommerce page")
    return render(request, 'ecommerce.html') 
def soft(request):
    #return HttpResponse("This is software services page")
    return render(request, 'soft.html') 
def dm(request):
    #return HttpResponse("This is digitalmedia page")
    return render(request, 'dm.html') 
def media(request):
    #return HttpResponse("This is media page")
    return render(request, 'media.html') 


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()

    #return HttpResponse("This is contact page")
    return render(request, 'contact.html') 
def blog(request):
    #return HttpResponse("This is blog page")
    return render(request, 'blog.html') 