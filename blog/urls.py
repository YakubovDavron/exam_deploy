from django.urls import path
from .views import AboutApiView

urlpatterns = [
     path('about/', AboutApiView.as_view(), name='about'),
]