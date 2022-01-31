
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views as authviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'), # to obtain the token of specific user

    
]
