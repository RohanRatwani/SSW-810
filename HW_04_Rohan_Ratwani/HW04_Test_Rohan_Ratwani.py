import random
import unittest
from typing import Iterator, List, Tuple
from HW04_Rohan_Ratwani import count_vowels,last_occurence,my_enumerate
#from HW04_First_Last import my_enumerate, my_enumerate_sarita, my_enumerate_yinghui, find_target, generator

# PART 1
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self) -> None:
        """ testing count vowels """
        self.assertEqual(count_vowels("My name is Rohan Ratwani"), 8)
        self.assertEqual(count_vowels(""), 0)
        self.assertNotEqual(count_vowels("name"), 1)

# PART 2
class FindLastTest(unittest.TestCase):
    def test_last_occurence(self) -> None:
        """ testing find_last """
        self.assertEqual(last_occurence(30,[40,30,30]),2)
        self.assertEqual(last_occurence(30, (40, 30, 30)), 2)


# PART 3
class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """
        self.assertEqual(list(my_enumerate("rohan")),list(enumerate("rohan")))
        self.assertEqual(list(my_enumerate("RatwanI")), list(enumerate("RatwanI")))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)