from django.urls import path
from . import views as views

urlpatterns = [
    path('user/', views.UserRecordView.as_view(), name='users'),
    path("register/", views.CreateUserAPIView.as_view(), name="register"),

    # for login and logout


]
