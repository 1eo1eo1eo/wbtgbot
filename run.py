import asyncio
import logging
from mainfiles.tgbotfiles.handlers import router
from mainfiles.tgbotfiles.modules import dp, bot
from mainfiles.tgbotfiles.callbacks import notify_new_products, notify_discounted_products

async def main():
    dp.include_router(router)
    notify_new_task = asyncio.create_task(notify_new_products(dp))
    notify_discount_task = asyncio.create_task(notify_discounted_products(dp))
    await dp.start_polling(bot)
    await notify_new_task
    await notify_discount_task

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
