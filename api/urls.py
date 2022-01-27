from django.urls import path
from rest_framework.authtoken import views as authviews
from . import views

urlpatterns=[
    path('',(views.list_endpoints)),
    path('data/',(views.data)), # working
    path('data/create/',(views.create_data)), # workinhg
    path('data/<str:pk>/update',(views.update_data)), 
    path('byid/<str:pk>',(views.get_by_name)), #working
    path('data/delete/<str:pk>',(views.deletedata)), # working
    path('user/',views.UserRecordView.as_view(),name='users'),


    # for login and logout


]