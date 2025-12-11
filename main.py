import asyncio
from aiogram import Bot, Dispatcher, types
from config import TELEGRAM_TOKEN, CHAT_ID
from strategy import get_signals

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

async def send_signals():
    while True:
        signals = get_signals()
        for signal in signals:
            msg = f"{signal['pair']} | {signal['side']} | Entry: {signal['entry']:.2f} | Exit: {signal['exit']:.2f} | Leverage: {signal['leverage']}"
            await bot.send_message(chat_id=CHAT_ID, text=msg)
        await asyncio.sleep(3600)  # раз в час

@dp.message()
async def start(message: types.Message):
    await message.answer("✅ Сигнальный бот запущен! Он будет присылать торговые сигналы.")

async def main():
    asyncio.create_task(send_signals())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
