'''Elabore a função divisor, que recebe como parâmetro dois números inteiros a e b e verifica se o segundo é divisor do
primeiro. Em caso positivo, exiba "b eh divisor de a", em caso negativo, "b nao eh divisor de a, o resto da operacao eh
 c".

A Entrada consiste de:
Não se aplica.

A Saída deve apresentar:
Uma string, conforme os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle
irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, o número 6 não divide o 13, pois essa operação tem resto 1 (13=6×2+1).
No segundo exemplo, o número 7 divide o 28.'''


def divisor(a, b):
    calc_resto = a % b
    if calc_resto != 0:
        print(f'{b} nao eh divisor de {a}, o resto da operacao eh {calc_resto}')
    elif calc_resto == 0:
        print(f'{b} eh divisor de {a}')


divisor(502, 5)
