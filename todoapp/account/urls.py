from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
  UserAction
)

urlpatterns = [
  path('login', obtain_auth_token, name='login'),
  path('logout', UserAction.as_view(), name='logout')
]