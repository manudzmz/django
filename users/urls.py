from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView

router = DefaultRouter()
router.register('api/1.0/users', UserViewSet, base_name='api_users_')

urlpatterns = [
    # Web URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    # API URLs
    # url(r'^api/1.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    # url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail'),
    url(r'', include(router.urls)),
]
