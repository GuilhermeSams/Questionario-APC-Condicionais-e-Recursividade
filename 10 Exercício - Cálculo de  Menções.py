'''Recentemente, o professor Jonas tomou um interesse particular pela programação. Ao longo de diversas conversas
bastante produtivas com seus alunos que estão cursando APC, ele se convenceu de que a forma que calcula as notas dos
alunos em cada prova já está datada e bastante tediosa.

Atualmente, o processo para o cálculo das notas segue algumas etapas bem simples, que Jonas realiza manualmente há anos.
Primeiramente, é preciso ter todas as notas das 3 provas que ocorreram durante o semestre. Ele então verifica as 3 notas
de um aluno e se assegura de que todas são maiores ou iguais a 5. Caso qualquer uma das notas esteja abaixo de 5 o aluno
será reprovado. Caso todas as notas sejam maiores ou iguais a 5 o aluno será aprovado. Por fim, ele verifica em ordem as
notas das 3 provas, classificando-as sob o sistema de menções da UNB em MM, MS e SS.

Considerando esse processo, Jonas buscou tutoriais online e tentou por conta própria implementar um programa que
facilite o cálculo das menções de seus alunos. Houve algum progresso, mas seu código ainda possui vários erros que ele
 simplesmente não consegue entender.

Segue abaixo o código de Jonas para você depurar.

entradas = input().split()
n1 = int(entradas[0])
n2 = int(entradas[1])
n3 = int(entradas[2])

if n1 > 5 and n2 > 5 and n3 >5:
    print('APROVAR')

    #Cálculo da nota 1
    if n1 >= 5 and n1 < 7:
        print('Prova 1: MM')
    if n1 >= 7 and n1 < 9:
        print('Prova 2: MS')
    else:
        print('Prova 1: SS')
    #Cálculo da nota 2
    if n2 >= 5 and n2 < 7:
        print('Prova 2: MM')
    if n2 >= 7 and n2 < 9:
        print('Prova 2: MS')
    else:
        print('Prova 2: SS')
    #Cálculo da nota 3
    if n1 >= 5 and n1 < 7:
        print('Prova 2: MM')
    if n1 >= 7 and n1 < 9:
        print('Prova 2: MS')
    else:
        print('Prova 2: SS')

else:
    print('REPROVAR')



A Entrada consiste de:
3 números inteiros: N1, N2 e N3 representando cada uma das notas nas 3 provas.

A Saída deve apresentar:
Em caso de reprovação o programa deve mostrar somente a mensagem "REPROVAR".
Em caso de aprovação o programa deve mostrar a mensagem "APROVAR". Em seguida deve mostrar a cada linha a menção obtida
 em cada uma das 3 provas no formato: "Prova X: Menção" onde X é o número da prova e Menção é a menção obtida
(MM, MS ou SS).

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Não se preocupe em alterar o código relativo à entrada de dados.
É aconselhável que a depuração seja realizada majoritariamente em seu próprio computador e não no Moodle. Assegure-se
de que sua resposta está correta antes de enviar para que não haja desconto na pontuação.

Descrição dos Exemplos:
Os exemplos são autoexplicativos.
'''

n1, n2, n3 = map(int, input().split())

# Cálculo da nota 1
if n1 >= 5 and n2 >=5 and n3 >= 5:
    print("APROVAR")
    #Cálculo nota 1
    if n1 >= 5 and n1 < 7:
        print('Prova 1: MM')
    elif n1 >= 7 and n1 < 9:
        print('Prova 1: MS')
    else:
        print('Prova 1: SS')

    # Cálculo da nota 2
    if n2 >= 5 and n2 < 7:
        print('Prova 2: MM')
    elif n2 >= 7 and n2 < 9:
        print('Prova 2: MS')
    else:
        print('Prova 2: SS')

    # Cálculo da nota 3
    if n3 >= 5 and n3 < 7:
        print('Prova 3: MM')
    elif n3 >= 7 and n3 < 9:
        print('Prova 3: MS')
    elif n3 >= 9:
        print('Prova 3: SS')

else:
    print("REPROVAR")
