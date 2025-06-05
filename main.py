import math 


# define os intervalos e erros
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
e = float(input("Digite o valor do erro: ")) 


# define uma função 
def f(x):
    return x**2 - 5  

# teorema de bolzano 
if f(a) * f(b) < 0:
    # enquanto o modulo for menor que o erro não atingimos o valor
    while (math.fabs((b-a)/2 > e)):
        xi = (a+b)/2 
        if f(xi) == 0:
            print("01 A raiz é:", xi)
            break
        else:
            if f(a) * f(xi) < 0:
                b = xi 
            else:
                a = xi
    print("02 A raiz é:", xi)
else:
    print("Não há raiz no intervalo dado!")