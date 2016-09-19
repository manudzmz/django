from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet
from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotoListView


router = DefaultRouter()
router.register('api/1.0/photos', PhotoViewSet, base_name='api_photos_')

urlpatterns = [
    # Web URLs
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_my_photos'),
    url(r'^photos/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^$', HomeView.as_view(), name='photos_home'),

    # API URLs
    # url(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='api_photos_list'),
    # url(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view(), name='api_photos_detail'),
    url(r'', include(router.urls)),
]
