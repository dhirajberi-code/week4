from django.urls import path
from . import views
urlpatterns = [
    path('ThirdPartyOrganizationDashboard/',views.ThirdPartyOrganizationDashboard,name='ThirdPartyOrganizationDashboard'),
    path('ThirdPartyOrganizationHome/',views.ThirdPartyOrganizationHome,name='ThirdPartyOrganizationHome'),
]
