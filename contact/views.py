from rest_framework import generics
from .models import Contact
from .seri import ContactSerializer


# Create your views here.

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
