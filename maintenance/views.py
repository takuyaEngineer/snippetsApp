from django.shortcuts import render

def Except(request):
    return render(request, "maintenance/except.html")