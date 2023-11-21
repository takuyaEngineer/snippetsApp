from django.shortcuts import render, redirect
from common.views import ComSessionCheck
from django.conf import settings

def top(request):
    return render(request, 'top/index.html')