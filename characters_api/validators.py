from characters.models import Character
from rest_framework import serializers

def contains_num(word):
        return ''.join([i for i in word if i.isdigit()])

def validate_name(value):
        qs = Character.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('This character already exists')
        if contains_num(value).isnumeric():
            raise serializers.ValidationError("Name can't contain numbers")
        return value
