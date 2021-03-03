from django.urls import path
from . import views
urlpatterns = [
    path('OrganizationDashboard/',views.OrganizationDashboard),
]
