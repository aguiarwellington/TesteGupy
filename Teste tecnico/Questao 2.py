#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Função para verificar se o número está na sequência de Fibonacci
def verificar_fibonacci(num):
    fib = fibonacci(num)
    if num in fib:
        return True
    else:
        return False


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verificação e resposta
if verificar_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")