from enum import Enum

class Gender(Enum): #An enum class that represents the gender options for a Human object.
    FEMALE = "FEMALE"
    MALE = "MALE"

class Type(Enum):  #An enum class that represents the different types of classes in a flight.
    FIRST_CLASS = "First Class"
    BUSINESS_CLASS = "Business Class"
    ECONOMY_CLASS = "Economy Class"

class Human:
    """Class representing human."""
    def __init__(self, name, age, gender, nationality, contact_number, email):
        # Constructor for the Human class, initializes a Human object with the provided parameters
        self._name = name # Initialization of human attributes.
        self._age = age
        self._gender = Gender(gender)
        self._nationality = nationality
        self._contact_number = contact_number
        self._email = email

    # Protected getter and setter methods for the attributes, help in to  access and modify the attributes safely.
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = Gender(gender)

    def get_nationality(self):
        return self._nationality

    def set_nationality(self, nationality):
        self._nationality = nationality

    def get_contact_number(self):
        return self._contact_number

    def set_contact_number(self, contact_number):
        self._contact_number = contact_number

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

class Passenger(Human):
    """ Class representing a passenger, inheriting attributes and methods from Human"""
    def __init__(self, name, age, gender, nationality, contact_number, email, ticket_id):
        # Class representing a passenger, inheriting attributes and methods from Human
        super().__init__(name, age, gender, nationality, contact_number, email)
        # Calls the constructor of the Human class to initialize inherited attributes.
        self.__ticket_id = ticket_id # Passenger's ticket ID, private attribute

    #getter method for the ticket_id attribute
    def get_ticket_id(self):
        return self.__ticket_id

    # Private setter method for the ticket_id attribute
    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

class Flight:
    """class representing Flight"""
    def __init__(self, airline, flight_number, date, departure_time, arrival_time, departure_city, arrival_city):
        # Constructor for the Flight class, initializes a Flight object with the provided parameters
        self.__airline = airline
        self.__flight_number = flight_number
        self.__date = date    # Initialization of flight attributes all private
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__departure_city = departure_city
        self.__arrival_city = arrival_city

    # Getter and setter methods for Flight attributes.
    def get_airline(self):
        return self.__airline

    def set_airline(self, airline):
        self.__airline = airline

    def get_flight_number(self):
        return self.__flight_number

    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def get_date(self):
        return self.__date

    def __set_date(self, date):
        self.__date = date

    def get_departure_time(self):
        return self.__departure_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def get_departure_city(self):
        return self.__departure_city

    def set_departure_city(self, departure_city):
        self.__departure_city = departure_city

    def get_arrival_city(self):
        return self.__arrival_city

    def set_arrival_city(self, arrival_city):
        self.__arrival_city = arrival_city

    def calculate_flight_duration(self):
        """Calculate the flight duration.
        Given the departure and arrival times this function should calculate
        the total flight duration, considering time zones if necessary."""
        pass

class Airport:
    """ class representing Airport"""
    def __init__(self, departure_airport_code, arrival_airport_code, departure_terminal, arrival_terminal, departure_gate, arrival_gate):
        # Constructor for the Airport class, initializes a Airport object with the provided parameters
        self.__departure_airport_code = departure_airport_code
        self.__arrival_airport_code = arrival_airport_code    # Initialization of Airport attributes all private
        self.__departure_terminal = departure_terminal
        self.__arrival_terminal = arrival_terminal
        self.__departure_gate = departure_gate
        self.__arrival_gate = arrival_gate
# Getter and setter methods for Airport attributes.
    def get_departure_airport_code(self):
        return self.__departure_airport_code

    def set_departure_airport_code(self, departure_airport_code):
        self.__departure_airport_code = departure_airport_code

    def get_arrival_airport_code(self):
        return self.__arrival_airport_code

    def set_arrival_airport_code(self, arrival_airport_code):
        self.__arrival_airport_code = arrival_airport_code

    def get_departure_terminal(self):
        return self.__departure_terminal

    def set_departure_terminal(self, departure_terminal):
        self.__departure_terminal = departure_terminal

    def get_arrival_terminal(self):
        return self.__arrival_terminal

    def set_arrival_terminal(self, arrival_terminal):
        self.__arrival_terminal = arrival_terminal

    def get_departure_gate(self):
        return self.__departure_gate

    def set_departure_gate(self, departure_gate):
        self.__departure_gate = departure_gate

    def get_arrival_gate(self):
        return self.__arrival_gate

    def set_arrival_gate(self, arrival_gate):
        self.__arrival_gate = arrival_gate

