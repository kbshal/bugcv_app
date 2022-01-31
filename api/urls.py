from django.urls import path
from . import views as views

urlpatterns=[
    path('',(views.list_endpoints)),
    path('data/',(views.data)), # working
    #path('data/create/',(views.create_data)), # workinhg
    #path('data/<str:pk>/update',(views.update_data)), 
    #path('byid/<str:pk>',(views.get_by_name)), #working
    #path('data/delete/<str:pk>',(views.deletedata)), # working
    path('user/',views.UserRecordView.as_view(),name='users'),

    # for login and logout


]