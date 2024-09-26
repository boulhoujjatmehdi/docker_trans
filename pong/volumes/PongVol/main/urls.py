
from django.urls import path
from .views import LoginView, HomeView, Mainview, GameView, DataView, UsersSearch, SearchForUser

urlpatterns = [
    path('login/', LoginView,name='login'),
    path('home/', HomeView, name='home'),
    path('game/', GameView),
    path('main/data/', DataView),
    path('api/search/<str:search_string>', SearchForUser.as_view(), name='user_search'),
]
