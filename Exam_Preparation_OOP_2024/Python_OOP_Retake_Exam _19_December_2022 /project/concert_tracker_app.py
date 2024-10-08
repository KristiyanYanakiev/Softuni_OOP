from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    valid_musicians_type_mapper = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musicians_type_mapper:
            raise ValueError("Invalid musician type!")
        try:
            musician = [m for m in self.musicians if m.name == name][0]
            raise Exception(f"{name} is already a musician!")

        except IndexError:
            created_musicien = self.valid_musicians_type_mapper[musician_type](name, age)
            self.musicians.append(created_musicien)
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):

        try:
            band = [b for b in self.bands if b.name == name][0]
            raise Exception(f"{name} band is already created!")
        except IndexError:
            created_band = Band(name)
            self.bands.append(created_band)
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        except IndexError:
            created_concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(created_concert)
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

        band = [b for b in self.bands if b.name == band_name][0]

        singer_count = 0
        drummer_count = 0
        guitarist_count = 0

        for member in band.members:
            if isinstance(member, Singer):
                singer_count += 1
            elif isinstance(member, Drummer):
                drummer_count += 1
            elif isinstance(member, Guitarist):
                guitarist_count += 1

        if any([singer_count < 1, drummer_count < 1, guitarist_count < 1]):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]

        for member in band.members:
            if concert.genre == "Rock":
                if isinstance(member, Drummer):
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer):
                    if "sing high pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Guitarist):
                    if "play rock" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

            elif concert.genre == "Metal":
                if isinstance(member, Drummer):
                    if "play the drums with drumsticks" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer):
                    if "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Guitarist):
                    if "play metal" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

            elif concert.genre == "Jazz":
                if isinstance(member, Drummer):
                    if "play the drums with drum brushes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Singer):
                    if "sing high pitch notes" not in member.skills or "sing low pitch notes" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif isinstance(member, Guitarist):
                    if "play jazz" not in member.skills:
                        raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
