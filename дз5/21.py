# 1. Создайте программу для игры с конфетами человек против человека.    
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?    
# a) Добавьте игру против бота    
# b) Подумайте как наделить бота "интеллектом"    


from random import randint as r
from random import choice as ch

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите', 'Ваш ход']

def introduce_players():
    player1 = input("Давайте познакомимся. Как Вас зовут??\n")
    player2 = 'Конфетный бот'
    print(f'Рад с Вами познакомиться, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет мы раздадим?\n '))
    m = int(input('Сколько конфет мы можем взять за один ход?\n '))
    first = int(input(
        f'{players[0]}, если вы хотите ходить первым, нажмите "1", если нет, - любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = r(1, rules[1])
            print(f'Я беру {move}')
        else:
            print(f'{players[0]}, {ch(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f"Это слишком много, ты не можешь взять больше {rules[1]} конфет {letter}, у нас осталось {rules[0]} конфет {letter}")
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте еще раз, у вас есть {attempt} попыток')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Извините, у Вас больше нет попыток. Игра окончена!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет {letter}')
        else:
            print('Все конфеты закончились.')
        count += 1
    return players[count % 2]


players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя. (ничья)')
else:
    print(f'Поздравляю! На этот раз  {winer} выиграл! Он получает все конфеты!')









