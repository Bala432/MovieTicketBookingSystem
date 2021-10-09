from rest_framework.response import Response
from rest_framework.views import APIView
from ticket_booking_app.models import Movie
from .serializers import MovieSerializer

class MoviesListView(APIView):

    def get(self, request,city):
        movies_list = Movie.objects.filter(movies_in_city__city_name=city.capitalize())
        if not movies_list:
            return Response({'status':"No Movies are currently playing in this city"})
        else:
            serializer = MovieSerializer(movies_list,many=True)
            return Response(serializer.data)