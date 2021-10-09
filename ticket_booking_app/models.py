from django.db import models

# Defining Models for Ticket Booking System

class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name

class Cinema(models.Model):
    cinema_name = models.CharField(max_length=50)
    cinema_location = models.CharField(max_length=50)
    located_city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.cinema_name

class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    movie_genre = models.CharField(max_length=20)
    movies_in_city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='city_movies_list')

    def __str__(self):
        return self.movie_title

class ShowTime(models.Model):
    show_time = models.TimeField()
    cinema_show_times = models.ForeignKey(Cinema,on_delete=models.CASCADE,related_name='show_timings')
    movie_show_times = models.ForeignKey(Movie,on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.show_time)

class BookSeats(models.Model):
    book_seat = models.OneToOneField(ShowTime,on_delete=models.CASCADE)
    max_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return str(self.book_seat)