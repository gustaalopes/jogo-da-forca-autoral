import time

def rest(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
        if t == 0:
            print('Descanso encerrado!')


series = int(input('Insira a quantidade de séries do exercício: '))
rest_time = int(input('Insira, em segundos, o tempo de descanso: '))


def exercise(series, rest_time):
    #Inicializando
    print(
        f'Exercício iniciado. {series} séries serão realizadas nesse exercício.'
        f'\n1ª série de {series} totais. Ao finalizar, sinalize o descanso.')
    start_rest = '' #variável para receber o comando de descanso
    series_count = 0 # variável para contar a quantidade de séries já realizadas

    while start_rest != 'S': #loop para fazer a contagem do descanso + incremento de uma série realizada
        start_rest = input(
            'Começar descanso? ["S" para começar descanso] ').strip().upper() #input para sinalizar o descanso
        if start_rest == 'S': # começo do descanso
            rest(rest_time)
            series_count += 1 #incremento da contagem de séries
            if series_count != series and not series-1 == series_count: #condicionais para dizer a situação atual do exercício
                print(
                    f'Série atual a ser realizada: {series_count+1}º de {series} séries.')
            elif series-1 == series_count:
                print(f'{series_count+1}º e última série a ser realizada.')
            else:
                return print(f'Exercício encerrado! Você realizou a {series_count}º e última série.'
                      '\nVá para o próximo exercício.')
            start_rest = 'N'



exercise(series, rest_time)
