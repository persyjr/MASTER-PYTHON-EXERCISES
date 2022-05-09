#Complete the function to return the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.
import math
dias=0
def car_route(n,m):
  dias=math.ceil(m/n)
 
  return dias


#Invoke the function with two intergers.
print(car_route(659,1857))