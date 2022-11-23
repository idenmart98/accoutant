from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Profile
from .forms import ProfileForm


def index_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        Profile.objects.create(
            login=login,
            password=password
            )
    form = ProfileForm  
    return render(
        request, 
        'login.html', 
        {"form":form}
        )

def index_view2(request):
    return HttpResponse(3+3)

