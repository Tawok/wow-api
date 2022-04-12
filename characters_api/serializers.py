from wsgiref import validate
from requests import request
from rest_framework import serializers
from characters.models import Character
from rest_framework.reverse import reverse
from .validators import validate_name


def contains_num(word):
    return ''.join([i for i in word if i.isdigit()])


class CharacterSerializer(serializers.ModelSerializer):
    """Serializar for the Character general view"""
    detail_url = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Character
        fields = [
            'detail_url',
            'pk',
            'name',
            'gender',
            'faction',
            'race',
            'job',
            'age',
            'description'
        ]

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('characters_api:character-detail', kwargs={'pk': obj.pk}, request=request)


class CharacterListSerializer(serializers.ModelSerializer):
    """Serializar for the Character list view"""
    detail_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Character
        fields = [
            'detail_url',
            'name',
        ]

    def get_detail_url(self, obj):
        request = self.context.get('request')
        print(request)
        if request is None:
            return None
        return reverse('characters_api:character-detail', kwargs={'pk': obj.pk}, request=request)


class CharacterDetailSerializer(serializers.ModelSerializer):
    """Serializar for the Character Detail view"""
    created_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Character
        fields = [
            'created_by',
            'pk',
            'name',
            'gender',
            'faction',
            'race',
            'job',
            'age',
            'description'
        ]

    def get_created_by(self, obj):
        return obj.user.email


class CharacterCreationSerializer(serializers.ModelSerializer):
    """Serializar for the Character creation and update view"""
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

    def validate_name(self, value):
        qs = Character.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('This character already exists')
        if contains_num(value).isnumeric():
            raise serializers.ValidationError("Name can't contain numbers")
        return value
