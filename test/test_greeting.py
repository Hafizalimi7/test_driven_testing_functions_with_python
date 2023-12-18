import unittest

from Examples.Greet import greetings


class Test_Greet(unittest.TestCase):
  def testing_greet(self):
    self.assertEqual(greetings("Hafiz"),"Hello Hafiz")


if __name__ == '__main__':
    unittest.main()
