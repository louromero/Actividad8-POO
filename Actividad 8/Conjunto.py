class Conjunto:
    __conjunto=[]

    def __init__(self,lista):
        self.__conjunto=lista

    
    def mostrar(self):
        return self.__conjunto

    def getLista(self):
        return self.__conjunto

    def __add__(self,otro):
        uno=self.__conjunto+otro.getLista()
        #self es el conjunto1
        #getLista es el conjunto2
        return Conjunto(uno)

    def __sub__(self,otro):
        nuevo = self.__conjunto.copy()
        for x in otro.getLista():
            if x in nuevo:
                #Remove elimina el primer elemento con el valor especificado (x)
                nuevo.remove(x)
        return Conjunto(nuevo)

    def __eq__(self, otro):
        if self.__conjunto == otro.getLista():
            return True
        else:
            return False

