from rest_framework import serializers
from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """Serializar for the Character model"""
    class Meta:
        model = Character
        fields = [
            'name',
            'gender',
            'faction',
            'race',
            'job',
            'age',
            'description'
        ]
    
   