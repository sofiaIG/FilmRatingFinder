import unittest
import main
from unittest.mock import Mock

mock = Mock()
mock.title = "something"
mock.date = 2010

class TestClass(unittest.TestCase):

    def test_input(self):
           parser = main.args_parser(mock.date, mock.title)
           self.assertTrue(main.args_parser(mock), list)

           #how to test if a int input is negative
           number = -5
           message = "this is negative"
           self.assertTrue(number>0, message)


         
        # self.assertEqual(input[0], str)
        #need to create a separate function that takes the values and make sure that the values are not negative.
    # def test_values(self):
    #     values = main.testing_something()

