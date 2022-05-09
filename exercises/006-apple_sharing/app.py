#Complete the function to return:
#1) How many apples each single student will get.
#2) How many apples wil remain in the basket.
#Hint: You can resolve this exercise either importing the math module or without it 
def apple_sharing(n,k):
  parte_enetera=int(k/n)
  parte_indivisible=k%n
  result=(parte_enetera,parte_indivisible)
  return result
 
    

#Print the two answer per the example output.
print(apple_sharing(6,50))