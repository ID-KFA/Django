from django.urls import path, include
from .views import recipe_list, recipe_detail, edit_recipe, add_recipe, \
    user_login, user_logout, registration, user_page

urlpatterns = [
    path('list/', recipe_list, name='recipe_list'),
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('edit/<int:recipe_id>', edit_recipe, name='edit_recipe'),
    path('add/', add_recipe, name='add_recipe'),
    path('', include('django.contrib.auth.urls')),
    # path('', user_page, name='user_page'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

