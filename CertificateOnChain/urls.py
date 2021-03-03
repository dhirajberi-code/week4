
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('Admin.urls')),
	path('', include('Student.urls')),
	path('', include('Organization.urls')),
	path('', include('Third_party_Organization.urls')),
	path('', include('Account.urls')),
	
]
