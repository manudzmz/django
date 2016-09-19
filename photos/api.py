from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.serializers import PhotoSerializer, PhotoListSerializer
from photos.views import PhotoQuerySet


class PhotoViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return PhotoQuerySet.get_photos_by_user(self.request.user)

    def get_serializer_class(self):
        return PhotoSerializer if self.action != "list" else PhotoListSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(owner=self.request.user)
