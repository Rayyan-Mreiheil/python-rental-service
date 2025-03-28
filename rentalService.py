
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

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price_per_day()}/day")



def show_vehicle_info(vehicle):
    vehicle.display_info()

# Create instances of Car and Bike
car1 = Car("Toyota","Corolla",2020,50,5)
bike1 = Bike("Yamaha","R1",2019,30,998)

car1.display_info()
bike1.display_info()

print()
print(f"Rental cost for {car1.brand} {car1.model} for 3 days: ${car1.calculate_rental_cost(3)}")
print(f"Rental cost for {bike1.brand} {bike1.model} for 5 days: ${bike1.calculate_rental_cost(5)}")

print()
car1.set_rental_price_per_day(55)
print(f"Updated rental price for {car1.brand} {car1.model}: ${car1.get_rental_price_per_day()}/day")

print()
show_vehicle_info(car1)
show_vehicle_info(bike1)