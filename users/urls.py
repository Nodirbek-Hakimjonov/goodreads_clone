from .views import RegisterView,LoginView,ProfileView,LogoutView,ProfileEditView
from django.urls import path

app_name='users'

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/edit/',ProfileEditView.as_view(),name='profile-edit')

]