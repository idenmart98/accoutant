from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Profile
from .forms import ProfileForm


def index_view(request):
    form = ProfileForm(request.POST or None) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(
        request, 
        'login.html', 
        {"form":form}
        )

def index_view2(request):
    return HttpResponse(3+3)

