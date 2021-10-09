from rest_framework import serializers
from ticket_booking_app.models import Movie, ShowTime, BookSeats

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_title','movie_genre')

class ShowTimeSerializer(serializers.ModelSerializer):
    cinema_name = serializers.CharField(source='cinema_show_times.cinema_name')
    class Meta:
        model = ShowTime
        fields = ('cinema_name','show_time')

class BookSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSeats
        fields = ['max_seats','booked_seats','available_seats']