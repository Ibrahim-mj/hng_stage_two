from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core import validators
from bleach import clean

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True,
    )
    name = serializers.CharField(
        max_length=100, 
        validators=[
            validators.RegexValidator(r'^[a-zA-Z ]+$', 'Name must be letters only'),
            UniqueValidator(queryset=Person.objects.all(), message='Name already exists, make it a bit different')
        ]
    )
    age = serializers.IntegerField(
        required=False,
        validators=[
            validators.MinValueValidator(1, message='Age can not be less than 1'),
            validators.MaxValueValidator(150, message='Age can not be greater than 150')
        ]
    )
    email = serializers.EmailField(
        required=False,
        validators=[
            validators.EmailValidator(),
            UniqueValidator(queryset=Person.objects.all(), message="Email already exists")
        ]
    )
    occupation = serializers.CharField(
        required=False,
        max_length=100, 
        validators=[
            validators.RegexValidator(r'^[a-zA-Z ]+$', 'Occupation must be letters only')
        ]
    )
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'email', 'occupation']