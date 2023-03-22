import random


def jogar():
    abertura()
    enforcou = False
    ganhou = False
    palavra_secreta = carrega_palavra()
    palavra_escondida = inicializar_palavra_secreta(palavra_secreta)
    tentativa = 0
    print('A palavra secreta foi gerada. Boa sorte no seu jogo!')
    print(palavra_escondida)

    while not enforcou and not ganhou:
        chute = pede_chute()

        if chute in palavra_secreta:
            chutes_corretos(chute, palavra_secreta, palavra_escondida)
            if '_' not in palavra_escondida:
                ganhou = True
                vencedor(palavra_secreta)
        else:
            tentativa += 1
            print("Letra NÃO encontrada!")
            if tentativa < 6:
                print(f'Você ainda possui {6 - tentativa} tentativas!')
                print(palavra_escondida)
            else:
                enforcou = True
                enforcado(palavra_secreta)


def chutes_corretos(chute, palavra_secreta, palavra_escondida):
    index = 0
    for _ in palavra_secreta:
        if chute == palavra_secreta[index]:
            palavra_escondida[index] = chute
        index += 1
    print(f'Letra {chute} foi encontrada!')
    print(palavra_escondida)


def carrega_palavra():
    print('Você tem duas opções de tema para jogar!')
    print('Escolha o tema a ser jogado:')
    answer = input('"Futebol" ou "Frutas"?: ')
    answer.strip().lower()
    if answer == 'futebol':
        file = open("futebol.txt", "r")
    elif answer == 'frutas':
        file = open("frutas.txt", "r")
    else:
        print('Tema invalido, digite o tema corretamente')
        carrega_palavra()

    palavras = []

    for palavra in file:
        palavra = palavra.strip().upper()
        palavras.append(palavra)

    file.close()
    numero = random.randrange(0, len(palavras))
    palavra_escolhida = palavras[numero]

    return palavra_escolhida


def inicializar_palavra_secreta(palavra_escolhida):
    return ['_' for _ in palavra_escolhida]


def pede_chute():
    chute = input('Digite uma letra: ').upper().strip()
    return chute


def vencedor(palavra_secreta):
    print('Parabéns! Você ganhou!')
    print(f'A palavra secreta era {palavra_secreta}')


def enforcado(palavra_secreta):
    print('Suas tentativas acabaram e você perdeu!')
    print(f'A palavra secreta era {palavra_secreta}')


def abertura():
    """Função que define a mensagem de abertura, indicando as regras do jogo."""
    print('-----------------------------------')
    print('----BEM VINDO AO JOGO DA FORCA!----')
    print('-----------------------------------')
    print('As regras são as seguintes: Você dará seu palpite, que será uma letra')
    print('Caso a letra seja encontrada na palavra secreta, você verá a posição dela na palavra!')
    print('Caso a letra não seja encontrada na palavra, perderá 1 tentativa.')
    print('Você só terá 6 possibilidades de erro. Caso erre 6 vezes, seu boneco será enforcado.')
    print('Você poderá escolher entre 2 temas: Frutas e times de futebol')
    print('Boa sorte e vamos jogar!')


if __name__ == '__main__':
    jogar()
