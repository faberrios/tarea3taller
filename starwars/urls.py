from django.urls import path
from . import views


urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('movie/<movieId>', views.movie_info, name='movie_info'),
    path('character/<characterId>', views.character_info, name='character_info'),
    path('planet/<planetId>', views.planet_info, name='planet_info'),
    path('ship/<shipId>', views.ship_info, name='ship_info')
]