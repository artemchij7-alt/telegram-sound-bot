import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = 8576592069:AAF_vXcbZLH5nyLxEKv1l87rn7pSvWUOG6E

bot = Bot(token=TOKEN)
dp = Dispatcher()

ACCESS_CODE = "sound123"
SOUND_FILE = "sound.mp3"

@dp.message(commands=["start"])
async def start(message: types.Message):
    args = message.text.split()

    if len(args) == 2 and args[1] == ACCESS_CODE:
        await bot.send_audio(
            chat_id=message.chat.id,
            audio=types.FSInputFile(SOUND_FILE),
            caption="🎧 Ваш звук"
        )
    else:
        await message.answer("❌ Неверный QR-код")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
