from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('career/', views.career, name='career'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('certificate/', views.certificate, name='certificate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pricing/', views.pricing, name='pricing'),
]
