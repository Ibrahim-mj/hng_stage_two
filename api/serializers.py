from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core import validators
from bleach import clean

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField(
        validators=[
            validators.EmailValidator(message="Provide a valid Email"), 
            UniqueValidator(queryset=Person.objects.all(), message="Email already exists")
        ]
    )
    occupation = serializers.CharField(max_length=100)

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Name must be letters only')
        return clean(value)

    def validate_age(self, value):
        if not value >= 1:
            raise serializers.ValidationError('Age can not be less than 1')
        if not isinstance(value, int):
            raise serializers.ValidationError('Age must be a number')
        return clean(value)
    
    def validate_occupation(self, value):
        if not value.isalpha():
            raise serializers.ValidationError('Occupation must be letters only')
        return clean(value)
    
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'occupation']