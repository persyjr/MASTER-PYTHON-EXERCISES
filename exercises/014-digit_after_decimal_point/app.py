#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
  diezveces=num*10
  result=int(diezveces%10)
  return result



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(1.79))