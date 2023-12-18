import unittest

from Examples.passcode import password


class Test_passcode(unittest.TestCase):
  def test_password(self):
    self.assertEqual(password("777"), "Correct Key")
    self.assertEqual(password("101"), "Invalid Key..Try again")
    self.assertEqual(password("13"), "Invalid Key..Try again")
    self.assertEqual(password("7777"), "Invalid Key..Try again")





if __name__== '__main__':
  unittest.main()