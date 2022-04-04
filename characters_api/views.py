from rest_framework import generics
from characters.models import Character
from .serializers import CharacterSerializer


class CharacterListCreationAPIView(generics.ListCreateAPIView):
    """class API for character creation and Character List"""
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.all()


class CharacterCreationAPIView(generics.CreateAPIView):
    """class API for character creation"""
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.all()


class CharacterListAPIView(generics.ListAPIView):
    """class API for listing all the characters"""
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.all()


class CharacterDetailAPIView(generics.RetrieveAPIView):
    """class API to get an especific character"""
    serializer_class = CharacterSerializer
    lookip_field = 'pk'

    def get_queryset(self):
        return Character.objects.all()


class CharacterUpdateAPIView(generics.UpdateAPIView):
    """class API to update an especific character"""
    serializer_class = CharacterSerializer
    lookip_field = 'pk'

    def get_queryset(self):
        return Character.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        return instance


class CharacterDeleteAPIView(generics.DestroyAPIView):
    """class API to delete an especific character"""
    serializer_class = CharacterSerializer
    lookip_field = 'pk'

    def get_queryset(self):
        return Character.objects.all()

    def perform_delete(self, serializer):
        instance = serializer.save()
        return instance
