from rest_framework import serializers
from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """Serializar for the Character model"""
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Character
        fields = [
            'user',
            'username',
            'name',
            'gender',
            'faction',
            'race',
            'job',
            'age',
            'description'
        ]

    def get_username(self, obj):
        """gets the email from the user field"""
        return obj.user.email