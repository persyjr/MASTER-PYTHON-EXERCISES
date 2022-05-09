import math
#definiendo variables
C=50
H=30
D=int(input("\n Q=sqrt((2*C*D)/H) \n ingrese un numero para D ej: 50 \n\n"))
print("El valor ingresado es D=", D)
#evaluabdo la funcion
Q=math.sqrt((2*C*D)/H)
#redondeando
result=int(Q)

print("El resultado es:Q= ", result)