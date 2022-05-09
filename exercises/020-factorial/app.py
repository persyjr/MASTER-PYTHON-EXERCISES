# Your code here

def factorial(n):
    num_factorial=1
    for i in range(n,1,-1):
        num_factorial=num_factorial*i
    print(num_factorial)    
    return num_factorial

factorial(8)