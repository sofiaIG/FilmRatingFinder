import unittest
import main
from unittest.mock import Mock

mock = Mock()
mock.title = "something"
mock.date = 2010

class TestClass(unittest.TestCase):

       def test_input(self):
              parser = main.args_parser(mock.date, mock.title)#how do I test each argument separately?
              self.assertTrue(main.args_parser(mock), list)
              self.assertTrue(len(mock.title)> 250, "title too long")

              #Testing if date is negative
              number = -5
              message = "this is negative"
              self.assertTrue(mock.date>0, message)

       # self.assertEqual(input[0], str)
       # need to create a separate function that takes the values and make sure that the values are not negative.
       # def test_values(self):
       #     values = main.testing_something()


       def test_api(self):
              rotten_tom_test = main.search_score_rotten("potato", 2010)
              self.assertTrue(rotten_tom_test, type(None))



         


