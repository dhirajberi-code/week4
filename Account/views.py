from django.conf.urls import url
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  
import requests
# Create your views here.

def forgetpassword(request):
	return render(request,'forget-password.html')

def login(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['pass']
		detail={'email':email,'password':password}
		r = requests.post('http://127.0.0.1:8080/login',json=detail)
		if str(r)=='<Response [200]>':
			#user = auth.authenticate(request, username=email, password=password)
			#print(user)
			request.session['email']=email
			#print(request.session['email'])
			return redirect('/StudentHome')
		else:
			return redirect('/login')
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		#auth.authenticate(request)
	except:
		pass
	return redirect('/login')

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