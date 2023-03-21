from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from app10.models import *
import os
import random
import string
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request,'index.html')

def services(request):
  data=category_tb.objects.all()
  # category=service_tb.objects.raw('SELECT * FROM app10_service_tb GROUP BY category_id')
  return render(request,'services.html',{'details':data})

def about(request):
  data=team_tb.objects.all()
  return render(request,'about.html',{'details':data})

def contact(request):
  if request.method=="POST":
    cname=request.POST["name"]
    cemail=request.POST["email"]
    csubject=request.POST["subject"]
    cphone=request.POST["phone"]
    cmessage=request.POST["message"]
    check=contactf_tb.objects.filter(email=cemail)
    if check:
        return render(request,'contact.html',{'error':'Already submitted'})
    else:
      add=contactf_tb(name=cname,email=cemail,subject=csubject,phone=cphone,message=cmessage)
      add.save()
      x = ''.join(random.choices(cname + string.digits, k=8))
      y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
      subject = 'Welcome to crystal shine cleaning'
      message = f'Hi {cname}, Thank you for valuable feeback.'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [cemail, ]
      send_mail( subject, message, email_from, recipient_list )
      asubject = 'Contact form '
      amessage = f' A message from  {cname},{cmessage}, contact number is {cphone} '
      aemail_from = settings.EMAIL_HOST_USER 
      arecipient_list = [settings.EMAIL_HOST_USER , ] 
      send_mail( asubject, amessage, aemail_from, arecipient_list )
      return render(request,'index.html',{'success':'Thankyou for submitting'})
  else:
    return render(request,'contact.html')	

def gallery(request):
  data=gallery_tb.objects.all()
  return render(request,'gallery.html',{'details':data})

def single(request):
  catid=request.GET['cid']
  data=service_tb.objects.filter(category=catid)
  return render(request,'single.html',{'details':data})

def get(request):
  if request.method == "POST":
    sid=request.GET['sid']
    cname=request.POST['name']
    cemail=request.POST['email']
    cphone=request.POST['phone']
    caddress=request.POST['address']
    sid=service_tb.objects.get(id=sid )
    check=getin_tb.objects.filter(phone=cphone)
    if check:
      sid=request.GET['sid']
      return render(request,'get.html',{'error':'already booked','details':sid})
    else:
      add=getin_tb(name=cname,email=cemail,phone=cphone,address=caddress,serid=sid)
      add.save()
      x = ''.join(random.choices(cname + string.digits, k=8))
      y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
      subject = 'Welcome to crystal shine cleaning'
      message = f'Hi {cname}, Thank you for booking our service. '
      email_from = settings.EMAIL_HOST_USER 
      recipient_list = [cemail, ] 
      send_mail( subject, message, email_from, recipient_list )
      asubject = 'Contact form '
      amessage = f' A message from  {cname},{caddress}, contact number is {cphone} '
      aemail_from = settings.EMAIL_HOST_USER 
      arecipient_list = [settings.EMAIL_HOST_USER , ] 
      send_mail( asubject, amessage, aemail_from, arecipient_list )


      return render(request,'index.html',{'success':"Thankyou for booking"})
  else:
    sid=request.GET['sid']
    return render(request,'get.html',{'details':sid})



#############################################admin######################################################

def admin_index(request):
  if request.session.has_key("id1"):
    return render(request,'admin/index.html')
  else:
    return HttpResponseRedirect('/admin_login/')    

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
               return render(request,'admin/login.html',{'success':'successfully Registered'})
   else:
       return render(request,'admin/register.html')    

def admin_forms(request):
  if request.session.has_key("id1"):
    category=category_tb.objects.all()
    if request.method=="POST":
      cname=request.POST["name"]
      ccategory=request.POST["category"]
      ccategory=category_tb.objects.get(id=ccategory)
      cprice=request.POST["price"]
      cdescription=request.POST["desc"]
      cimage=request.FILES["image"]
      check=service_tb.objects.filter(servicename=cname)
      if check:
        return render(request,'admin/forms.html',{'error':'Already Registered',"data":category})
      else:
        add=service_tb(servicename=cname,category=ccategory,price=cprice,desc=cdescription,image=cimage)
        add.save()
        return render(request,'admin/index.html',{'success':'Data Saved'})
    else:
      return render(request,'admin/forms.html',{"data":category})
  else:
    return HttpResponseRedirect('/admin_login/') 

def admin_cform(request):
  if request.session.has_key("id1"):
      if request.method=="POST":
         ccategory=request.POST["category"]
         cimage=request.FILES["images"]
         check=category_tb.objects.filter(category=ccategory)
         if check:
                return render(request,'admin/cform.html',{'error':'Already Registered'})
         else:
                add=category_tb(category=ccategory,image=cimage)
                add.save()
                return render(request,'admin/index.html',{'success':'Data Saved'})
      else:
          return render(request,'admin/cform.html')
  else:
    return HttpResponseRedirect('/admin_login/') 

def admin_table(request):
  if request.session.has_key("id1"):
    data=service_tb.objects.all()
    return render(request,'admin/table.html',{'details':data})
  else:
    return HttpResponseRedirect('/admin_login/')  

