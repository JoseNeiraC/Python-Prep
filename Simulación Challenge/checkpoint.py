# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if type(numero) != int:
        return 'Ingresar numero entero'
    if numero < 1:
        return 'Ingresar un numero mayor a cero'
    if numero > 1:
        numero = numero * Factorial(numero - 1)
    return numero

    
   

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    primo = True
    if type(valor) != int:
        return "Valor nulo"
    for div in range (2,valor):
        if valor % div == 0:
            primo = False
            break
        
    return primo
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    return 'Funcion incompleta'

class Animal:
    def __init__ (self, edad,especie, color):
        self.edad = edad
        self.especie = especie
        self.color = color
        
        if (type(edad) != int):
            print ("Ingrese un numero entero")
        
        elif (edad <= 0):
            print ("Ingrese un valor igual o mayor a cero")
        else:
            print(self.edad)
            print(self.especie)
            print(self.color)
            

    def cumplirAnios(self):  
        self.edad = self.edad + 1
