from datetime import date, datetime
from multiprocessing import context
from home.models import Contact
from django.shortcuts import render, HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
   
    # return HttpResponse("This is Home Page")
    context = {
        "variable" : "This is Set"
    }
    return render(request, "index.html", context)
    
def about(request):
    # return HttpResponse("This is About Page")
    return render (request , "about.html")

def services(request):
    return render (request , "services.html")
    # return HttpResponse("This is Service Page")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name =name , email =email , phone =phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request,'Your Message has been Sent!')
    return render (request , "contact.html")
    # return HttpResponse("This is Contact Page")