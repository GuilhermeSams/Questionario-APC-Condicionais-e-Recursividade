'''O programa abaixo apresenta uma implementação completa da sequência de Fibonacci de forma recursiva, porém, ao executar, é possível notar que nada está sendo impresso. Seu trabalho é analisar o código e realizar todas as alterações necessárias para que o programa funcione como o esperado.

def fibonacci(n):
    if n:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1

A Entrada consiste de:
Um número inteiro n indicando qual é a posição do número na sequência de Fibonacci desejado.

A Saída deve apresentar:
O número na posição desejada da sequência de Fibonacci.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Lembrando que a sequência de Fibonacci é 0, 1, 1, 2, 3, 5, 8, 13, 21... e que os casos de testes foram dados com os
índices da sequência iniciando em 1.

Descrição dos Exemplos:
No primeiro exemplo, o Fibonacci de 2 deve apresentar o valor 1.
No segundo exemplo, o Fibonacci de 5 deve apresentar o valor 5.'''


n = int(input())
n = n - 1


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))


