from Conjunto import Conjunto

def imprimir():
    print(" ")
    print("--------MENU----------")
    print("1. Unir Conjunto")
    print("2. Diferencia de dos conjuntos")
    print("3. Verificar si los conjuntos son iguales")
    print("0. Salir")
    print(" ")

#def menu(unConjunto,otroConjunto):
def menu(c1,c2):
    print(" ")
    print("--------------------------------------------------------")
    print("El primer conjunto es: ",c1.mostrar())
    print("El segundo conjunto es: ",c2.mostrar())
    print("--------------------------------------------------------")
    band=True
    while band:
        imprimir()
        op=int(input("Ingrese una opcion: "))

        if op==1:
            c=c1+c2
            print("Union: ", c.mostrar())
            print(" ")

        elif op==2:
            c=c1-c2
            print("Diferencia: ", c.mostrar())

        elif op==3:
            if c1==c2:
                print("Son iguales")

            else:
                print("No son iguales")

        else:
            print("Chau :)")
            band=False


if __name__=='__main__':
    c1=[65,85,32,42,4,15]
    c2=[25,32,14,21,2,14]
    c1=Conjunto(c1)
    c2=Conjunto(c2)
    menu(c1,c2)


