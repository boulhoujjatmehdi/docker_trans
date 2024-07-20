from django.urls import path, include
from .views import SimpleAPIView, PlayerStatesViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'playerstates', PlayerStatesViewSet)


urlpatterns = [
    path('simple/', SimpleAPIView.as_view(), name='simple-api'),
    path('productsstates', include(router.urls))
]


