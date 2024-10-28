from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profil_umum(request):
    return render(request, 'apkku/profil_umum.html')

def pendidikan(request):
    return render(request, 'apkku/pendidikan.html')

def pengalaman_kerja(request):
    return render(request, 'apkku/pengalaman_kerja.html')

def sosial_media(request):
    return render(request, 'apkku/sosial_media.html')
