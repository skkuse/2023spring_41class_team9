from django.shortcuts import render

# Create your views here.

def practice(request):
    return render(request, 'practice.html')

def real(request):
    return render(request, 'real.html')