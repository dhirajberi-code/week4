from django.shortcuts import render

# Create your views here.
def OrganizationDashboard(request):
	print("Here")
	return render(request,'./dist/OrganizationBase.html')
