from unittest import TestCase, main
from project.trip import Trip

class TestTrip(TestCase):

    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self):
        self.trip = Trip(100.0, 1, False)


    def test_correct_init(self):
        self.assertEqual(100.0, self.trip.budget)
        self.assertEqual(1, self.trip.travelers)
        self.assertFalse(self.trip.is_family)

    def test_travellers_value_less_than_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_set_correct_with_travellers_less_than_2_should_be_set_false(self):
        self.trip.travelers = 1
        self.assertFalse(self.trip.is_family)

    def test_is_family_set_at_false_if_travellers_more_or_equal_than_two_even_if_passed_value_is_true(self):
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)


    def test_book_a_trip_destination_not_in_destinations_returns_strin(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!', self.trip.book_a_trip("project"))

    def test_book_a_trip_with_correct_destination_not_enough_budget_returns_correct_string(self):
        self.trip.budget = 0
        self.assertEqual('Your budget is not enough!', self.trip.book_a_trip("New Zealand"))

    def test_book_a_trip_with_correct_destination_and_enough_budget_budget_reduced_by_required_price(self):
        destination = "New Zealand"
        self.trip.budget = 10000
        self.trip.book_a_trip(destination)
        expected_left_budget = 10000 - 7500

        self.assertEqual(expected_left_budget, self.trip.budget)

    def test_book_a_trip_with_correct_destination_returns_correct_string(self):
        destination = "New Zealand"
        self.trip.budget = 10000

        self.assertEqual('Successfully booked destination New Zealand! Your budget left is 2500.00', self.trip.book_a_trip(destination))

    def test_booking_status_for_nonexistant_destination_in_booked_destinations_paid_amounts(self):
        expected_message = "No bookings yet. Budget: 100.00"
        self.assertEqual(expected_message, self.trip.booking_status())

    def test_booking_status_with_existing_destination_in_booked_destinations_paid_amounts(self):
        destination = "Bulgaria"
        self.trip.budget = 10000
        self.trip.book_a_trip(destination)
        expected_message = """Booked Destination: Bulgaria
Paid Amount: 500.00\nNumber of Travelers: 1
Budget Left: 9500.00"""
        self.assertEqual(expected_message, self.trip.booking_status())








if __name__ == "__main__":
    main()
