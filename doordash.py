class FoodApp:
    def __init__(self):
        self.restaurants = []
        self.orders = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def display_restaurants(self):
        for restaurant in self.restaurants:
            print(restaurant)

    def add_order(self, order):
        self.orders.append(order)


class Drivers:
    def __init__(self, name):
        self.name = name
        self.is_avaliable = True
        self.current_order = None

    def get_order(self, order):
        if self.is_avaliable and order.status == "Ready":
            self.is_avaliable = False
            self.current_order = order 
            order.update_status("Out for Delivery") 
            return f"Picked up an order for {order.name}"
        return f"{self.name} cannot pick up the order."

    def do_delivery(self):
        if self.current_order:
            self.current_order.update_status("Delivered")
            self.is_avaliable = True
            self.current_order = None
            return "Order Complete."
        return "No active orders to deliver."

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, food_name, cost):
        for food in self.menu:
            if food_name == food.name:
                return f"{food_name} is already in the menu."
        self.menu.append(Food(food_name, cost))
        return f"{food_name} added to {self.name}'s menu."

    def display_menu(self):
        for food in self.menu:
            print(f"{food.name} - {food.cost}")
    
    def __str__(self):
        return f"{self.name}"
    
    def update_status(new_status, order):
        order.status = new_status


class Food:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name 
    
class User:
    def __init__(self, name):
        self.name = name

    def browse_resturants(foodapp):
        foodapp.display_restaurants()

    def see_menu(restaurant):
        restaurant.display_menu()

    def make_order(self, restaurant, food_items):
        total_cost = 0
        valid_food = []
        for food in food_items:
            for item in restaurant.menu:
                if item.name == food:
                    total_cost += item.cost
                    valid_food.append(food)
                    break
                else: 
                    print(f"{food} not found at {restaurant.name}'s menu")

        Order(total_cost, self.name, valid_food, restaurant)

    def order_status(self, order):
        print(order.current_status())

class Order:
    def __init__(self, cost, user, food_items, restaurant):
        self.restaurant = restaurant
        self.user = user
        self.cost = cost
        self.food_items = food_items
        self.status = "Order Placed"

    def current_status(self):
        return f"The order status is: {self.status}."

                




    

        
    

