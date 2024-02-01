from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('user/register/', views.register, name='register'),
]