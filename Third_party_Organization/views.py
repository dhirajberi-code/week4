from django.shortcuts import render

# Create your views here.
def ThirdPartyOrganizationDashboard(request):
	print("Here")
	return render(request,'./dist/ThirdPartyOrganizationBase.html')
	
