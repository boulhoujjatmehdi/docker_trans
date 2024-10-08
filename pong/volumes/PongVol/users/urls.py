from django.urls import path
from .views import RegisterView , LoginView, UserView, LogoutView, csrf_token_view, enable_otp, confirm_otp, change_pass, profile_img
from .oauth import oauth42
from .friends import send_friendship_request, accept_friendship_request, SearchForUser, RequestsOnWait
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()), 
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('csrf-token/', csrf_token_view, name='csrf-token'),
    path("42/callback/", oauth42.as_view()),
    path("otp/qrcode/", enable_otp),
    path("otp/confirm", confirm_otp),
    path("change-pass/", change_pass),
    path('profile-img/', profile_img),
    path('relations/send-friendship/<str:target_id>', send_friendship_request),
    path('relations/accept-friendship/<str:target_id>', accept_friendship_request),
    path('search/<str:search_string>', SearchForUser.as_view(), name='user_search'),
    path('get-requests/', RequestsOnWait.as_view(), name="requests"),

    # friendships

]
