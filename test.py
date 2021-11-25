import unittest
import film_searching


class TestClass(unittest.TestCase):

       def test_rotten_tomatoes(self):
              self.assertEqual(film_searching.search_score_rotten("The French Dispatch" ,2021), 75)
              self.assertEqual(film_searching.search_score_rotten("Dune", 2021), 82)

       def test_imdb(self):
              self.assertEqual(film_searching.search_filmratings_imdb(2021, "Judas and the Black Messiah"), 7.5)
              self.assertEqual(film_searching.search_filmratings_imdb(1957, "12 Angry Men"), 9.0)
              self.assertEqual(film_searching.search_filmratings_imdb(1962, "To Kill a Mockingbird"), 8.3)

if __name__ == '__main__':
    unittest.main()





         


