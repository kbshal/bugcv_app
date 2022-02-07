from django.urls import path
from . import views as views

urlpatterns = [
    path('data/', (views.data)),  # working
    # path('data/create/',(views.create_data)), # workinhg
    # path('data/<str:pk>/update',(views.update_data)),
    # path('byid/<str:pk>',(views.get_by_name)), #working
    # path('data/delete/<str:pk>',(views.deletedata)), # working
    path('user/', views.UserRecordView.as_view(), name='users'),
    path("register/", views.CreateUserAPIView.as_view(), name="register"),
    path('', (views.list_endpoints)),

    # for login and logout


]
