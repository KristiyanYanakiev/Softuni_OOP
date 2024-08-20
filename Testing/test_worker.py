from unittest import TestCase, main
#from first_test_worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker(
            "Gosho",
            1000,
            100
        )

    def test_correct_init(self):
        self.assertEqual("Gosho", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method_with_energy_less_or_equal_than_zero_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_enough_energy_raises_money_by_salary_and_decreases_energy_by_one(self):

        expected_money = self.worker.money + self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_increases_energy_by_one(self):
        expected_energy = self.worker.energy + 1  # arrange

        self.worker.rest()  # act

        self.assertEqual(expected_energy, self.worker.energy) #  assert

    def test_get_info_method_returns_expected_string(self):
        expected_string = 'Gosho has saved 0 money.'

        self.assertEqual(expected_string, self.worker.get_info())


if __name__ == "__main__":
    main()
