from rest_framework.response import Response
from rest_framework.views import APIView
from ticket_booking_app.models import Movie, ShowTime
from .serializers import MovieSerializer, ShowTimeSerializer

class MoviesListView(APIView):

    def get(self, request,city):
        movies_list = Movie.objects.filter(movies_in_city__city_name=city.capitalize())
        if not movies_list:
            return Response({'status':"This City is not playing any movies"})
        else:
            serializer = MovieSerializer(movies_list,many=True)
            return Response(serializer.data)

class MovieShowTimesView(APIView):

    def get(self, request,movie_title):
        movie_title = ShowTime.objects.filter(movie_show_times__movie_title=movie_title)
        if not movie_title:
            return Response({'status':'This Movie is not Playing in any of the Cinemas'})
        else:
            serializer = ShowTimeSerializer(movie_title,many=True)
            return Response(serializer.data)