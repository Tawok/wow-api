from rest_framework import authentication, generics, permissions
from characters.models import Character
from .serializers import (CharacterSerializer,
                          CharacterDetailSerializer,
                          CharacterListSerializer,
                          CharacterCreationSerializer)
from .permissions import IsStaffPermission


class CharacterListCreationAPIView(generics.ListCreateAPIView):
    """class API for character creation and Character List"""
    serializer_class = CharacterSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAdminUser,
                          IsStaffPermission,
                          permissions.IsAuthenticatedOrReadOnly
                          ]

    def get_queryset(self):
        return Character.objects.all()

    def perform_create(self, serializer):
        """auto populate the user field with the logged-in user"""
        instance = serializer.save(user=self.request.user)
        return instance


class CharacterCreationAPIView(generics.CreateAPIView):
    """class API for character creation"""
    serializer_class = CharacterCreationSerializer

    def get_queryset(self):
        return Character.objects.all()

    def perform_create(self, serializer):
        """auto populate the user field with the logged-in user"""
        instance = serializer.save(user=self.request.user)
        return instance


class CharacterListAPIView(generics.ListAPIView):
    """class API for listing all the characters"""
    serializer_class = CharacterListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Character.objects.all()
        return Character.objects.filter(user=self.request.user)


class CharacterDetailAPIView(generics.RetrieveAPIView):
    """class API to get an especific character"""
    serializer_class = CharacterDetailSerializer
    lookip_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
