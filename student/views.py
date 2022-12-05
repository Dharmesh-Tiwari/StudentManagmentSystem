from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Records
def signup(req):
    return render(req,"signup.html")

def home(req):
    return render(req,'home.html')
def signuptask(req):
    ob=Records()
    ob.name=req.POST.get("name")
    ob.email=req.POST.get("email")
    ob.dob=req.POST.get("dob")
    ob.mobile=req.POST.get("mobile")
    ob.password=req.POST.get("password")
    ob.role=req.POST.get("role")
    ob.save() 
    return redirect("/home")
def login(req):
    return render(req,'login.html')
global Name
global Email
def loginTask(req):
	role=req.POST.get('role')
	if role=="student":
		global Email
		Email=req.POST.get('email')
		password=req.POST.get('password')
		global data
		data=Records.objects.all()
		for i in data:
			if role==i.role:
				if Email==i.email:
					if password==i.password:
						
						Name=i.name
						return render(req,"student.html",{"name":Name})
		else:
			h="No User Found!!"
			return render(req,"login.html",{"span":h})
	elif role=="admin":
		email=req.POST.get('email')
		password=req.POST.get('password')
		data=Records.objects.all()
		for i in data:
			if role==i.role:
				if email==i.email:
					if password==i.password:
						name=i.name
						return render(req,"admin.html",{"list":data,"name":name})		
		else:
			h="No User Found!!"
			return render(req,"login.html",{"span":h})
	elif role=="faculty":
		email=req.POST.get('email')
		password=req.POST.get('password')
		data=Records.objects.all()
		for i in data:
			if role==i.role:
				if email==i.email:
					if password==i.password:
						name=i.name.capitalize()
						return render(req,"faculty.html",{"list":data,"name":name})		
		else:
			h="No User Found!!"
			return render(req,"login.html",{"span":h})
def student(req):
	
	return render(req,"student.html")

def admin(req):
    return render(req,'admin.html')
	
	#student particular profile

def profile(req):
	rec=Records.objects.filter(email=Email)
	
	return render(req,"profile.html",{"list":rec})

def stprofile(req):
	sdata=Records.objects.filter(role="student")
	return render(req,"stprofile.html",{"list":sdata})

def facultyprofile(req):
	fdata=Records.objects.filter(role="faculty")
	return render(req,"facultyprofile.html",{"list":fdata})
def faculty(req):
	return render(req,'faculty.html')	
def adminprofile(req):
	adata=Records.objects.filter(role="admin")
	return render(req,"adminprofile.html",{"list":adata})
def newstudent(req):
	return render(req,"newstudent.html")
def addstudent(req):
	oe=Records()
	oe.name=req.POST.get("name")
	oe.email=req.POST.get("email")
	oe.dob=req.POST.get("dob")
	oe.mobile=req.POST.get("mobile")
	oe.password=req.POST.get("password")
	oe.role="student"
	oe.save() 
	return redirect("/admin")
def profiles(req):
	rec=Records.objects.all()
	print(rec)
	return render(req,'delete.html',{"list":rec})
def delete(req):
	return render(req,"delete.html")
def deletetask(req):
	id=req.GET.get('id')
	obj=Records.objects.get(id=id)
	obj.delete()
	return redirect("/profiles")




				#student update
def updatestudent(req):
	rec=Records.objects.filter(email=Email)
	return render(req,"updatestudent.html",{"list":rec})
	
def updatetask(req):
	ID=req.POST.get("id")
	print(ID)
	oc=Records.objects.get(id=ID)
	oc.name=req.POST.get("name")
	oc.email=req.POST.get("email")
	oc.mobile=req.POST.get("mobile")
	oc.dob=req.POST.get("dob")
	oc.password=req.POST.get("password")
	oc.role="student"
	oc.save() 
	print("this is ",oc)
	return redirect("/updatestudent")





def updaterecord(req):
	rec=Records.objects.all()
	return render(req,'updaterecord.html',{"list":rec})

def updaterecordtask(req):
	u_id=req.GET.get("id")
	of=Records.objects.get(id=u_id)
	of.name=req.POST.get("name")
	of.email=req.POST.get("email")
	of.mobile=req.POST.get("mobile")
	of.dob=req.POST.get("dob")
	of.password=req.POST.get("password")
	of.role=req.POST.get("role")
	of.save() 
	return redirect("/admin")	
	

