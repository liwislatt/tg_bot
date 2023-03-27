from aiogram.utils import executor

from imports import dp

async def on_startup(_):
    print('Online!')

from handlers import user

user.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)