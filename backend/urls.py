from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.endpoints),
    path('data/',views.access_api),
    path('data/<str:pk>',views.get_by_id)
]
