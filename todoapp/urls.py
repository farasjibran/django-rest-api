from django.contrib import admin
from django.urls import path, include
from todoapi import urls as todo_urls
from account import urls as account_urls
from todoapi.models import Todo

# register models to django admin
admin.site.register(Todo)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls')),
  path('api/', include(todo_urls)),
  path('api/account/', include(account_urls))
]
