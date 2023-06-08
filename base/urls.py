from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage),

    path('signup/',views.signup),
    path('frontpage/', views.frontpage),

    path('login/',auth_views.LoginView.as_view(template_name='base/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    path('lobby/', views.lobby),
    path('room/', views.room),

    path('get_token/',views.getToken),

    path('create_member/',views.createMember),

    path('get_member/',views.getMember),
    path('delete_member/',views.deleteMember),


]