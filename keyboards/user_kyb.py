from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from imports import dp

kb_user = InlineKeyboardMarkup(row_width=1)
b3 = InlineKeyboardButton(text='1-22', callback_data="first")
b2 = InlineKeyboardButton(text='2-22', callback_data="second")
b1 = InlineKeyboardButton(text='3-22', callback_data="mine")
kb_user.add(b3, b2, b1)

@dp.callback_query_handler(text="mine")
async def gr3(callback: types.CallbackQuery):
    await callback.message.answer('Выберите день недели: ', reply_markup=kb_user2)
    await callback.answer()

@dp.callback_query_handler(text="second")
async def gr2(callback: types.CallbackQuery):
    await callback.message.answer('Выберите день недели: ', reply_markup=kb_user3)
    await callback.answer()

@dp.callback_query_handler(text="first")
async def gr1(callback: types.CallbackQuery):
    await callback.message.answer('Выберите день недели: ', reply_markup=kb_user4)
    await callback.answer()

kb_user2 = InlineKeyboardMarkup(row_width=1)
b4 = InlineKeyboardButton(text="Понедельник", callback_data="Monday")
b5 = InlineKeyboardButton(text="Вторник", callback_data="Tuesday")
b6 = InlineKeyboardButton(text="Среда", callback_data="Wednesday")
b7 = InlineKeyboardButton(text="Четверг", callback_data="Thursday")
b8 = InlineKeyboardButton(text="Пятница", callback_data="Friday")
b9 = InlineKeyboardButton(text="Суббота", callback_data="Saturday")

kb_user2.add(b4, b5, b6, b7, b8, b9)

@dp.callback_query_handler(text='Monday')
async def pn(callback: types.CallbackQuery):
    await callback.message.answer('Понедельник: \n'
                                '\n'
                                '9:30 - 10:50 : Web Application Development (Java) 2/128 \n'
                                '\n'
                                '11:00 - 12:20 : Web Application Development (Java) 1/357 \n'
                                '\n'
                                '14:30 - 15:50 : Physical Culture and sports' )
    await callback.answer()

@dp.callback_query_handler(text='Tuesday')
async def vt(callback: types.CallbackQuery):
    await callback.message.answer('Вторник: \n'
                                '\n'
                                'У вас нет пар, вам повезло :) ')
    await callback.answer()

@dp.callback_query_handler(text='Wednesday')
async def sr(callback: types.CallbackQuery):
    await callback.message.answer('Среда: \n'
                                '\n'
                                '9:30 - 10:50 : (Числ) Manas Study 2/128 \n'
                                '\n'
                                '11:00 - 12:20 : (Числ) Basics of Team and Group Communication 1/264 \n'
                                '\n'
                                '13:00 - 14:20 : Physical culture and sports')
    await callback.answer()

@dp.callback_query_handler(text='Thursday')
async def cht(callback: types.CallbackQuery):
    await callback.message.answer('Четверг: \n'
                                '\n'
                                '8:00-9:20 : Project works 1 1/355 \n'
                                '\n'
                                '9:30-10:50 : Project works 1 1/355 \n'
                                '\n'
                                '11:00-12:20 :  Kyrgyz Language (basics) 2 and Literature 2/505 \n'
                                '\n'
                                '13:00-14:20 :  Web Application Development (C#) 2/228')
    await callback.answer()

@dp.callback_query_handler(text='Friday')
async def pt(callback: types.CallbackQuery):
    await callback.message.answer('Пятница: \n'
                                '\n'
                                '8:00-9:20 : Web Application Development (C#) 1/357 \n'
                                '\n'
                                '9:30-10:50 : (Знам) Kyrgyz Language (basics) 2 and Literature 2/505 \n'
                                '/ (Числ) Manas Study 1/412 \n'
                                '\n'
                                '11:00-12:20: Function-Oriented (Structured) Design / Algorithmic Language 1 1/304 \n'
                                '\n'
                                '13:00-14:20: Function-Oriented (Structured) Design / Algorithmic Language 1 1/304')
    await callback.answer()

