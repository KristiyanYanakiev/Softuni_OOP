class Room:

    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests: int = 0
        self.is_taken: bool = False

    def take_room(self, people: int) -> str or None:
        if self.capacity < people or self.is_taken:
            return f"Room number {self.number} cannot be taken"
        self.guests += people
        self.is_taken = True

    def free_room(self) -> None or str:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0

