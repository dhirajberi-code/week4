from django.shortcuts import render

# Create your views here.
def AdminDashboard(request):
	return render(request,'./dist/admin_org_all_view.html')

def AdminOrgList(request):
	return render(request,'./dist/admin_org_all_view.html')

def AdminOrgRequest(request):
	return render(request,'./dist/admin_org_request.html')
	
def AdminOrgBlock(request):
	return render(request,'./dist/admin_org_blocked_view.html')

def AdminTPORequest(request):
	return render(request,'./dist/admin_tpo_request_view.html')	