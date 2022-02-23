'''Primeiramente, leia uma string a da entrada padrão e imprima uma frase dependendo da entrada a.

Caso a string a seja "fala", leia outra string b e imprima outra frase dependendo da entrada b.


A Entrada consiste de:
Uma ou duas strings, dependendo da primeira entrada.

A Saída deve apresentar:
Se a primeira entrada for "fala" (sem aspas e toda minúscula), imprima "Oi! Tudo bem?". Se não, imprima "Vou ficar
calado! Ops..." e finalize o programa.
Se a segunda entrada for "tudo beleza", imprima "Hum... Que legal!". Se não, imprima "Poxa, não entendi".

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, foi digitado "fala" e "tudo beleza", returnando "Oi! Tudo bem?" e "Hum... Que legal!"
No segundo exemplo, foi digitado "Fala", retornando "Vou ficar calado! Ops..."
No terceiro exemplo, foi digitado "fala" e "alo", retornando "Oi! Tudo bem?" e "Poxa, não entendi".'''


a = str(input())
if a == 'fala':
    print("Oi! Tudo bem?")
    b = str(input())
    if b == 'tudo beleza':
        print("Hum... Que legal!")
    else:
        print("Poxa, não entendi")
else:
    print("Vou ficar calado! Ops...")
