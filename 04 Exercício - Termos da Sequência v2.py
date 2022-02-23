'''Implemente uma função recursiva chamada imprimeTermos que receba um número inteiro n e imprima os termos da
sequência −n,−n+2,...,0, isto é, os termos da sequência que começa pelo valor −n e termina em 0, de 2 em 2 valores, de
maneira crescente.


A Entrada consiste de:
A função recebe como parâmetro um único número inteiro n (2≤n≤109).

A Saída deve apresentar:
os termos que compõem a sequência estabelecida, sendo que cada termo da sequência −n,−n+2,...,0 deve ser impresso em
única linha.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, a função recebe como parâmetro o número e portanto imprime 8,
depois -8+2=-6, e na sequência, -4, -2 e 0'''


def imprimeTermos(n):
    if n >= 0:
        print(-n)
        imprimeTermos(n - 2)
        if n == 1:
            print(0)


imprimeTermos(8)