class Baggage:
    """ class representing Baggage"""
    def __init__(self, baggage_id, weight, passenger_id, flight_number, destination_code,  baggage_type, fragile, claimed):
        # Constructor for the Baggage class, initializes a Baggage object with the provided parameters
        self.__baggage_id = baggage_id
        self.__weight = weight
        self.__passenger_id = passenger_id
        self.__flight_number = flight_number    # Initialization of baggage attributes all private
        self.__destination_code = destination_code
        self.__baggage_type = baggage_type
        self.__fragile = fragile
        self.__claimed = claimed

    # Getter and setter methods for baggage attributes, provide controlled access and the ability to modify baggage details
    def getBaggageID(self):
        return self.__baggage_id

    def setBaggageID(self, baggage_id):
        self.__baggage_id = baggage_id

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        self.__weight = weight

    def getPassengerID(self):
        return self.__passenger_id

    def setPassengerID(self, passenger_id):
        self.__passenger_id = passenger_id

    def getFlightNumber(self):
        return self.__flight_number

    def setFlightNumber(self, flight_number):
        self.__flight_number = flight_number

    def getDestinationCode(self):
        return self.__destination_code

    def setDestinationCode(self, destination_code):
        self.__destination_code = destination_code


    def getBaggageType(self):
        return self.__baggage_type

    def setBaggageType(self, baggage_type):
        self.__baggage_type = baggage_type

    def isFragile(self):
        return self.__fragile

    def setFragile(self, fragile):
        self.__fragile = fragile

    def isClaimed(self):
        return self.__claimed

    def __setClaimed(self, claimed):
        self.__claimed = claimed

class Seat:
    """class representing Seat"""
    def __init__(self, seat_number, TYPE, seat_type, is_available):
        # Constructor for the Seat class, initializes a Seat object with the provided parameters
        self.__seat_number = seat_number
        self.__TYPE = Type(TYPE)     # Initialization of seat attributes all private
        self.__seat_type = seat_type
        self.__is_available = is_available

    # Getter and setter methods for seat attributes.
    def get_seat_number(self):
        return self.__seat_number

    def set_seat_number(self, seat_number):
        self.__seat_number = seat_number

    def get_TYPE(self):
        return self.__TYPE

    def set_TYPE(self,TYPE):
        self.__TYPE = Type(TYPE)

    def get_seat_type(self):
        return self.__seat_type

    def set_seat_type(self, seat_type):
        self.__seat_type = seat_type

    def get_is_available(self):
        return self.__is_available

    def __set_is_available(self, is_available):
        self.__is_available = is_available

    def upgarde_seat(self):
        """"
        upgrade the seat to a new type
        This method should check the current seat type and, based on some conditions
        (e.g., availability, seat type restrictions), perform the upgrade, adjusting
        the seat's attributes accordingly.
        """
        pass
# The display_itinerary function takes five arguments (passenger, flight, airport, seat, and baggage), which are objects representing different aspects of a passenger's itinerary. The function then retrieves specific information from these objects and prints it in a formatted way.
def display_itinerary(passenger, flight, airport, seat, baggage):
    #The `get` methods retrieve information from objects, and the `print` function displays that information in a goo way.
    print(f"Passenger Name: {passenger.get_name()}, "f"Ticket ID: {passenger.get_ticket_id()}, "f"Age: {passenger.get_age()}, "f"Gender: {passenger.get_gender().name}, "f"Nationality: {passenger.get_nationality()}, " f"Contact Number: {passenger.get_contact_number()}, "f"Email: {passenger.get_email()}")
    print(f"Flight: {flight.get_airline()} {flight.get_flight_number()}, "f"from {flight.get_departure_city()} to {flight.get_arrival_city()}")
    print(f"Date: {flight.get_date()}, "f"Departure: {flight.get_departure_time()}, "f"Arrival: {flight.get_arrival_time()}")
    print(f"Seat: {seat.get_seat_number()}, Type class: {seat.get_TYPE().value}, Lane: {seat.get_seat_type()}, "f"Available: {seat.get_is_available()}")
    print(f"Departure Terminal: {airport.get_departure_terminal()}, "f"Gate: {airport.get_departure_gate()}")
    print(f"Arrival Terminal: {airport.get_arrival_terminal()}, "f"Gate: {airport.get_arrival_gate()}")
    print(f"Baggage ID: {baggage.getBaggageID()}, Weight: {baggage.getWeight()}kg, "f"Fragile: {'Yes' if baggage.isFragile() else 'No'}, " f"Claimed: {'Yes' if baggage.isClaimed() else 'No'}")
#creating objects, these examples are all from the ticket pick in the assignment provided.
passenger1 = Passenger("James Smith", 30, "MALE", "American", "00123456789", "j.smith@example.com", "5A6BCD78")
flight1 = Flight("National Airlines", "NA4321", "06 Dec 20", "11:40", "13:30", "Chicago ORD", "New York JFK")
airport1 = Airport("ORD", "JFK", "1", "2", "03", "B10")
seat1 = Seat("09A", "First Class", "WINDOW", True)
baggage1 = Baggage("CB12345", 23.5, "5A6BCD78", "NA4321", "JFK", "Carry on", False,  True)
display_itinerary(passenger1, flight1, airport1, seat1, baggage1) #The display_itinerary function is called with the passenger1, flight1, airport1, seat1, and baggage1 objects as arguments.
# This will print out the itinerary details for the provided passenger's itinerary, using the information stored in those objects.