@dp.callback_query_handler(text='Saturday')
async def sb(callback: types.CallbackQuery):
    await callback.message.answer('Суббота: \n'
                                '\n'
                                '13:00 - 14:20 :  Basics of Team and Group Communication 1/351 \n'
                                '\n'
                                '14:30 - 15:50 :  Structures and Algorithms for the Data Transaction Processing 1/304 \n'
                                '\n'
                                '16:00 - 17:20 :  Structures and Algorithms for the Data Transaction Processing 1/304 \n')
    await callback.answer()

kb_user3 = InlineKeyboardMarkup(row_width=1)
b42 = InlineKeyboardButton(text="Понедельник", callback_data="Monday2")
b52 = InlineKeyboardButton(text="Вторник", callback_data="Tuesday2")
b62 = InlineKeyboardButton(text="Среда", callback_data="Wednesday2")
b72 = InlineKeyboardButton(text="Четверг", callback_data="Thursday2")
b82 = InlineKeyboardButton(text="Пятница", callback_data="Friday2")
b92 = InlineKeyboardButton(text="Суббота", callback_data="Saturday2")

kb_user3.add(b42, b52, b62, b72, b82, b92)

@dp.callback_query_handler(text="Monday2")
async def pn2(callback: types.CallbackQuery):
    await callback.message.answer('Понедельник: \n'
                                  '\n'
                                  '8:00 - 9:20 : Web Application Development (Java) 2/226 \n'
                                  '\n'
                                  '9:30 - 10:50 : Web Application Development (Java) 2/128 \n'
                                  '\n'
                                  '14:30 - 15:50 : Physical culture and sports ')
    await callback.answer()

@dp.callback_query_handler(text="Tuesday2")
async def vt2(callback: types.CallbackQuery):
    await callback.message.answer('Вторник: \n'
                                  '\n'
                                  'У вас нет пар на сегодня, вам повезло!')
    await callback.answer()

@dp.callback_query_handler(text="Wednesday2")
async def sr2(callnack: types.CallbackQuery):
    await callnack.message.answer('Среда: \n'
                                  '\n'
                                  '9:30 - 10:50 : (Числ) Manas Study 2/128 \n'
                                  '\n'
                                  '11:00 - 12:20 : (Числ) Manas Study 1/158 \n'
                                  '\n'
                                  '13:00 - 14:20 : Physical culture and sports \n'
                                  '\n'
                                  '14:30 - 15:50 : Project works 5/36\n'
                                  '\n'
                                  '16:00 - 17:20 : Project works 5/36')

@dp.callback_query_handler(text="Thursday2")
async def cht2(callback: types.CallbackQuery):
    await callback.message.answer('Четверг: \n'
                                  '\n'
                                '11:00 - 12:20 : Kyrgyz language and Literature 2/505 || 2/517 \n'
                                  '\n'
                                '13:00 - 14:20 : Function-Oriented (Structured) Design / Algorithmic Language 1 1/304\n'
                                  '\n'
                                '14:30 - 15:50 : Function-Oriented (Structured) Design / Algorithmic Language 1 1/304')

@dp.callback_query_handler(text="Friday2")
async def pt2(callback: types.CallbackQuery):
    await callback.message.answer('Пятница: \n'
                                  '\n'
                                  '8:00 - 9:20 : Web Application Development (C#) \n'
                                  '\n'
                                  '9:30 - 10:50 : Kyrgyz language and Literature 2/505 || 2/615')

