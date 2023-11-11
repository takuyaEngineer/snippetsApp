from django.shortcuts import render

# Create your views here.

def LoginIndex(request):
    return render(request, 'login/index.html')