from main_app.models import Posts
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.UserProfileList.as_view(), name="profile_list"),
    path('profile/<int:pk>/', views.PostsDetail.as_view(), name="profile_detail"),
    path('profile/<int:pk>/posts/new',views.PostsCreate.as_view(), name="posts_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]