def admin_update(request):
  if request.method=="POST":
        cname=request.POST["name"]
        ccategory=request.POST["category"]
        service=category_tb.objects.get(id=ccategory)
        cprice=request.POST["price"]
        cdesc=request.POST["desc"]
        serid=request.GET['uid']
        imgval=request.POST['imgup']
        if imgval == "Yes":

          cimage=request.FILES['image']
          oldrec=service_tb.objects.filter(id=serid)
          updrec=service_tb.objects.get(id=serid)
          for x in oldrec:
              if x.image: 
                imgurl=x.image.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('successfully deleted')
          updrec.image=cimage
          updrec.save()        
        add=service_tb.objects.filter(id=serid).update(servicename=cname,category=service,price=cprice,desc=cdesc)
        return HttpResponseRedirect('/admin_table/')
  else:
        serid=request.GET['uid']
        data=service_tb.objects.filter(id=serid)
        return render(request,"admin/update.html",{'details':data})

def admin_delete(request):
  serid=request.GET['uidd']
  oldrec=service_tb.objects.filter(id=serid)
  for x in oldrec:
    imgurl=x.image.url
    pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
    if os.path.exists(pathtoimage):
      os.remove(pathtoimage)
  data=service_tb.objects.filter(id=serid).delete()
  return HttpResponseRedirect('/admin_table/')

def  admin_gallery(request):
  if request.session.has_key("id1"):
    if request.method == "POST":
      cimage=request.FILES['image']
      check=gallery_tb.objects.filter(image=cimage)
      if check:
        return render(request,'admin/gallery.html',{'error':'already registered'})
      else:
        add=gallery_tb(image=cimage)
        add.save()
        return render(request,'admin/index.html',{'success':"data saved"})
    else:
      return render(request,'admin/gallery.html')
  else:
    return HttpResponseRedirect('/admin_login/')

def admin_gallerytb(request):
  if request.session.has_key("id1"):
    data=gallery_tb.objects.all()
    return render(request,'admin/gallerytb.html',{'details':data})
  else:
    return HttpResponseRedirect('/admin_login/') 
  
def admin_galldlt(request):
      fid=request.GET['did']
      oldrec=gallery_tb.objects.filter(id=fid)
      for x in oldrec:
        imgurl=x.image.url
        pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
        if os.path.exists(pathtoimage):
          os.remove(pathtoimage)
      data=gallery_tb.objects.filter(id=fid).delete()
      return HttpResponseRedirect('/admin_gallerytb/')

def admin_contacttb(request):
  if request.session.has_key("id1"):
    data=contactf_tb.objects.all()
    return render(request,'admin/contacttb.html',{'details':data})
  else:
    return HttpResponseRedirect('/admin_login/')   

def admin_ctable(request):
  if request.session.has_key("id1"):
    data=category_tb.objects.all()
    return render(request,'admin/ctable.html',{'details':data})
  else:
    return HttpResponseRedirect('/admin_login/')

def admin_cupdate(request):
  if request.method=="POST":
        ccategory=request.POST["category"]
        cid=request.GET['uid']
        imgval=request.POST['imgup']
        if imgval == "Yes":

          cimage=request.FILES['images']
          oldrec=category_tb.objects.filter(id=cid)
          updrec=category_tb.objects.get(id=cid)
          for x in oldrec:
              if x.image: 
                imgurl=x.image.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('successfully deleted')
          updrec.image=cimage
          updrec.save()        
        add=category_tb.objects.filter(id=cid).update(category=ccategory)
        return HttpResponseRedirect('/admin_ctable/')
  else:
        cid=request.GET['uid']
        data=category_tb.objects.filter(id=cid)
        return render(request,"admin/cupdate.html",{'details':data})

def admin_tform(request):
  if request.session.has_key("id1"):
    if request.method=="POST":
      cimage=request.FILES["image"]
      cname=request.POST["name"]
      cdesc=request.POST["desc"]
      ccontact=request.POST["contact"]
      add=team_tb(image=cimage,name=cname,desc=cdesc,contact=ccontact)
      add.save()
      return render(request,'admin/index.html',{'success':'Data Saved'})
    else:
      return render(request,'admin/tform.html')
  else:
    return HttpResponseRedirect('/admin_login/')

def admin_ttable(request):
  if request.session.has_key("id1"):
    data=team_tb.objects.all()
    return render(request,'admin/ttable.html',{'details':data})
  else:
    return HttpResponseRedirect('/admin_login/')

def admin_tupdate(request):
  if request.method=="POST":
        cname=request.POST["name"]
        cdesc=request.POST["desc"]
        ccontact=request.POST["contact"]
        cid=request.GET['uid']
        imgval=request.POST['imgup']
        if imgval == "Yes":

          cimage=request.FILES['image']
          oldrec=team_tb.objects.filter(id=cid)
          updrec=team_tb.objects.get(id=cid)
          for x in oldrec:
              if x.image: 
                imgurl=x.image.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('successfully deleted')
          updrec.image=cimage
          updrec.save()        
        add=team_tb.objects.filter(id=cid).update(name=cname,desc=cdesc,contact=ccontact)
        return HttpResponseRedirect('/admin_ttable/')
  else:
        cid=request.GET['uid']
        data=team_tb.objects.filter(id=cid)
        return render(request,"admin/tupdate.html",{'details':data}) 

def admin_tdelete(request):
  cid=request.GET['uidd']
  oldrec=team_tb.objects.filter(id=cid)
  for x in oldrec:
    imgurl=x.image.url
    pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
    if os.path.exists(pathtoimage):
      os.remove(pathtoimage)
  data=team_tb.objects.filter(id=cid).delete()
  return HttpResponseRedirect('/admin_ttable/')

def admin_booking(request):
  if request.session.has_key("id1"):
    data=getin_tb.objects.all()
    return render(request,'admin/booking.html',{'details':data})
  else:
    return HttpResponseRedirect('/admin_login/')

                               
                     





         

  
          			