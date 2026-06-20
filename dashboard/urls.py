from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_admin, name='index'),
    path('manage-users/', views.manage_users, name='manage_users'),
]