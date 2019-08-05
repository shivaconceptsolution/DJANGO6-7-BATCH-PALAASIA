from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"studentapp/index.html")
def about(request):
    return render(request,"studentapp/about.html")
def contact(request):
    return render(request,"studentapp/contact.html")        

def si(request):
  p=12000
  r=2.2
  t=2
  si=(p*r*t)/100
  return HttpResponse("Result is "+str(si))    


