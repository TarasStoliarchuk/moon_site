from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('accounts/profile/add', views.profile_post_add, name='profile_post_add'),
    path('accounts/register/done', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', views.RegisterUserView.as_view(), name='register'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/alluser/', views.alluser, name='alluser'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/main_for_all/<int:pk>/', views.main_for_all, name='main_for_all'),
    path('accounts/logout/', views.MoonLogoutView.as_view(), name='logout'),
    path('accounts/login/', views.MoonLoginView.as_view(), name='login'),
    path('post/<str:author>/<int:post_pk>/', views.detail, name='detail'),
    path('', views.home, name='home'),
]
