import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
import sys

from config import settings
from handlers import routes

logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
    level="DEBUG",
    colorize=True,
)
logger.add(
    "bot.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
    level="DEBUG",
    rotation="10 MB",
    retention="7 days",
)

async def main():
    logger.info("🚀 Запуск бота...")

    proxy_url = settings.PROXY_URL if settings.PROXY_URL else None
    session = AiohttpSession(proxy=proxy_url)

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=session
    )

    logger.info("✅ Прокси успешно подключен!" if proxy_url else "⚠️ Прокси не используется.")

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)
    dp.include_routers(*routes)

    logger.info("✅ Роутеры успешно подключены!")

    await asyncio.sleep(1)
    logger.info("🚀 Бот готов к работе!")

    try: 
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, handle_signals=False)
    except asyncio.CancelledError:
        pass
    finally:
        logger.info("🛑 Остановка бота...")
        # Остановка сервисов если потом будут
        logger.success("✅ Бот остановлен.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n👋Выход')