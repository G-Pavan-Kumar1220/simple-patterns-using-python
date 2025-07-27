# F 
# E F 
# D E F
# C D E F
# B C D E F
# A B C D E F

# reverse letter triangle with letters
n=5
for x in range(n+1):
  for y in range(x,-1,-1):
    print(chr(65+n-y),end=" ")
  print()
