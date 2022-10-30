from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('createTask', CreateTask.as_view(), name='createTask'),
    path('updateTask/<int:pk>/', UpdateTask.as_view(), name='updateTask'),
    path('deleteTask/<int:pk>/', DeleteTask.as_view(), name='deleteTask'),
    path('login', LoginTask.as_view(), name='login'),
    path('Logaut', LogoutView.as_view(next_page='login'), name='logaut'),
    path('register', register.as_view(), name='register')




]
