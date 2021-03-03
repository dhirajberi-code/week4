from django.conf.urls import url
from django.shortcuts import redirect, render
import requests
# Create your views here.

def forgetpassword(request):
	return render(request,'forget-password.html')

def login(request):
	if request.method=="POST":
		print("post method")
		email=request.POST['email']
		password=request.POST['pass']
		detail={'email':email,'password':password}
		print(detail)
		r = requests.post('http://127.0.0.1:8080/login',json=detail)
		print(r)
		if str(r)=='<Response [200]>':
			return redirect('/StudentDashboard')
		else:
			print('here')
			return redirect('login')
	else:
		return render(request,'login.html')

def adminlogin(request):
	return render(request,'admin_login.html')

def category_signup(request):
	return render(request,'category-signup.html')

def org_signup(request):
	return render(request,'organization-signup.html')

def student_signup(request):
	return render(request,'student-signup.html')

def tp_signup(request):
	return render(request,'third-party-signup.html')
	
def verify_user(request):
	return redirect('/StudentDashboard/')