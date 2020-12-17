from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
 
urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_list'),
    path('childname/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profiles/new', views.ProfileCreate.as_view(), name='profile_create'),
    path('childname/<int:pk>/edit', views.profile_edit, name='profile_edit'),
    path('childname/<int:pk>/delete', views.profile_delete, name='profile_delete'),
    path('', views.Home.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('staff/', views.Staff.as_view(), name='staff'),    
    path('login/', views.Login.as_view(), name='login'),    
]
