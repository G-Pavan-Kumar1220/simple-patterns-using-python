# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

# square numbers
n=4
size = 2*n-1
for x in range(size):
  for y in range(size):
    m=min(x,y,(size-1-x),(size-1-y))
    print(n-m,end=" ")
  print()