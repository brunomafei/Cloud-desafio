def fibonacci_recursivo(N):
    #evita numeros negativos
    if N <= 0: 
        return 0
    elif N == 1:
        return 1
    else:
        return fibonacci_recursivo(N - 1) + fibonacci_recursivo(N - 2)

def fibonacci_linear(N):
    #evita numeros negativos
    if N <= 1:
        return N
    
    anterior = 0
    atual = 1

    for i in range(2, N + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo

    return atual


def primo_recursivo(N, divisor=3):
    # não primo
    if N <= 1:
        return False
    # unico par
    elif N == 2:
        return True
    # tira pares
    elif N % 2 == 0:
        return False
        
    if divisor == N:
        return True

    if N % divisor == 0:
        return False

    return primo_recursivo(N, divisor + 2)

def primo_linear(N):
    #não primo
    if N <= 1:
        return False
    #unico primo par
    elif N == 2:
        return True
    #testa pra ver se e impar
    elif N % 2 != 0:
        for i in range(3, N, 2):
            if N % i ==0:
                return False
            
        return True
    
    else:
        return False