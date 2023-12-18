def add_up(a,b):
  total = a + b
  return total

def times_up(a,b):
  total = a * b
  return total


def subtract(a,b):
  total = a - b
  return total


def division(a,b):
  if b == 0:
    raise ValueError("Can't divide this number")
  return a / b

