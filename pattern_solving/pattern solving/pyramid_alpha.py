#pyramid with the alphabet
#       A 
#     A B A
#   A B C B A
# A B C D C B A

n=5
for x in range(n):
  for k in range(n-x-1):
    print(" ",end=" ")
  for y in range(x):
    print(chr(65+y),end=" ")
  for j in range(x-2,-1,-1):
    print(chr(65+j),end=" ")

  print()


 