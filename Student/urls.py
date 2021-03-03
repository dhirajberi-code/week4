from django.urls import path
from . import views
urlpatterns = [
    path('StudentDashboard/',views.StudentDashboard,name='StudentDashboard'),
    path('StudentViewProfile/',views.StudentViewProfile,name='StudentViewProfile'),
    path('StudentEditProfile/',views.StudentEditProfile,name='StudentEditProfile'),
    path('SaveStudentProfile/',views.SaveStudentProfile,name='SaveStudentProfile'),
]
