from aiogram import types

button1 = types.KeyboardButton(text='start')
button2 = types.KeyboardButton(text='stop')
button3 = types.KeyboardButton(text='info')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='work')

keyboard1 = [
    [button1, button5],
    [button3, button4],
    [button2]
]

keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
