
class Vehicle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day # Private Attribute (Using double _)

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return days * self.get_rental_price_per_day()

    # Setter for rental_price_per_day
    def set_rental_price_per_day(self, new_price):
        if isinstance(new_price, (int,float)) and new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Invalid rental price! It must be a positive number.")

    # Getter for rental_price_per_day
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day


# Class Car Inherits from Class Vehicle
class Car(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,seating_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price_per_day()}/day")


# Class Car Inherits from Class Vehicle
class Bike(Vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine_capacity = engine_capacity