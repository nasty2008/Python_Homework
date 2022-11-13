import telebot
import random

bot = telebot.TeleBot('5474740493:AAGcPzSSpAlGNjHVZlLvgJXL36y7MZ8zOKM', parse_mode = None)

candy=2021
fate = 0
user_id = 0
min_move = 1
global_max = 28
max_move = global_max
min_candy = 10
max_candy = 50
game_over = False

@bot.message_handler(commands=['start'])
def new_game(message):
    global game_over
    global bot
    game_over = False
    global max_move
    global global_max
    max_move = global_max
    global candy
    candy 
    fate = random.randint(0, 1)
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id,
                     f"Здравствуй, человек! Давай сыграем с тобой в игру!\nУ нас есть {candy} конфет.\nТот кто заберет последнюю конфету - победил. За один раз можно брать не более {max_move} и не менее {min_move} конфеты")
    if fate:
        bot.send_message(user_id, "Первым ходит игрок\nВведите число конфет:")
    else:
        bot.send_message(user_id, f"Первым ходит бот")
        ai_move()

@bot.message_handler(func=lambda m: True)
def user_move(message):
    global game_over
    global min_move
    global max_move
    global candy
    global user_id
    global bot
    error = True
    if game_over:
        bot.send_message(user_id, f"Игра окончена.\nЕсли хотите сыграть еще раз, введите /start")
    else:
        if max_move>candy:
            max_move=candy
        if message.text.isdigit():
            if int(message.text) > min_move - 1 and max_move + 1 > int(message.text):
                move = int(message.text)
                error = False
        if error:
            bot.send_message(user_id, f"Некорректные данные.\nВведите число от {min_move} до {max_move}")
            if message.text.isdigit and (int(message.text) > min_move - 1 and max_move + 1 > int(message.text)):
                move = int(message.text)
                error = False
        else:
            candy -= move
            win_combo()
            if game_over:
                bot.send_message(user_id, f"Вы победили!")
                bot.send_message(user_id, f"Может, ещё разок? /start!!!")
            else:
                ai_move()

def ai_move():
    global user_id
    global game_over
    global min_move
    global max_move
    global candy
    global bot
    bot.send_message(user_id, f"Осталось {candy} конфет")
    if max_move>candy:
        max_move=candy
    bot.send_message(user_id, f"Можно взять от {min_move} до {max_move} конфет")
    if random.randint(0,1):
        bot_move=random.randint(min_move,max_move)
    else:
        bot_move = candy%(max_move+1)
        if bot_move == 0:
            bot_move = random.randint(min_move, max_move)
    bot.send_message(user_id, f"Бот взял {bot_move} конфет")
    candy -= bot_move
    win_combo()
    if game_over:
        bot.send_message(user_id, f"Бот обыграл Вас!")
        bot.send_message(user_id, f"Сыграем еще раз? /start!!!")
    else:
        if max_move>candy:
            max_move=candy
        bot.send_message(user_id, f"Осталось {candy} конфет.\nВозьмите от {min_move} до {max_move} конфет")

def win_combo():
    global game_over
    if candy == 0:
        game_over = True

bot.infinity_polling()