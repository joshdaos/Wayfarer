from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.UserProfileList.as_view(), name="profile_list"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]
