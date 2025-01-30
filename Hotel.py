class HotelRoom:
    def __init__(self, number, room_type, price, capacity):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.capacity = capacity
        self._guest_name = None  # Encapsulation
        self._is_available = True
        self.num_nights = 0

    def is_available(self):
        return self._is_available

    def book(self, name, nights, guests):
        if not self._is_available:
            return f"Room {self.number} is already booked."
        
        if guests > self.capacity:
            return f"Booking failed: {self.room_type} rooms allow only {self.capacity} guests."
        
        self._guest_name = name
        self.num_nights = nights
        self._is_available = False
        return f"{name} booked {self.room_type} Room {self.number} for {nights} nights."

    def leave(self):
        if self._is_available:
            return f"Room {self.number} is already available."
        
        guest = self._guest_name
        self._guest_name = None
        self.num_nights = 0
        self._is_available = True
        return f"{guest} has checked out of Room {self.number}."

class Hotel:
    def __init__(self, total_singles, total_doubles, total_suites):
        self.rooms = []
        self.revenue = 0
        for i in range(total_singles):
            self.rooms.append(HotelRoom(i + 100, "Single", 100, 1))
        for i in range(total_doubles):
            self.rooms.append(HotelRoom(i + 200, "Double", 150, 2))
        for i in range(total_suites):
            self.rooms.append(HotelRoom(i + 300, "Suite", 300, 4))

    def book_room(self, name, room_type, nights, guests=1):
        for room in self.rooms:
            if room.is_available() and room.room_type == room_type:
                print(room.book(name, nights, guests))
                self.revenue += room.price * nights
                return
        print(f"No available {room_type} rooms for {name}.")

    def checkout(self, name):
        for room in self.rooms:
            if room._guest_name == name and not room.is_available():
                print(room.leave())
                return
        print(f"No booking found for {name}.")

    def total_rooms_available(self, room_type):
        return sum(1 for room in self.rooms if room.room_type == room_type and room.is_available())

    def get_summary(self):
        print("Available Rooms:")
        print(f"  Single: {self.total_rooms_available('Single')}")
        print(f"  Double: {self.total_rooms_available('Double')}")
        print(f"  Suite: {self.total_rooms_available('Suite')}")
        print(f"Total Revenue: ${self.revenue}")