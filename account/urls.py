from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Signup, name="signup"),
    path('login/', views.Login, name="login"),
    path('registered/', views.success_register, name="register_success"),
    path('dashboard/', views.Dash, name="dashboard"),
    path('logout/', views.Logout, name="logout"),
]