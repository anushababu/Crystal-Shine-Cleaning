from django.shortcuts import render
from django.http import HttpResponseRedirect
from app10.models import *

# Create your views here.
def index(request):
	return render(request,'index.html')

def services(request):
	return render(request,'services.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')	


#############################################admin######################################################

def admin_index(request):
   return render(request,'admin/index.html') 

def admin_login(request):
   if request.method=="POST":
         cemail=request.POST["email"]
         cpassword=request.POST["password"]

         check=register_tb.objects.filter(email=cemail,password=cpassword)
         if check:
              for x in check:
                  request.session['id1']=x.id
                  request.session['email1']=x.email
              return render(request,'admin/index.html',{'success':'successfully logined'})
         else:
             return render(request,'admin/login.html',{'error':'invalid details'})
   else:
   	return render(request,'admin/login.html')

def admin_logout(request):
    if request.session.has_key("id1"):
         del request.session['id1']
         del request.session['email1']
    return HttpResponseRedirect('/admin_login/')   	 

def admin_register(request):
   if request.method=="POST":
         cemail=request.POST["email"]
         cpassword=request.POST["password"]
         cconfirmpass=request.POST["confirmpassword"]
      
         check=register_tb.objects.filter(email=cemail)
         if check:
               return render(request,'admin/register.html',{'error':'Already Registered'})
         else:
               add=register_tb(email=cemail,password=cpassword,confirmpassword=cconfirmpass)
               add.save()
               return render(request,'admin/index.html',{'success':'successfully Registered'})
   else:
       return render(request,'admin/register.html')       			