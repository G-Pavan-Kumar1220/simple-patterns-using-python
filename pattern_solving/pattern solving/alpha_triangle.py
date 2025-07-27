#printing the alphabet triangel

# A 
# A B
# A B C
# A B C D
# A B C D E
# A B C D
# A B C
# A B
# A

n=5
for x in range(n):
  n=65
  for y in range(x):
    print(chr(n),end=" ")
    n+=1
  print()


  #reverse
  m=5
for x in range(m):
  n=65
  for y in range(m-x):
    print(chr(n),end=" ")
    n+=1
  print()
