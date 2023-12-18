import unittest

from my_add.addition import add_up

class TestAdd(unittest.TestCase):
    def test_add(self):
        """ Test add numbers together """
        self.assertEqual(add_up(5), 10)
        self.assertEqual(add_up(2), 7)
        self.assertEqual(add_up(-11), -6)
        self.assertEqual(add_up(-3), 2)

if __name__ == '__main__':
    unittest.main()