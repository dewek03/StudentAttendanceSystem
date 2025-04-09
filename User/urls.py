from django.urls import path
from .views import index, user_login, user_register, landing_page, user_logout

urlpatterns = [
    path('', index, name='index'),  # Main landing page
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('landing/', landing_page, name='landing'),
    path('logout/', user_logout, name='logout'),
]