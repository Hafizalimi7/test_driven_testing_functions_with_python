def password(lock):
  if lock == "777" and len(lock) == 3:
    return "Correct Key"
  else:
    return "Invalid Key..Try again"