import asyncio
from aiogram import Bot, Dispatcher, types
from config import TELEGRAM_TOKEN, CHAT_ID
from strategy import get_signals

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

async def send_signals():
    while True:
        signals = get_signals()  # Возвращает список сигналов по 7 парам
        for signal in signals:
            msg = f"{signal['pair']} | {signal['side']} | Entry: {signal['entry']} | Exit: {signal['exit']} | Leverage: {signal['leverage']}"
            await bot.send_message(chat_id=CHAT_ID, text=msg)
        await asyncio.sleep(3600)  # Повтор каждые 1 час

@dp.message()
async def start(message: types.Message):
    await message.answer("✅ Сигнальный бот запущен! Он будет присылать торговые сигналы по выбранным криптовалютам.")

async def main():
    asyncio.create_task(send_signals())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
