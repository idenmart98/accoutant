import uuid
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from .forms import ProfileForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile



def index_view(request):
    form = ProfileForm(request.POST or None) 
    message = "Заполните поля"
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.uid = uuid.uuid4().hex
            profile.save()
            url = f"{settings.SITE_NAME}accountant/auth/{profile.uid}"
            send_mail(
                subject='Проверка почты',
                message=url,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[profile.email])
            message = "Проверьте почту"
    return render(
        request, 
        'create.html', 
        {"form":form,
         "message":message}
        )

def index_view2(request, uid):
    profile = Profile.objects.get(uid=uid)
    profile.verified =True
    profile.save()
    return render(
        request, 
        'verify.html', 
        {"message":"Ваша почта потверждена"}
        )



