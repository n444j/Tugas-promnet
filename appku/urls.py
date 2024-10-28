from django.urls import path
from . import views

urlpatterns = [
    path('', views.profil_umum, name='profil_umum'),
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('pengalaman_kerja/', views.pengalaman_kerja, name='pengalaman_kerja'),
    path('sosial_media/', views.sosial_media, name='sosial_media'), 
]
