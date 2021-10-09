from rest_framework.response import Response
from rest_framework.views import APIView
from ticket_booking_app.models import Movie, ShowTime, BookSeats
from .serializers import MovieSerializer, ShowTimeSerializer, BookSeatsSerializer
from datetime import datetime

#GET API for Listing All Movies currently playing in City

class MoviesListView(APIView):

    def get(self, request,city):
        movies_list = Movie.objects.filter(movies_in_city__city_name=city.capitalize())
        if not movies_list:
            return Response({'status':"This City is not playing any movies"})
        else:
            serializer = MovieSerializer(movies_list,many=True)
            return Response(serializer.data)

#GET API for Listing All cinemas playing Specific Movie and their Show Timings

class MovieShowTimesView(APIView):

    def get(self, request,movie_title):
        movie_screening_list = ShowTime.objects.filter(movie_show_times__movie_title=movie_title)
        if not movie_screening_list:
            return Response({'status':'This Movie is not Playing in any of the Cinemas'})
        else:
            serializer = ShowTimeSerializer(movie_screening_list,many=True)
            return Response(serializer.data)

class ShowTimeSeatsView(APIView):

    # GET Request for checking Availability of seats for each show time for specific Movie 
    def get(self, request, movie_title, show_time):
        formatted_show_time = datetime.strptime(show_time, '%H:%M:%S').time()
        try:
            movie_title_object = Movie.objects.get(movie_title=movie_title)
        except Movie.DoesNotExist:
            movie_title_object = None
        if movie_title_object is None:
            return Response({'status':'This Movie is not playing in any of the Cinemas'})
        else:
            try:
                movie_show_time_object = BookSeats.objects.get(book_seat__movie_show_times=movie_title_object,book_seat__show_time=formatted_show_time)
            except BookSeats.DoesNotExist:
                movie_show_time_object = None
            if movie_show_time_object is None:
                return Response({'status':'This Movie is not playing in this show time'})
            else:
                serializer = BookSeatsSerializer(movie_show_time_object)
                return Response(serializer.data)