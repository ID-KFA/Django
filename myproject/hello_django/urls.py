from django.urls import path
from . import views

urlpatterns = [
 path("", views.IndexPageView.as_view(), name="index"),
 # path('', views.index, name='index'),

 # path('about/', views.about, name='about'),
]