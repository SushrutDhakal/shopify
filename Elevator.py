class Elevator:
    def __init__(self, max_capacity):
        self.current_floor = 1
        self.max_capacity = max_capacity
        self.current_people = 0
        self.is_avaliable = True

    def close_door(self):
        print("Door is closed")
        return 
    
    def open_door(self):
        print("Door is open")
        return

    def add_person(self, num_people, floor_num):
        if self.current_people + num_people <= self.max_capacity:
            if self.current_people + num_people == self.max_capacity:
                self.is_avaliable = False
            self.open_door()
            self.current_people += num_people 
            self.current_floor = floor_num
            self.close_door()
        else:
            return "Elevator is full."


class Building:
    def __init__(self, total_floors, total_elevators):
        self.total_floors = total_floors
        self.total_elevators = total_elevators
        self.elevators = [Elevator(10)] * self.total_elevators

    def call_elevator(self, floor_num, num_people):
        called_elevator = self.elevators[0]
        for elevator in self.elevators:
            if elevator.current_floor - floor_num < called_elevator.current_floor - floor_num and elevator.is_avaliable:
                called_elevator = elevator 
        called_elevator.add_person(num_people, floor_num)

 