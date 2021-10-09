from rest_framework import serializers
from ticket_booking_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_title','movie_genre')