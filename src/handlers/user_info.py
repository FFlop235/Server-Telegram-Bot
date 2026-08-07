from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("my_info"))
async def get_my_info(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "без username"
    full_name = message.from_user.full_name or "без имени"
    
    response_text = (
        f"👤 Ваш Telegram ID: <code>{user_id}</code>\n"
        f"📝 Имя: {full_name}\n"
        f"🔗 Username: @{username}"
    )
    
    await message.answer(
        response_text,
        parse_mode="HTML"
    )