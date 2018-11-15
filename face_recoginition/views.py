from django.shortcuts import render

# Create your views here.

def index(request):
    # main page
    return render(request, 'face_recoginition/index.html')