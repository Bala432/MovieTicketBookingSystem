# MovieTicketBookingSystem
This Project consists of API's for working with Movie Tickets Booking System and developed in Django Rest Framework

This Project Contains following API's.

1.) GET API ---  '/api/city/<city_name>'
   ----> This API call will fetch all the movies that are currently playing in the city( Here i used only one city -- Hyderabad). so call will be '/api/city/Hyderabad'
   
 2.) GET API --- '/api/city/movie/<movie_name>'
   ----> This API call will List all cinemas with Show Timings for a Specific mentioned movie . so call will be '/api/city/movie/Avengers'
   
 3.) 
  a.) API --- '/api/city/<movie_name>/<show_time>'
    ----> GET API call will check for Availability of seats for mentioned show time . so call will be like '/api/city/movie/Avengers/13:30:00'
    
  b.) PUT API call will book a seat for mentioned show time and will update booked_seats and available_seats for that show.(Just need to click on PUT Request without any need to pass data )
    
 
