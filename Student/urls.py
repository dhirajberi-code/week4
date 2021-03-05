from django.urls import path
from . import views
urlpatterns = [
    path('StudentDashboard/',views.StudentDashboard,name='StudentDashboard'),
    path('StudentViewProfile/',views.StudentViewProfile,name='StudentViewProfile'),
    path('StudentEditProfile/',views.StudentEditProfile,name='StudentEditProfile'),
    path('SaveStudentProfile/',views.SaveStudentProfile,name='SaveStudentProfile'),
    path('StudentHome/',views.StudentHome,name='StudentHome'),
    path('StudentChangePassword/',views.StudentChangePassword,name='StudentChangePassword'),
    path('ListOfCertificate/',views.ListOfCertificate,name='ListOfCertificate'),
    path('RequestForCertificate/',views.RequestForCertificate,name='RequestForCertificate'),
    path('ViewCertificate/',views.ViewCertificate,name='ViewCertificate'),
    path('RequestForNewCategory/',views.RequestForNewCategory,name='RequestForNewCategory'),
]
