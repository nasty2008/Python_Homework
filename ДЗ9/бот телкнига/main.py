import UI as ui
import logger as lg
import crud


lg.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()









# import telebot, wikipedia, re
# # Создаем экземпляр бота
# bot = telebot.TeleBot('Здесь впиши токен, полученный от @botfather')
# # Устанавливаем русский язык в Wikipedia
# wikipedia.set_lang("ru")
# # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext=ny.content[:1000]
#         # Разделяем по точкам
#         wikimas=wikitext.split('.')
#         # Отбрасываем всЕ после последней точки
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
#         for x in wikimas:
#             if not('==' in x):
#                     # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'
# # Функция, обрабатывающая команду /start
# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, getwiki(message.text))
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)







# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)
# plt.show()



# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))



# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     bar.next()
# bar.finish()



# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4)) 



