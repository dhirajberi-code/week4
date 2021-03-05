from django.urls import path
from . import views

urlpatterns = [
    path('forgetpassword/', views.forgetpassword,name="forgetpassword"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('org_signup/', views.org_signup,name="org_signup"),
    path('category_signup/', views.category_signup,name="category_signup"),
    path('student_signup/', views.student_signup,name="student_signup"),
    path('tp_signup/', views.tp_signup,name="tp_signup"),
    path('verify_user/', views.verify_user,name="verfy_user"),




]