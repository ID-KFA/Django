from django.urls import path
from . import views

# urlpatterns = [
#  path("", views.IndexPageView.as_view(), name="index"),
# ]

urlpatterns = [
    path('coin/', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('rand_hundred/', views.rand_hundred, name='rand_hundred'),
    path('dice/<int:num>/', views.gen_dice, name='gen_dice'),
    path('coin/<int:num>/', views.gen_coin, name='gen_coin'),
    path('number/<int:num>/', views.gen_number, name='gen_number'),
    path('game/', views.game, name='game'),

]