from django.contrib import admin
from ticket_booking_app.models import City, Cinema, Movie, ShowTime, BookSeats

#Registering Models to Admin

admin.site.register(City)
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(ShowTime)
admin.site.register(BookSeats)
