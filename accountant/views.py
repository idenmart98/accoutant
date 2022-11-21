from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .forms import ProfileForm


def index_view(request):
    form = ProfileForm  
    return render(
        request, 
        'login.html', 
        {"form":form}
        )

def index_view2(request):
    return HttpResponse(3+3)

