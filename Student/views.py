from django.shortcuts import render,redirect
from django.http import HttpResponse  	
import requests

import requests,json
# Create your views here.


def StudentDashboard(request):
	return render(request,'./StudentBase.html')

def StudentViewProfile(request):
	data = requests.get('http://127.0.0.1:8080/viewProfile').json()
	return render(request, './dist/student-profile.html', {'data': data})

def StudentEditProfile(request):
	data = requests.get('http://127.0.0.1:8080/viewProfile').json()
	return render(request,'./dist/student-edit-profile.html',{'data': data})

def	SaveStudentProfile(request):
	print("Student Profile Save")
	return render(request,'./dist/student-profile.html')

def StudentHome(request):
	try:
		request.session['email']
		return render(request,'./dist/Student_home.html')
	except:
		return redirect('/login')

def ListOfCertificate(request):
	return render (request,'./dist/student_certificate_list.html')

def RequestForCertificate(request):
	return render (request,'./dist/student_request_for_certificate.html')

def RequestForNewCategory(request):
	return render (request,'./dist/student_request_for_new_category.html')

def StudentChangePassword(request):
	return render(request,'./dist/change-password.html')

def RequestForCertificate(request):
	return render(request,'./dist/request-certificate.html')

def RequestForNewCategory(request):
	return render(request,'./dist/request-new-category.html')

def ViewCertificate(request):
	return render(request,'./dist/certificate.html')