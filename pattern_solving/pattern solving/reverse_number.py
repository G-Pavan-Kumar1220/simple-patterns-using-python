# reverse number triangle

# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n=10
for x in range(1,n):
  for y in range(1,n-x):
    print(y,end=" ")
  print()