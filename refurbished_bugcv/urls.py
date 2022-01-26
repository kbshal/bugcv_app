from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

    
]
