#just demo code for checking

def poor():
  print("you are poor")

def middle_class():
  print("you are middle class")

def rich():
  print("you are rich")

def test(salary):
  if salary>=100000:
    rich()
  elif salary>=10000 and salary<=100000:
    middle_class()
  else:
    poor()

test(200000)
