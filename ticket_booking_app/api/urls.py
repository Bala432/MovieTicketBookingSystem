from django.urls import path
from .views import MoviesListView, MovieShowTimesView

urlpatterns = [
    path('city/<city>',MoviesListView.as_view()),
    path('city/movie/<movie_title>',MovieShowTimesView.as_view()),

]