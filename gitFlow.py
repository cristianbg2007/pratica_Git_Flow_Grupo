#calculadora con git flow

import calculadora as calc
    
def calcsuma():
    # aqui se va calcular la suma
    return


def calculadora_restando(n1, n2):
    restar=calc.restar(n1, n2)
    return restar


def iniciar_aplicacion():
    opcion=int(input("digite 1 sumar. digite 2 restar: "))
    
    if(opcion == 1):
        n1=int(input("digite el primer numero"))
        n2=int(input("digite el segundo numero"))

        #mandar a llamar la funcion
    else:
        n1=int(input("digite el primer numero"))
        n2=int(input("digite el segundo numero"))
        print("el resultado de la resta es: ", calculadora_restando(n1, n2))
iniciar_aplicacion()