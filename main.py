
from models import Car

dealership_cars = [
    Car("Audi", "A3 2.0 TDI", 150),
    Car("VW", "Golf", 105),
    Car("BMW", "320d", 190),
    Car("Ford", "Fiesta", 75)
]

print("All available cars in the dealership:")
for car in dealership_cars:
    print(car.get_full_name())

print("\nPowerful cars (150+ hp):")
for car in dealership_cars:
    if car.is_powerful():
        print(f"-> {car.get_full_name()} is a powerful choice!")