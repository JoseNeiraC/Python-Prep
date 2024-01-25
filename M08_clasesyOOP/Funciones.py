class Funciones:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
    
    def verificar_Primo (self):    # Pendiente resolver Fault
        for i in self.lista:
            if (self.__verificar_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')        
        # Funcion Primo anterior ara un solo numero
        # primo = True
        # for div in range (self.lista):
        #     if self.lista % div == 0:
        #         primo = False
        #         break
        # return primo


    def valor_Modal (self, lista):
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
        

    def conversion_grados (self, valor, origen, destino):
        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor
            elif destino == 'farenheit':
                valor_destino = (valor * 9/5) + 32
            elif destino ==  'kelvin':
                valor_destino = valor + 273.15
            else:
                print("Ingrese un destino correcto")
    
        elif origen ==  'farenheit':
            if destino == 'celsius':
                valor_destino = (valor-32)*5/9
            elif destino == 'farenheit':
                valor_destino = valor
            elif destino ==  'kelvin':
                valor_destino = ((valor-32)*5/9) + 273.15
            else:
                print("Ingrese un destino correcto")
    
        elif origen == 'kelvin':
            if destino == 'celsius':
                valor_destino = valor - 273.15
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15)*9/5) + 32
            elif destino ==  'kelvin':
                valor_destino = valor
            else:
                print("Ingrese un destino correcto")
        else:
            print('Ingrese un origen correcto')
        return valor_destino

    def factorial (self, numero):
        if type(numero) != int:
            return 'Ingrese un numero entero'
        if numero < 1:
            return 'Ingrese un numero mayor a cero'
        if numero > 1:
            numero = numero * self.factorial(numero - 1)
        return numero

