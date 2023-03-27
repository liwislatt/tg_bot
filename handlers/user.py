from aiogram import types, Dispatcher
from keyboards import kb_user, kb_user2, kb_user3, kb_user4

async def command_start(message: types.Message):
    await message.answer('Выберите свою группу: ', reply_markup=kb_user)

async def command_help(message: types.Message):
    await message.answer('Список команд: \n'
                         '/first - Расписание для первой группы \n'
                         '/second - Расписание для второй группы \n'
                         '/third -Расписание для третьей группы \n')

async def command_first(message: types.Message):
    await message.answer('Выберите день недели: ', reply_markup=kb_user4)

async def command_second(message: types.Message):
    await message.answer('Выберите день недели: ', reply_markup=kb_user3)

async def command_third(message: types.Message):
    await message.answer('Выберите день недели: ', reply_markup=kb_user2)

async def messages(message: types.Message):
    await message.answer('Не понимаю ваших сообщений!')
    await message.delete()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_first, commands=['first'])
    dp.register_message_handler(command_second, commands=['second'])
    dp.register_message_handler(command_third, commands=['third'])
    dp.register_message_handler(messages)
