from aiogram import Router, types
from aiogram.filters import CommandStart
from config import settings

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    if message.from_user.id != settings.ADMIN_ID:
        await message.answer("❌ У вас нет доступа к этому боту.")
        return
    await message.answer(
        f"Привет! Я — твой серверный бот 🤖\n\n"
        f"Я подключён к твоему серверу и могу:\n"
        f"• Проверять статус сервера\n"
        f"• Перезагружать его\n"
        f"• Показывать логи\n"
        f"• Выполнять команды\n\n"
        f"Чем могу помочь? 😊"
    )