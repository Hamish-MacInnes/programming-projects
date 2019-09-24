x = 1
while x < 100:
  r = ''
  if (x % 3 == 0):
	 r = "fizz"
  if (x % 5 == 0):
	 r += "buzz"
  if r == '':
    r = x
  print r
  x += 1
