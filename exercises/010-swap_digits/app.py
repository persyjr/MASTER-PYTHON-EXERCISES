#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  decenas=int(num/10)
  unidades=num%10
  result=str(unidades)+str(decenas)
  result=int(result)
  return result
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
