#same number triangle
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9


n=10
for x in range(1,n):
  for y in range(1,x):
    print(y,end=" ")
  print()


n=10
for x in range(n):
  for y in range(x):
    print(x,end=" ")
  print()