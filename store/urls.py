from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("<int:game_id>/", views.game_detail, name="game_detail"),
    path("profile/", views.user_profile, name="user_profile"),
    path("change_mail/", views.change_mail, name="change_mail"),
    path("<int:game_id>/buy/", views.buy_game, name="buy_game"),
]
