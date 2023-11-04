from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patientregistration', views.patientregistration, name='patientregistration'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('doctorregistration', views.doctorregistration, name='doctorregistration'),
    path('patientdashboard', views.patientdashboard, name='patientdashboard'),
    path('doctordashboard', views.doctordashboard, name='doctordashboard'),
    path('intake', views.intake, name='intake'),
    path('logout', views.logout, name='logout'),
    path('report', views.report, name='report'),
    path('application', views.application, name='application'),
    path('doctorheader', views.doctorheader, name='doctorheader'),
    path('predictions_patient', views.predictions_patient, name='predictions_patient'),
]