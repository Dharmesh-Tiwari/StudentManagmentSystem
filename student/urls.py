
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('signup',views.signup),
    path('signuptask',views.signuptask),
    path('login',views.login),
    path('loginTask',views.loginTask),
    path('student',views.student),
    path('admin',views.admin),
    path('profile',views.profile),
    path('profiles',views.profiles),
    path('facultyprofile',views.facultyprofile),
    path('faculty',views.faculty),
    path('adminprofile',views.adminprofile),
    path('stprofile',views.stprofile),
    path('newstudent',views.newstudent),
    path('addstudent',views.addstudent),
    path('delete',views.delete),
    path('deletetask',views.deletetask),
    path('updatestudent',views.updatestudent),
    path('updatetask',views.updatetask),
    path('updaterecord',views.updaterecord),
    path('updaterecordtask',views.updaterecordtask),
]
