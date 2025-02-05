from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Import for login/logout

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),  # Use Django's built-in login view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), # Use Django's built-in logout view. Redirects to 'home' after logout.
    path('profile/', views.profile, name='profile'),
]
