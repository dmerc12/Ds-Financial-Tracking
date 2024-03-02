from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='user-home'),
    path('register/', views.register, name='register'),
    path('update/', views.update_user, name='update-user'),
    path('change-password/', views.change_password, name='change-password'),
    path('delete/', views.delete_user, name='delete-user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
