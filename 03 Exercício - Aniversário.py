'''Elabore um programa que receba um número inteiro, representando a quantidade de dias que uma pessoa tem de vida, e
retorne o número de anos, meses e dias que essa pessoa possui. Este programa deve considerar que um ano tem 365 dias e
um mês tem 30 dias.  Caso seja o aniversário da pessoa, retorne também a string "pa-pa-pa-parabensss!!!".


A Entrada consiste de:
Um número inteiro positivo, representando os dias de vida da pessoa.

A Saída deve apresentar:
Uma string com os anos, meses e dias que a pessoa tem de vida, em caso de ser o seu aniversário, mais uma string
conforme indica o enunciado e os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, a pessoa possui 588 dias de vida, o que equivale a 1 ano, 7 meses 13 dias.
No segundo exemplo, a pessoa possui 2555 dias de vida, o que equivale a exatos 7 anos. Como a pessoa está completando
7 anos nesse dia, a string "pa-pa-pa-parabensss!!!" também é exibida.'''

dias_de_vida = int(input())

ano = (dias_de_vida // 365)

calc_mes = 365 * ano
calc_1_mes = dias_de_vida - calc_mes
mes = calc_1_mes // 30

calc_1_dias = calc_1_mes - 30
dia = calc_1_dias % 30
if mes == 0 and dia == 0:
    print(f'{ano} anos, {mes} meses e {dia} dias')
    print("pa-pa-pa-parabensss!!!")
else:
    print(f'{ano} anos, {mes} meses e {dia} dias')
