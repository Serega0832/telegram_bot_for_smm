import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('sticks/welcome.tgs ', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("О компании")
	item2 = types.KeyboardButton("Наши услуги")
	item3 = types.KeyboardButton("Примеры")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'О компании':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Контакты", callback_data='contacts')
			item2 = types.InlineKeyboardButton("Сайт", url='https://habrahabr.ru')
			item3 = types.InlineKeyboardButton("Инстаграм", url='https://instagram.com/cube_online_russia')

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Компания является экспертом..', reply_markup=markup)
		elif message.text == 'Наши услуги':
			bot.send_message(message.chat.id, 'Тут должны быть фотки')
		elif message.text == 'Примеры':
			bot.send_message(message.chat.id, 'Здесь вы можете посмотреть примеры наших работ\n[Рестораны 🍕🍷]\n@BigBuddaVLBot'.format(message.from_user, bot.get_me()),
		parse_mode='html')
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'contacts':
				bot.send_message(call.message.chat.id, 'Мы находимся по адресу: г.Москва, Варшавское шоссе д.1 ст 1, офис В605')

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)