import math

def bissecao(f, a, b, epsilon, max_iter):
    """
        f (function): Função a ser analisada.
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        epsilon (float): Critério de parada (tolerância).
        max_iter (int): Número máximo de iterações.
    """
    if f(a) * f(b) >= 0:
        return None, 0, False  # Não há raiz no intervalo
    
    iteracao = 0
    xi_anterior = a  # Valor inicial para cálculo do erro
    
    print("\n{:^10} {:^15} {:^15} {:^15} {:^15} {:^15}".format(
        "Iteração", "a", "b", "xi", "f(xi)", "Erro (|b-a|/2)"))
    print("-" * 85)
    
    while iteracao < max_iter:
        xi = (a + b) / 2
        erro = abs(b - a) / 2  # Erro máximo possível
        
        # Saída intermediária formatada
        print("{:^10} {:^15.8f} {:^15.8f} {:^15.8f} {:^15.8f} {:^15.8f}".format(
            iteracao + 1, a, b, xi, f(xi), erro))
        
        if abs(f(xi)) < 1e-12:  # Considera como raiz exata
            return xi, iteracao + 1, True
        
        if f(a) * f(xi) < 0:
            b = xi
        else:
            a = xi
        
        if erro < epsilon:
            return xi, iteracao + 1, True
        
        iteracao += 1
    
    return xi, max_iter, False  # Retorna o melhor valor mesmo sem convergência

# Entrada do usuário
def obter_funcao():
    expr = input("Digite a função: ")
    return lambda x: eval(expr)

# Configurações do método
print("\nMétodo da Bisseção - Encontrar raízes de f(x) = 0")
f = obter_funcao()
a = float(input("Limite inferior do intervalo (a): "))
b = float(input("Limite superior do intervalo (b): "))
epsilon = float(input("Tolerância (E): "))
max_iter = int(input("Número máximo de iterações: "))

# Execução do método
raiz, iteracoes, convergiu = bissecao(f, a, b, epsilon, max_iter)

# Resultados
print("\n--- Resultados ---")
if raiz is not None:
    print(f"Raiz aproximada: {raiz:.8f}")
    print(f"Valor de f(raiz): {f(raiz):.2e}")
    print(f"Iterações realizadas: {iteracoes}/{max_iter}")
    print(f"Convergiu? {'Sim' if convergiu else 'Não (atingiu o máximo de iterações)'}")
else:
    print("Erro: f(a) e f(b) devem ter sinais opostos (Teorema de Bolzano não satisfeito)!")