from django.urls import path

from userapp import views

urlpatterns = [
    path('', views.register_user, name='register'),
    path('login/',views.login_user,name='login'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('logout/',views.logout,name='logout'),
    path('addproject/',views.add_project,name='addproject'),
    path('viewproject/',views.view_project,name='viewproject'),
    path('addexperience/', views.add_experience, name='addexperience'),
    path('viewexperience/', views.view_experience, name='viewexperience'),
    path('addqualification/', views.add_qualification, name='addqualification'),
    path('viewqualification/', views.view_qualification, name='viewqualification'),
    path('addcertificate/', views.add_certificate, name='addcertificate'),
    path('viewcertificate/', views.view_certificate, name='viewcertificate'),

]