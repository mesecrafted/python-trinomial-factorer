from fractions import gcd
from adder import find

def factorTrinomial():
  box = [0,0,0,0]
  dm = [0,0,0,0]
  par = [0,0,0,0]

  print("Ax^2+Bxy+Cy^2")
  try:
    A = int(input("A: "))
    B = int(input("B: "))
    C = int(input("C: "))
    R = int(input("range: "))
  except:
    print("you must have missed a number")
    exit()
  try:
    box[0] = A
    box[3] = C
    dm[0] = A*C
    dm[3] = B

    dm = find(R, dm)

    box[1] = dm[1]
    box[2] = dm[2]
  except:
    print("the numbers do not work")
    exit()

  print("\nbox:\n" + str(box[0]) + "\t|" + str(box[1]) + "\n---------\n" + str(box[2]) + "\t|" + str(box[3]) + "\n")
  print("diamond:\n\\" + str(dm[0]) + "/\n" + str(dm[1]) + "*" + str(dm[2]) + "\n/" + str(dm[3]) + "\\\n")
  try:
    par[0] = gcd(box[1],box[0])
    par[1] = gcd(box[3],box[2])
    par[2] = gcd(box[2],box[0])
    par[3] = gcd(box[3],box[1])
  except:
    print("gcd failed")
    exit()

  print( "\n(" + str(par[0]) + "x+" + str(par[1]) + "y)(" + str(par[2]) + "x+" + str(par[3]) + "y)")
