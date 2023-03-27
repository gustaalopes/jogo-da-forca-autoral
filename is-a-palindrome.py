def isAPalindrome():
    var = str(input('Insira uma palavra, frase ou número para descobrir se é um palíndromo ')).lower().strip()

    palavra = var.replace(".", "").replace("-", "").replace(" ", "").replace(",", "")

    li = [x for x in palavra]
    lista = [x for x in li[::-1]]

    if li == lista:
        return print(f'"{var}" é um palíndromo!')
    else:
        return print(f'"{var}" não é um palíndromo!')


isAPalindrome()
