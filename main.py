import math

def bissecao(f, a, b, parada, max_iter):
    """
        f (function): Função a ser analisada.
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        parada (float): Critério de parada (tolerância).
        max_iter (int): Número máximo de iterações.
    
    """
    if f(a) * f(b) >= 0:
        return None, 0, False  # Não há raiz no intervalo
    
    iteracao = 0
    xi = a  # Valor inicial
    
    while iteracao < max_iter:
        xi_anterior = xi
        xi = (a + b) / 2
        erro = abs(xi - xi_anterior)
        
        if abs(f(xi)) < 1e-12:  # Considera como raiz exata
            return xi, iteracao + 1, True
        
        if f(a) * f(xi) < 0:
            b = xi
        else:
            a = xi
        
        if erro < parada:
            return xi, iteracao + 1, True
        
        iteracao += 1
    
    return xi, max_iter, False  # Retorna o melhor valor mesmo sem convergência

# Entrada do usuário
def obter_funcao():
    expr = input("Digite a função: ")
    return lambda x: eval(expr)

# Configurações do método
print("Método da Bisseção - Encontrar raízes de f(x) = 0")
f = obter_funcao()
a = float(input("Limite inferior do intervalo (a): "))
b = float(input("Limite superior do intervalo (b): "))
parada = float(input("Tolerância (e): "))
max_iter = int(input("Número máximo de iterações: "))

# Execução do método
raiz, iteracoes, convergiu = bissecao(f, a, b, parada, max_iter)

# Resultados
print("\n--- Resultados ---")
if raiz is not None:
    print(f"Raiz aproximada: {raiz:.8f}")
    print(f"Valor de f(raiz): {f(raiz):.2e}")
    print(f"Iterações realizadas: {iteracoes}/{max_iter}")
    print(f"Convergiu? {'Sim' if convergiu else 'Não (atingiu o máximo de iterações)'}")
else:
    print("Erro: f(a) e f(b) devem ter sinais opostos (Teorema de Bolzano não satisfeito)!")