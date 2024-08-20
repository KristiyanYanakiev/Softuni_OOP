from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer("Test_name", 20, 100)

    def test_correct_init(self):
        self.assertEqual("Test_name", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "a"

        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_name_setter_raises_value_error_when_name_has_two_chars(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "ab"

        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_age_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_new_win_with_correct_tournament_name_expect_success(self):
        self.player.add_new_win("Test_tournament")
        self.assertEqual(["Test_tournament"], self.player.wins)

    def test_add_new_win_with_existing_tournament_in_wins_list_returns_correct_message(self):
        self.player.add_new_win("Test_tournament")
        result = self.player.add_new_win("Test_tournament")
        self.assertEqual("Test_tournament has been already added to the list of wins!", result)

    def test_larger_than_method_with_other_player_has_more_points_returns_correct_message(self):
        other = TennisPlayer("second_name", 30, 150)
        result = self.player.__lt__(other)
        expected = 'second_name is a top seeded player and he/she is better than Test_name'

        self.assertEqual(expected, result)

    def test_larger_than_method_with_first_player_has_more_points_returns_correct_message(self):
        other = TennisPlayer("second_name", 30, 90)
        result = self.player.__lt__(other)
        expected = 'Test_name is a better player than second_name'

        self.assertEqual(expected, result)

    def test_str_method_returns_correct_message(self):
        self.player.add_new_win("first")
        self.player.add_new_win("second")
        self.player.add_new_win("third")

        expected = f"Tennis Player: Test_name\n" \
                   f"Age: 20\n" \
                   f"Points: 100.0\n" \
                   f"Tournaments won: first, second, third"

        result = str(self.player)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
