from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CharacterCreationAPIView,
    CharacterListCreationAPIView,
    CharacterDeleteAPIView,
    CharacterDetailAPIView,
    CharacterListAPIView,
    CharacterUpdateAPIView,
)

app_name = 'characters_api'
urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', CharacterListCreationAPIView.as_view()),
    path('create/', CharacterCreationAPIView.as_view()),
    path('all/', CharacterListAPIView.as_view()),
    path('detail/<int:pk>/', CharacterDetailAPIView.as_view(),
         name='character-detail'),
    path('detail/<int:pk>/update/', CharacterUpdateAPIView.as_view()),
    path('detail/<int:pk>/delete/', CharacterDeleteAPIView.as_view()),
]
