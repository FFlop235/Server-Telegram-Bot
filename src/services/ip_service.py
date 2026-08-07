import socket
from loguru import logger
from typing import Optional

async def get_ip() -> Optional[str]:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        logger.info(f"IP получен: {ip}")
        return ip
    except Exception as e:
        logger.error(f"Ошибка получения IP: {e}")
        return None