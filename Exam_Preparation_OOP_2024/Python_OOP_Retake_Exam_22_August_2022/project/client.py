class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []
        self.bill: float = 0.0
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, value:str):
        if not all([value.startswith("0"), len(value) == 10, value.isnumeric()]):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value