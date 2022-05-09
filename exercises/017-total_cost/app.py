#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    dolares=d*n
    centavos=c*n
    precio=(dolares,centavos)
    return precio
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(10,15,2))
