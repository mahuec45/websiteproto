try:
  test = input("what is your name? ").lower()
  if test == "josh":
    print("No it's not you cornball")
  else:
    print(f"hi {test}")
except ValueError:
    print("Please enter a valid name")