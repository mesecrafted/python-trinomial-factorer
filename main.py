from ft import factorTrinomial
from guessCheckAdder import find

while True:
  check = True
  while check:
    try:
      print("\npolynomial toolkit:\n 1: factor a trinomial\n 2: fill in a diamond\n")
      run = int(input("type a number: "))
    except:
      print("you typed the wrong number")
      exit()
    if run in [1,2]:
      check = False
    else:
      print("you typed the wrong number")

  if run == 1:
    factorTrinomial()
  if run == 2:
    diamond = [0,0,0,0]
    try:
      diamond[0] = int(input("\ntop of diamond: "))
      diamond[3] = int(input("bottom of diamond: "))
      diamond = find(100, diamond)
    except:
      print("you must have entered something wrong")
      exit()
    print("\n" + str(diamond[1]) + " and " + str(diamond[2]))
