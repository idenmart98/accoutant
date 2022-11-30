from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm


def index_view(request):
    form = UserForm(request.POST or None) 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(
        request, 
        'login.html', 
        {"form":form}
        )