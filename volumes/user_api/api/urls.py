from django.urls import path, include
from .views import SimpleAPIView, PlayerStatesViewSet
from .views import custom_login_view, custom_signup_view

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'playerstates', PlayerStatesViewSet)


urlpatterns = [
    path('simple/', SimpleAPIView.as_view(), name='simple-api'),
    path('test', include(router.urls)),

    
    path('login/', custom_login_view, name='custom_login_view'),
    path('signup/', custom_signup_view, name='custom_signup_view'),
]


