from django.urls import path
from .views import RegisterUser, LoginUser, logout_user, ProfileView, update_profile

app_name = 'users'
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/update/', update_profile, name='update_profile')
]