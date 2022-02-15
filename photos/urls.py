from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('', views.PhotoListView.as_view(), name='list'),
    path('<str:pk>', views.PhotoDetailView.as_view(), name='detail'),
    path('query/', views.PhotoQueryView.as_view(), name='query'),
    path('favorite/', views.FavoritesListView.as_view(), name='list-favorite'),
    path('favorite/add/', csrf_exempt(views.add_favorite_photo), name='add-favorite'),
]