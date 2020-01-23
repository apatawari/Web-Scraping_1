#To square a number using functions

def square(x):
 y = 0
 z = x
 for i in range(x):
  x = x + y
  y = z
 return x
def square2(x):
 y = 1
 for i in range(2):
  y = y * x
 return y


tosquare = int(input("Enter the value to be squared"))
result = square(tosquare)
result2 = square2(tosquare)
print(tosquare,"Squared using square",result)
print(tosquare,"Squared using square2", result2)
