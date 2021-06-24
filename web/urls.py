from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name="main"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('alarm/', views.alarm, name="alarm"),
]
