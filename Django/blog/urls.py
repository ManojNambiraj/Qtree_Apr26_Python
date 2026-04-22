from django.contrib import admin
from django.urls import path
from userapp.views import UserApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserApi.as_view())
]
