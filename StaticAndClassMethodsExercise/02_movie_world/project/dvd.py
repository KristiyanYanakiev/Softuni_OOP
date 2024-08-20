import calendar


class DVD:
    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split(".")
        year = int(year)
        month_as_str = calendar.month_name[int(month)]

        return cls(name, _id, year, month_as_str, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})"
                f" has age restriction {self.age_restriction}. "
                f"Status: {'rented' if self.is_rented else 'not rented'}")
