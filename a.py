# Use API : https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={value}

import telebot
import requests
from telebot import types, TeleBot
import random
import time
from time import sleep

# -- Token -- #
TOKEN = ('5334586594:AAHN34STvQnny1CV1v9y-9a701olsgizFmo')
# --------------
app = telebot.TeleBot(TOKEN)
# -- Buttons -- #
Made_qr_btn = types.InlineKeyboardButton(text='🎟️︙أصنع QR .', callback_data='CreateQr')
version_btn = types.InlineKeyboardButton(text='- Version 2.4.7 ✨ .', callback_data='v')
dev = types.InlineKeyboardButton(text='🙋︙أدارة البوت .', url='tg://openmessages?user_id=2018287597')
# --------
# -- Random emoji in Message Welocme -- #
list_emoji = [
	'😊',
	'☺️',
	'😀',
	'🙃',
	'♥',
	'✨',
	'🤗',
	'🫡',
	'🌝',
	'🫣',
	'💛',
	'❤️‍🔥',
	'🌚',
	'🫶🏻'
	]
@app.message_handler(commands=['start'])
def welcome(message):
	ran_list_emoji = random.choice(list_emoji)
	ran_list_emoji2 = random.choice(list_emoji)
	
	btn = types.InlineKeyboardMarkup()
	btn.row_width = 2
	btn.add(Made_qr_btn,version_btn,dev)
	first_name = message.chat.first_name
	app.reply_to(message,text=f'''
<b>
- هلا والله فيك {first_name} 😌 .
- يمكنك ارسال اي نص او رابط لانشاء QR له ✅ .
----------
{ran_list_emoji} ⌯ شكرا لاستعمال روبوتنا {ran_list_emoji2} .
👨🏻‍💻 ↝ 𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟 : @xwab5 . 
👨🏻‍💻 ⌯ مطور البوت : @xwab5 .
</b>

''', reply_markup=btn, parse_mode='html')

@app.message_handler(func=lambda message: True)
def qr_value(message):
	chat = '2018287597'
	app.forward_message(chat, message.chat.id, message.message_id)
	
	value = message.text
	value_to_qr_ = app.send_message(message.chat.id,text=f'✅︙جاري التحويل الى QR ....')
	"""i = 1
	while i < 101:
		app.edit_message_text(f'✅︙جاري التحويل الى QR ... {i}',value_to_qr_.chat.id,value_to_qr_.message_id)
		i+=1"""
	key = {
		'domain': 'https://api.qrserver.com/v1/create-qr-code/',
		'size': '?size=150x150',
		'data': '&data='+value
	}
	#key = (f'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={value}')
	
	try:
		app.send_chat_action(message.chat.id,action='upload_photo')
		app.edit_message_text(f'📤︙جاري الرفع ...',value_to_qr_.chat.id,value_to_qr_.message_id)

		app.send_photo(message.chat.id,key.get('domain')+key.get('size')+key.get('data'),caption=f'''
		- تم صنع QR بنجاح ✅ .
		----------
		- 🌝 ↝ 𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟 : @xwab5 .
	''', reply_to_message_id=message.id)

		app.delete_message(value_to_qr_.chat.id, value_to_qr_.message_id)
	
	except:
		app.edit_message_text(f'- صار خطأ يالعزيز خخخ، أعد المحاولة !',value_to_qr_. chat.id, value_to_qr_.message_id)
	
@app.callback_query_handler(func=lambda call : True)
def buttons(call):
	if call.data=='CreateQr':
		app.answer_callback_query(call.id,show_alert=True, text=f'- اوكي ، ارسل النص او الرابط فقط .')
	if call.data=='v':
		app.answer_callback_query(call.id,text=f'- الإصدار 2.4.7 ✨ .')
		
app.infinity_polling(True)
