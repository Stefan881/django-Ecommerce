from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-url'),
    path('about/', views.about, name='about-url'),
    path('login/', views.login_user, name='login-url'),
    path('logout/', views.logout_user, name='logout-url'),
    path('register/', views.register_user, name='register-url'),
]
