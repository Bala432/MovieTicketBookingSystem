from django.urls import path
from .views import MoviesListView

urlpatterns = [
    path('city/<city>',MoviesListView.as_view()),
]