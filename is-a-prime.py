def isAPrime(num):
    primo = 0
    for i in range(2, num):
        if num % i == 0:
            primo += 1
            #print(i) -> Caso não seja primo, mostra os números que dividem o número
            # que é fornecido (sem incluir o 1 e o próprio número)

    if primo == 0:
        print(f'{num} é um número primo')
    else:
        print(f'{num} não é um número primo')

isAPrime(7)