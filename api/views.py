from django.shortcuts import render
from rest_framework import generics
from .serializers import PersonSerializer
from .models import Person

# Create your views here.
class PersonView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    search_fields = ['name', 'occupation']
    ordering_fields = ['name', 'occupation']

    def get_queryset(self):
        """
        Optionally restricts the returned response to a given user
        """
        queryset = Person.objects.all()
        name = self.request.query_params.get('name')
        occupation = self.request.query_params.get('occupation')
        if name is not None:
            queryset = queryset.filter(name=name)
        if occupation is not None:
            queryset = queryset.filter(occupation=occupation)
        else:
            queryset = queryset.all()
        return queryset

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer