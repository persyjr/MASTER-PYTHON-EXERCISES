
class PruebaString:
    def __init__(self):
        self.string = str(input("ingrese un String\n"))
        self.stringMay=''
#definiendo las propiedades y asignando valores mediante input y predefinido        
    def getString(self):
        self.stringMay=self.string
        print(self.stringMay)
        return self.stringMay  
        #metodo para almacenar un string en variable stringMay
    def printString(self):
        self.stringMay=self.string.upper()
        print(self.stringMay)
        #método para imprimir string definido mediante input y devolverlo en mayuscula

p1 = PruebaString()
p1.printString()
p1.getString()




