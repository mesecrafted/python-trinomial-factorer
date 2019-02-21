def find(R, block):
  for i in range(-R,R):
    for j in range(-R,R):
      if (i*j == block[0]) and (i+j == block[3]):
        block[1] = i
        block[2] = j
        return block