@dp.callback_query_handler(text='Saturday2')
async def sb2(callback: types.CallbackQuery):
    await callback.message.answer('Суббота: \n'
                                  '\n'
                                  '8:00 - 9:20 : Basics of Team and Group Communication 1/351 \n'
                                  '\n'
                                  '9:30 - 10:50 : Basics of Team and Group Communication 1/351 \n'
                                  '\n'
                                  '11:00 - 12:20 : Structures and Algorithms for the Data Transaction Processing 1/304 \n'
                                  '\n'
                                  '13:00 - 14:20 : Structures and Algorithms for the Data Transaction Processing 1/304')

kb_user4 = InlineKeyboardMarkup(row_width=1)
b41 = InlineKeyboardButton(text="Понедельник", callback_data="Monday1")
b51 = InlineKeyboardButton(text="Вторник", callback_data="Tuesday1")
b61 = InlineKeyboardButton(text="Среда", callback_data="Wednesday1")
b71 = InlineKeyboardButton(text="Четверг", callback_data="Thursday1")
b81 = InlineKeyboardButton(text="Пятница", callback_data="Friday1")
b91 = InlineKeyboardButton(text="Суббота", callback_data="Saturday1")

kb_user4.add(b41, b51, b61, b71, b81, b91)

@dp.callback_query_handler(text='Monday1')
async def pn1(callback: types.CallbackQuery):
    await callback.message.answer('Понедельник: \n'
                                  '\n'
                                '9:30 - 10:50 : Web Application Development (Java) 2/128 \n'
                                  '\n'
                                '11:00 - 12:20 : Web Application Development (Java) 1/357 \n'
                                  '\n'
                                '14:30 - 15:50 : Physical Culture and sports' )

@dp.callback_query_handler(text='Tuesday1')
async def __(callback: types.CallbackQuery):
    await callback.message.answer('Вторник: \n'
                                  '\n'
                                  '8:00 - 9:20 : Function-Oriented (Structured) Design / Algorithmic Language 1 1/304 \n'
                                  '\n'
                                  '9:30 - 10:50 : Function-Oriented (Structured) Design / Algorithmic Language 1 1/304 \n'
                                  '\n'
                                  '11:00 - 12:20 : Project works 2/430 \n'
                                  '\n'
                                  '13:00 - 14:20 : Project works 2/430')

@dp.callback_query_handler(text='Wednesday1')
async def __(callback: types.CallbackQuery):
    await callback.message.answer('Среда: \n'
                                  '\n'
                                  '9:30 - 10:50 : (Числ) Manas Study 2/128 \n'
                                  '\n'
                                  '11:00 - 12:20 : (Числ) Manas Study 1/158 \n'
                                  '\n'
                                  '13:00 - 14:20 : Physical culture and sports')

@dp.callback_query_handler(text='Thursday1')
async def __(callback: types.CallbackQuery):
    await callback.message.answer('Четверг: \n'
                                  '\n'
                                  '8:00 - 9:20 : Basics of Team and Group Communication 1/351 \n'
                                  '\n'
                                  '11:00 - 12:20 : Kyrgyz language and Literature 2/505 || 2/607 \n'
                                  '\n'
                                  '13:00 - 14:20 : Web Application Development (C#) 2/228')

@dp.callback_query_handler(text='Friday1')
async def __(callback: types.CallbackQuery):
    await callback.message.answer('Пятница: \n'
                                  '\n'
                                  '8:00 - 9:20 : Web Application Development (C#) 1/357 \n'
                                  '\n'
                                  '9:30 - 10:50 : Kyrgyz language and Literature 2/505 || 2/517')

@dp.callback_query_handler(text='Saturday1')
async def __(callback: types.CallbackQuery):
    await callback.message.answer('Суббота: \n'
                                  '\n'
                                  '8:00 - 9:20 : Structures and Algorithms for the Data Transaction Processing 1/304 \n'
                                  '\n'
                                  '9:30 - 10:50 : Structures and Algorithms for the Data Transaction Processing 1/304 \n'
                                  '\n'
                                  '11:00 - 12:20 : Basics of Team and Group Communication 1/351 ')
