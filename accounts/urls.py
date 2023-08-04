from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration', views.registration, name='register'),
    path('accounts/login/', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]