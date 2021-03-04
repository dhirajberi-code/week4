from django.urls import path
from . import views
urlpatterns = [
    path('ThirdPartyOrganizationDashboard/',views.ThirdPartyOrganizationDashboard),
    path('ThirdPartyOrganizationHome/',views.ThirdPartyOrganizationHome),
]
