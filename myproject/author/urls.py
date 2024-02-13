from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:author_id>/', views.all_articles, name='all_articles'),
    path('article/<int:article_id>/', views.article_page, name='article_page'),
    path('newauthor/', views.newauthor, name='newauthor'),
    path('newarticle/', views.newarticle, name='newarticle'),

]