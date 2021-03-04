from django.urls import path
from . import views
urlpatterns = [
    path('AdminDashboard/',views.AdminDashboard),
	path('request/',views.AdminOrgRequest),
	path('list/',views.AdminOrgList),
	path('block/',views.AdminOrgBlock),
	path('tporequest/',views.AdminTPORequest),
	path('ViewPerticularOrg/',views.AdminViewPerticularOrg,name='ViewPerticularOrg'),
	path('AdminHome/',views.AdminHome),
	
]
