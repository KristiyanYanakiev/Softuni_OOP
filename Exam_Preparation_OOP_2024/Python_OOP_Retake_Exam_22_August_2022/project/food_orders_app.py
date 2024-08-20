from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []

    def register_client(self, client_phone_number: str):

        try:
            next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for m in meals:
            if isinstance(m, Meal):
                self.menu.append(m)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []

        for m in self.menu:
            result.append(m.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        for meal_name in meal_names_and_quantities:
            if meal_name not in [m.name for m in self.menu]:
                raise Exception("{meal_name} is not on the menu!")

        for meal_name in meal_names_and_quantities:
            meal = next(filter(lambda m: m.name == meal_name, self.menu))
            if meal_names_and_quantities[meal_name] > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name}: {meal_name}!")

        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)

        for meal_name in meal_names_and_quantities:
            meal = next(filter(lambda m: m.name == meal_name, self.menu))
            client.shopping_cart.append(meal)
            client.bill += meal_names_and_quantities[meal_name] * meal.price
            meal.quantity -= meal_names_and_quantities[meal_name]

        return (f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} "
                f"for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for m_in_client_list in client.shopping_cart:
            m_in_menu = next(filter(lambda m: m.name == m_in_client_list.name, self.menu))
            m_in_menu.quantity = m_in_client_list.quantity

        client.shopping_cart = []
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        current_receipt_id = 0

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0

        return (f"Receipt #{current_receipt_id + 1} with total amount of {total_paid_money:.2f} "
                f"was successfully paid for {client_phone_number}.")


    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


