from typing import List
from project.room import Room


class Hotel:

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)


    def take_room(self, room_number: int, people: int) -> None or str:
        r = [r for r in self.rooms if r.number == room_number][0]
        result = r.take_room(people)
        if result is None:
            self.guests += people



    def free_room(self, room_number: int) -> None or str:
        r = [r for r in self.rooms if r.number == room_number][0]
        people = r.guests
        result = r.free_room()
        if result is None:
            self.guests -= people


    def status(self) -> str:
        res = (f"Hotel {self.name} has {self.guests} total guests\n"
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}\n")

        return res



