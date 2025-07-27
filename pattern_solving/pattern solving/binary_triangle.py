# 1 
# 0 1
# 1 0 1
# 0 1 0 1

# printing the binary triangle

n=5
for x in range(n):
  for y in range(x):
    print((x+y)%2,end=" ")
  print() 
         
