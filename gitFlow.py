#calculadora con git flow

import calculadora as calc
    
def calcsuma(n1,n2):
    sumar=calc.Sumar(n1,n2)
    return sumar


def calculadora_restando():
    #se va calcular la resta
    return


def iniciar_aplicacion():
    opcion=int(input("digite 1 sumar. digite 2 restar: "))
    
    if(opcion == 1):
        n1=int(input("digite el primer numero"))
        n2=int(input("digite el segundo numero"))
        print("el resultado de la suma es: ", calcsuma(n1, n2))
    else:
        n1=int(input("digite el primer numero"))
        n2=int(input("digite el segundo numero"))

        #mandar a llamar la funcion
iniciar_aplicacion()
