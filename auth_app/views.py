from django.http import HttpResponse
from django.shortcuts import render
from .models import homemodel
# Create your views here.
def regview(request):
    if request.method == 'POST':
        a=homemodel()
        a.Username= request.POST.get('name')
        a.password = request.POST.get('password')
        a.designation = request.POST.get('designation')
        a.save()
        return HttpResponse('success')
    return render(request,'registration.html')
