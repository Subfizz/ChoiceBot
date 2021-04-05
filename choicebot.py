import telebot
import random
USERS = []

bot = telebot.TeleBot('');


@bot.message_handler(commands=['start'])
def start(message):
	if message.chat.id not in USERS:
		bot.send_message(message.chat.id, 'Привет! Это бот, который поможет тебе определиться с выбором. Подумай, какое действие или предмет относится к какой цифре и выбери количество исходов! Что выпало, то и выбирай! Пиши /random', parse_mode='html')
		USERS.append(message.chat.id)
	else:
		bot.send_message(message.chat.id, 'Извини, ты уже его активировал')


@bot.message_handler(commands=['random'])
def start(message):
	bot.send_message(message.chat.id,'Количество исходов?')
	bot.register_next_step_handler(message, get_login)

def get_login(message):
	global iscount
	iscount = message.text
	ran = ''.join(iscount)
	try:
		randumb = random.randint(int(1), int(ran))
		bot.send_message(message.chat.id,randumb)
	except ValueError:
		bot.send_message(message.chat.id,'не число')
	bot.register_next_step_handler(message, get_login)


if __name__ == '__main__':
	bot.polling(none_stop=True)
