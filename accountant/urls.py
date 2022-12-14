from django.urls import path, include
from .views import index_view, index_view2

urlpatterns = [
    path('', index_view),
    path('red/', index_view2),
    path('auth/<str:uid>', index_view2),
]
