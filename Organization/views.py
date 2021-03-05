from django.shortcuts import render

# Create your views here.
def OrganizationDashboard(request):
	print("Here")
	return render(request,'OrganizationBase.html')

def OrganizationHome(request):
	return render(request,'./dist/organization_home.html')

def OrganizationStudentRequest(request):
	return render(request,'./dist/org_student_request.html')
