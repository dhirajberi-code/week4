from django.urls import path
from . import views
urlpatterns = [
    path('OrganizationDashboard/',views.OrganizationDashboard),
    path('OrganizationHome/',views.OrganizationHome),
    path('OrganizationStudentRequest/',views.OrganizationStudentRequest,name='OrganizationStudentRequest'),
]
