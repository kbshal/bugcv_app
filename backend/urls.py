from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.endpoints),
    path('',views.access_api),
]
