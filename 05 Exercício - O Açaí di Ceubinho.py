def qtdcopos(n):
    if n // 4:

        if n % 3 == 0 :
            calc = n // 4
            result = calc - 4
            sub = result - 4
            print(f'Pode voltar pro ceubinho, deivis! Falta(m) {abs(sub)} copo(s)!')
        elif n % 2 == 0:
            print('Pode levar pros calourinhos, deivis!')
        else:
            calc = n // 4
            result = calc - 4
            sub = result - 4
            print(f'Pode voltar pro ceubinho, deivis! Falta(m) {abs(sub)} copo(s)!')

qtdcopos(15)