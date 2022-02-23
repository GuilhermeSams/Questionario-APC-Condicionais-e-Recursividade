'''Números Maravilhosos
Números Maravilhosos constituem um problema muito bem conhecido no meio da matemática. Esse problema tem diversos outros
nomes e um deles é a Conjectura de Siracusa. Uma conjectura em matemática é uma proposição ou sentença tida como verdade
que, no entanto, nunca foi provada. Quando é provada ser verdadeira ela passa a ser um Teorema. A Conjectura de Siracusa
tem o seguinte enunciado: "A partir de qualquer número n, dividindo-o por 2 se for par, ou multiplicando por 3 e
adicionando 1 se for ímpar, e fazendo assim sucessivamente, chegaremos sempre ao número 1".

Números Maravilhosos


De uma maneira recursiva, esse problema pode ser visto da seguinte forma:

maravilhosos(x)=⎧⎩⎨1maravilhosos(3x+1)maravilhosos(x2)se x=1se x for imparse x for par

Dessa forma, implemente um programa para receber um valor x e imprimir a sequência de números que x irá tomar até que
seu valor alcance 1. Seu programa deve possuir uma função recursiva chamada maravilhosos com um parâmetro chamado x que
irá receber um valor e deverá imprimir recursivamente a aplicação da função até que o caso base (valor 1) seja
alcançado.


A Entrada consiste de:
1 inteiro x tal que (1<x<105).

A Saída deve apresentar:
Cada linha da saída deve possuir um inteiro da sequência até o número um, conforme os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).

Descrição dos Exemplos:
No primeiro exemplo, o contador começa em 4 e seu valor é impresso na primeira chamada a função. Sendo 4 um número par,
a função maravilhosos foi chamada novamente passando como parâmetro o número 2 que é impresso na tela. Sendo 2 um número
 par, a função maravilhosos foi chamada novamente passando como parâmetro o número 1 que é impresso na tela. No caso do
 número 1 a função encerra sua execução.
No segundo exemplo, o contador começa em 5 e seu valor é impresso na primeira chamada a função. Sendo 5 um número ímpar,
a função maravilhosos foi chamada novamente passando como parâmetro o número 16 que é impresso na tela. Sendo 16 um
número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 8 que é impresso na tela.
Sendo 8 um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 4 que é impresso na
tela. E assim a execução segue o mesmo caminho descrito no primeiro caso de teste.
No terceiro exemplo, o contador começa em 7 e seu valor é impresso na primeira chamada a função. Sendo 7 um número
ímpar, a função maravilhosos foi chamada novamente passando como parâmetro o número 22 que é impresso na tela. Sendo 22
um número par, a função maravilhosos foi chamada novamente passando como parâmetro o número 11 que é impresso na tela.
Sendo 11 um número ímpar, a função maravilhosos foi chamada novamente passando como parâmetro o número 34 que é impresso
na tela. Bem, acho que você entendeu não é?'''


n = int(input())
if n == 1:
    print(1)

def maravilhosos(n):
    if n % 2 == 0:
        print(n)
        maravilhosos(n // 2)
        if n == 2:
            print(1)
    else:
        if n != 1:
            print(n)
            maravilhosos(n * 3 + 1)
        if n == 2:
            print(1)
