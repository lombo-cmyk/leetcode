from unittest import TestCase

from src.main import SolutionLongestPalindrome

from timed_test_case import TimedTestCase


class TestLongestPalindrome(TimedTestCase):

    def test_longest_palindrome_empty(self):
        text = ""
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         text)

    def test_longest_palindrome_one_letter(self):
        text = "a"
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         text)

    def test_longest_palindrome_two_different_letters(self):
        text = "ab"
        self.assertIn(SolutionLongestPalindrome.longest_palindrome(text),
                      ["a", "b"])

    def test_longest_palindrome_two_equal_letters(self):
        text = "aa"
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         text)

    def test_longest_palindrome_three_different_letters(self):
        text = "abc"
        self.assertIn(SolutionLongestPalindrome.longest_palindrome(text),
                      ["a", "b", "c"])

    def test_longest_palindrome_even(self):
        text = "dsrgbqwertyytrewqzbmkjuilj"
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         "qwertyytrewq")

    def test_longest_palindrome_odd(self):
        text = "piuuqwertytrewqfgj"
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         "qwertytrewq")

    def test_longest_palindrome_on_the_left(self):
        text = "asdfghjklkjhgfdsaqqweqweqweqrtyutiu"
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         "asdfghjklkjhgfdsa")

    def test_longest_palindrome_long(self):
        text = 3000 * "a"
        self.assertEqual(SolutionLongestPalindrome.longest_palindrome(text),
                         text)
