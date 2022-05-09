#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  decenas=int(digit/10)
  unidades=digit%10
  result=(decenas, unidades)
  return result
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
