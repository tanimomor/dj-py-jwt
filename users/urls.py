from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import RegisterView, UserViewSet, LoginView, UserView, LogoutView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('', include(router.urls)),
]
