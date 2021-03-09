from django.urls import path
from . import views
urlpatterns = [
    path('OrganizationDashboard/',views.OrganizationDashboard),
    path('OrganizationHome/',views.OrganizationHome),
    path('OrganizationStudentRequest/',views.OrganizationStudentRequest,name='OrganizationStudentRequest'),
    path('OrganizationAllStudent/',views.OrganizationAllStudent,name='OrganizationAllStudent'),
    path('OrganizationBlockedStudent/',views.OrganizationBlockedStudent,name='OrganizationBlockedStudent'),
]
