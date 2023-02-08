from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers

app_name = 'recipes'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(
        'admin/',
         admin.site.urls),
    path(
        'recipes/api/v2/',
        views.RecipeAPIList.as_view(),
        name='recipes_api_v2',
    ),
    path(
        'recipes/api/v2/<int:pk>/',
        views.RecipeAPIDetail.as_view(),
        name='recipes_api_v2_detail',
    ),
    path(
        'recipes/api/v2/tag/<int:pk>/',
        views.tag_api_detail,
        name='recipes_api_v2_tag',
    ),
]
