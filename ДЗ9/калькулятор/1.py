import telepot
from telepot.loop import MessageLoop
from pprint import pprint

bot = telepot.Bot('5741153445:AAGLDMmyv466AsUPPScTI45yBnrwREKH2tc')

response = bot.getUpdates()

pprint(response)

TOKEN = '5741153445:AAGLDMmyv466AsUPPScTI45yBnrwREKH2tc'
bot = telepot.Bot(TOKEN)

def handle(msg):
    """ Process request like '3+2' """
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
    except:
        answer = "Can't calculate :("
    bot.sendMessage(chat_id, "answer: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break