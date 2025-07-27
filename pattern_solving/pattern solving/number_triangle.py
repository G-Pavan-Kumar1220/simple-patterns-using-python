# nummber triangle
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

temp=1
for x in range(5):
  for j in range(x):
    print(temp,end=" ")
    temp+=1
  print()