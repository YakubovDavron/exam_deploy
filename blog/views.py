from rest_framework import generics
from .models import About

# Create your views here.

from .seri import AboutSerializer


class AboutApiView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
