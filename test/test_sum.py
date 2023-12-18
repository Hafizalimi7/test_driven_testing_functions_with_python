import unittest

from Examples.sum import add_up, times_up, subtract, division

class TestAdd(unittest.TestCase):
    def test_add(self):
        """ Test add numbers together """
        self.assertEqual(add_up(5, 10), 15)
        self.assertEqual(add_up(2, 7), 9)
        self.assertEqual(add_up(-11, 6), -5)
        self.assertEqual(add_up(-3, 2), -1)

    """ Test multiplys numbers together """
    def test_multication(self):
        self.assertEqual(times_up(10, 50), 500)
        self.assertEqual(times_up(1, 5), 5)
        self.assertEqual(times_up(-11, -5),55 )
        self.assertEqual(times_up(0, 0),0)

    """ Test subracts numbers together """
    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 6), -1)
        self.assertEqual(subtract(-16, -1), -15)
        self.assertEqual(subtract(0, 5), -5)

    """ Test divides numbers together """
    def test_division(self):
        self.assertEqual(division(5, 2), 2.5)
        self.assertEqual(division(20, 4), 5)
        self.assertEqual(division(20, -4), -5)

        with self.assertRaises(ValueError):
             division(10,0)
        

if __name__ == '__main__':
    unittest.main()