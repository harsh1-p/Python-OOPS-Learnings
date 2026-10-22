'''Create a class Movie with the following:

Attributes:
movie name -> name of the movie
total seats -> total seats available in the theatre
ticket price -> price per ticket
booked seats -> starts at 0
Methods:
book_ticket(num_tickets) books the given number of tickets. If enough seats are available,

confirm the booking and show the total amount to pay. If not,

show "Sorry, not enough seats available"
show_status() displays movie name, seats available, and seats booked so far'''

class Movie:

    def __init__(self, movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = 100
        self.booked_seats = 0

    def book_ticket(self, num_tickets):
        available_seats = self.total_seats - self.booked_seats

        if num_tickets <= available_seats:
            self.booked_seats += num_tickets
            total_amount = num_tickets * self.ticket_price

            print("Booking confirmed!")
            print("Total amount to pay:", total_amount)
        else:
            print("Sorry, not enough seats available")

    def show_status(self):
        available_seats = self.total_seats - self.booked_seats

        print("Movie Name:", self.movie_name)
        print("Seats Available:", available_seats)
        print("Seats Booked:", self.booked_seats)


obj1 = Movie("SpiderMan", 100)

obj1.book_ticket(50)
obj1.show_status()

        