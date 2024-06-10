from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('contact/',views.contact,name="contact"),
    path('careers/',views.careers,name="careers"), 
    path('form_submitted/', views.form_submitted, name="form_submitted"),
    path('careers/data_analyst/',views.data_analyst, name='data_analyst'),
    path('careers/it_consultant/',views.it_consultant, name="it_consultant"),
    path('careers/network_engineer/',views.network_engineer, name="network_engineer"),
    path('careers/project_manager/',views.project_manager,name="project_manager"),
    path('careers/senior_software_engineer/',views.senior_software_engineer,name='senior_software_engineer'),
    path('careers/application/',views.application,name='application'),
    path('careers/application/submit/', views.submit_application, name='submit_application'),
]
