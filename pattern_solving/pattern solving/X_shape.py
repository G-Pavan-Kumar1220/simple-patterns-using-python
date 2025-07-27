# #printing the x shape 

# *          *
# **        **
# ***      ***
# ****    ****
# *****  *****
# ****    ****
# ***      ***
# **        **
# *          *


n=5
for x in range(n):#primary loop
  print("*"*(x)," "*((n-x)*2),"*"*x)
for y in range(n): #secondary loop
   print("*"*(n-y)," "*((y)*2),"*"*(n-y))