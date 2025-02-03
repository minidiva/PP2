a = 33
b = 200
c = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")

if a > b and c > a:
  print("Both conditions are True")
if a > b or c > a:
  print("Both conditions are True")

if not a > b: print("a is not greater than b")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

if b > a:
  pass