from django.urls import path,include
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register("patient",views.CreateUser,basename="create_patient")
router.register("doctor",views.CreateDoctor,basename="create_docter")
router.register("history",views.CreatePatientHistory,basename="create_history")
urlpatterns = [
    path("create/",include(router.urls)),
    path("profile/",views.Profile.as_view()),
    path("history/",views.PatientHistoryView.as_view(),),
    path("doc_info/<int:id>",views.get_info_by_id,name="doc_info"),
]

