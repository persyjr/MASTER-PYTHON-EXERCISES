#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  num_string=str(num)
  long_num=len(num_string)
  num_array=[]
  suma=0
  for i in range(0,long_num):
    numero=int(num_string[i])
    num_array.append(numero)
  for i in num_array:
    suma=suma+i  
    
  return suma


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))