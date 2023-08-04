from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index.as_view()),
    path('home/',views.home.as_view(),name='home'),
    path('task/',views.TaskListView.as_view(),name='TaskListView'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='TaskDetailView'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='TaskDeleteView'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='TaskUpdateView'),
    path('searchresults/',views.Search.as_view(),name='search'),
 ]