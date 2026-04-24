from django.urls import path
from .views import UserAPI

urlpatterns = [
    path('users/', UserAPI.as_view()),
    path('users/<int:user_id>', UserAPI.as_view()),
]