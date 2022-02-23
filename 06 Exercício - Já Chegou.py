def alerta(a, b):
    if a != b:
        print(f'Ta sussa, {a} horas ainda.')
        alerta(a + 1, b)

    else:
        print("Ja chegou o disco voador!!!!")


alerta(16, 20)
