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

def add(request):
  return render(request,"studentapp/add.html")

def addlogic(request):

	a = request.POST["txtnum1"]
	b = request.POST["txtnum2"]
	if(request.POST['btnsubmit'] =="ADD"):
	 c = int(a)+int(b)
	elif(request.POST['btnsubmit'] =="SUB"):
	 c = int(a)-int(b)
	elif(request.POST['btnsubmit'] =="MULTI"):
	 c = int(a)*int(b)
	else:
	 c = int(a)/int(b)  
	return render(request,"studentapp/add.html",{'key':'result is '+str(c)})





