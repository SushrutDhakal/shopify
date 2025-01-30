'''
Small spots = motorcycle and small cars
Medium = Medium cars + small cars
Large spots = Any vehicle + buses

If theres a spot avaliable for a vehicle they can enter parking lot (park)
Once vehicle leaves a parking lot it becomes empty

Have total for each spot + display total for each spot type

Charge fee on enter of each vehicle based on type
Display running parking lot total
'''

# type of car
# rate that it charges
# 


class Motorcycle():
    def __init__(self):
        self.type = "motorcycle"
        self.rate = 5

class SmallCar():
    def __init__(self):
        self.type = "small-car"
        self.rate = 10

class MediumCar():
    def __init__(self):
        self.type = "medium-car"
        self.rate = 10

class Bus():
    def __init__(self):
        self.type = "bus"
        self.rate = 20

class ParkingLot: 
    small_spot_count = 50
    medium_spots_count = 50
    large_spots_count = 50 

    small_spots = []
    medium_spots = []
    large_spots = []

    daily_total = 0

    def add_car(self, vehicle):
        if vehicle.type == "small-car" or vehicle.type == "motorcycle":
            if ParkingLot.small_spot_count > 0:
                ParkingLot.small_spots.append(vehicle)
                ParkingLot.small_spots_count -= 1
            elif ParkingLot.medium_spot_count > 0:
                ParkingLot.medium_spots.append(vehicle)
                ParkingLot.medium_spots_count -= 1
            elif ParkingLot.large_spots_count > 0:
                ParkingLot.large_spots.append(vehicle)
                ParkingLot.large_spots_count -= 1   
            else:
                print("Parking lot is full") 

        if vehicle.type == "medium-car":
            if ParkingLot.medium_spot_count > 0:
                ParkingLot.medium_spots.append(vehicle)
                ParkingLot.medium_spots_count -= 1
            elif ParkingLot.large_spots_count > 0:
                ParkingLot.large_spots.append(vehicle)
                ParkingLot.large_spots_count -= 1  
            else:
                print("Parking lot is full") 

        if vehicle.type == "bus":
            if ParkingLot.large_spots_count > 0:
                ParkingLot.large_spots.append(vehicle)
                ParkingLot.large_spots_count -= 1  
            else:
                print("Parking lot is full")   

        ParkingLot.daily_total += vehicle.rate
        return f"{vehicle.type} parked for {vehicle.rate}."

    def remove_car(self, vehicle):
        if vehicle.type == "small-car" or vehicle.type == "motorcycle":
            ParkingLot.small_spots.remove(vehicle)   
            ParkingLot.small_spots_count += 1
        if vehicle.type == "medium-car":
            ParkingLot.medium_spots.remove(vehicle)   
            ParkingLot.medium_spots_count += 1
        if vehicle.type == "bus":
            ParkingLot.large_spots.remove(vehicle)   
            ParkingLot.large_spots_count += 1
        return f"{vehicle.type} has left the parking lot."
    
    def display_avaliablity(self):
        return f"The parking lot has {ParkingLot.small_spot_count} small spots, {ParkingLot.medium_spots_count} medium spots, and {ParkingLot.large_spot_count} large spots"
    

        
            