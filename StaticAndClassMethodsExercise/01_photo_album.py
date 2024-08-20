from math import ceil
from typing import List


class PhotoAlbum:

    MAX_NUM_OF_PHOTOS_PER_PAGE = 4
    PAGE_SEPARATOR = "-"
    PAGE_SEPARATOR_COUNT = 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str) -> str or None:
        for page in range(len(self.photos)): #rows of matrix
            if len(self.photos[page]) < self.MAX_NUM_OF_PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                free_page = page + 1
                free_slot = self.photos[page].index(label) + 1

                return f"{label} photo added successfully on page {free_page} slot {free_slot}"

        return "No more free slots"

    def display(self):
        page_separation = self.PAGE_SEPARATOR * self.PAGE_SEPARATOR_COUNT
        result = f"{page_separation}\n"

        for row in self.photos:
            if len(row) > 0:
                result += f"{'[] ' * len(row)}\n".rstrip()
            result += f"\n{page_separation}\n"

        return result[:-1]


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())






