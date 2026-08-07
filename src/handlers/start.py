from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет! Я — твой серверный бот 🤖\n\n"
        f"Я подключён к твоему серверу и могу:\n"
        f"• Проверять статус сервера\n"
        f"• Перезагружать его\n"
        f"• Показывать логи\n"
        f"• Выполнять команды\n\n"
        f"Чем могу помочь? 😊"
    )