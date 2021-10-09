from rest_framework.response import Response
from rest_framework.views import APIView
from ticket_booking_app.models import Movie, ShowTime, BookSeats
from .serializers import MovieSerializer, ShowTimeSerializer, BookSeatsSerializer
from datetime import datetime
from rest_framework import status

#GET API for Listing All Movies currently playing in City

class MoviesListView(APIView):

    def get(self, request,city):
        movies_list = Movie.objects.filter(movies_in_city__city_name=city.capitalize())  # Filtering Movies List based on City Name
        if not movies_list:
            return Response({'status':"This City is not playing any movies"})
        else:
            serializer = MovieSerializer(movies_list,many=True)
            return Response(serializer.data)

#GET API for Listing All cinemas playing Specific Movie and their Show Timings

class MovieShowTimesView(APIView):

    def get(self, request,movie_title):
        movie_screening_list = ShowTime.objects.filter(movie_show_times__movie_title=movie_title)  # Filtering List of Show times(With Cinema) for Specific Movie
        if not movie_screening_list:
            return Response({'status':'This Movie is not Playing in any of the Cinemas'})
        else:
            serializer = ShowTimeSerializer(movie_screening_list,many=True)
            return Response(serializer.data)

class ShowTimeSeatsView(APIView):

    # GET Request for checking Availability of seats for each show time for specific Movie 
    def get(self, request, movie_title, show_time):
        formatted_show_time = datetime.strptime(show_time, '%H:%M:%S').time()       # Formatting Input String from URL to time object
        try:
            movie_title_object = Movie.objects.get(movie_title=movie_title)         # Fetching Movie Object by it's title
        except Movie.DoesNotExist:
            movie_title_object = None
        if movie_title_object is None:
            return Response({'status':'This Movie is not playing in any of the Cinemas'})
        else:
            try:
                # Passing Movie Object and Show Time to BookSeats Model for obtaining specific Show Time for that Movie
                movie_show_time_object = BookSeats.objects.get(book_seat__movie_show_times=movie_title_object,book_seat__show_time=formatted_show_time)
            except BookSeats.DoesNotExist:
                movie_show_time_object = None
            if movie_show_time_object is None:
                return Response({'status':'This Movie is not playing in this show time'})
            else:
                serializer = BookSeatsSerializer(movie_show_time_object)
                return Response(serializer.data)

    # API for Booking Seat for Movie in a specific show
    def put(self, request, movie_title, show_time):
        formatted_show_time = datetime.strptime(show_time, '%H:%M:%S').time()       # Formatting Input String from URL to time object
        try:
            movie_title_object = Movie.objects.get(movie_title=movie_title)         # Fetching Movie Object by it's title
        except Movie.DoesNotExist:
            movie_title_object = None
        if movie_title_object is None:
            return Response({'status':'This Movie is not playing in any of the Cinemas'})
        else:
            try:
                # Passing Movie Object and Show Time to BookSeats Model for obtaining specific Show Time for that Movie
                movie_show_time_object = BookSeats.objects.get(book_seat__movie_show_times=movie_title_object,book_seat__show_time=formatted_show_time)
            except BookSeats.DoesNotExist:
                movie_show_time_object = None
            if movie_show_time_object is None:
                return Response({'status':'This Movie is not playing in this show time'})
            else:
                if movie_show_time_object.booked_seats == movie_show_time_object.max_seats:   # Check for Availability of Seats
                    return Response({'booking_status':'Seats are not available for this Show'})
                else:
                    movie_show_time_object.booked_seats = movie_show_time_object.booked_seats + 1
                    movie_show_time_object.available_seats = movie_show_time_object.available_seats - 1
                    movie_show_time_object.save()
                    return Response({'booking_status':'Seat is booked for this show'},status=status.HTTP_202_ACCEPTED)