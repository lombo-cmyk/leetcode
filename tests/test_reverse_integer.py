from unittest import TestCase

from src.main import SolutionReverseInteger


class TestReverseInteger(TestCase):

    def test_reverse_zero(self):
        number_to_reverse = 0
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse), 0)

    def test_reverse_one_digit(self):
        number_to_reverse = 3
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse), 3)

    def test_reverse_happy_path(self):
        number_to_reverse = 123
        number_reversed = 321
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse),
                         number_reversed)

    def test_reverse_happy_path_negative(self):
        number_to_reverse = -123
        number_reversed = -321
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse),
                         number_reversed)

    def test_reverse_long_number(self):
        number_to_reverse = 123456789
        number_reversed = 987654321
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse),
                         number_reversed)

    def test_reverse_trailing_zero(self):
        number_to_reverse = 12345678900
        number_reversed = 987654321
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse),
                         number_reversed)

    def test_reverse_tricky_input(self):
        number_to_reverse = 1534236469
        expected = 0
        self.assertEqual(SolutionReverseInteger.reverse(number_to_reverse),
                         expected)


