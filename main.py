import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# Bot Token
API_TOKEN = '8513575851:AAE40PrEkbs8cwijIKo9OmsvdBGHOv-zLts'
# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Cheksiz jarayonlarni (loop) boshqarish uchun lug'at
active_loops = {}
# Konstantalar - Xabarlar va Ma'lumotlar
LOVE_MESSAGES_LOOP = [
    "Seni sevaman ❤️",
    "Я тебя люблю 💖",
    "I love you 💌",
    "Seni seviyorum 💘"
]
ROMANTIC_PHRASES = [
    "Sen mening hayotimning nurisiz 🌹",
    "Sening kulgiching qalbimni eritadi 💖",
    "Sen bilan bo‘lish dunyoni yaxshilaydi 💌",
    "Har tonging men uchun quvonch 💘",
    "Senga qarash dunyoni unutsam ham qiladi 💝",
    "Sen mening qalbimning yulduzisiz ✨",
    "Har so‘zim senga bag‘ishlangan 💕",
    "Sen bilan vaqt o'tishi ertakday ⏳",
    "Senga bo‘lgan sevgim cheksiz 🌊",
    "Sening tabassuming meni baxtli qiladi 🌸"
]
POEMS = [
    "Sevgi – bu yurakning tilidir,\nSen bilan men baxtliman har da.",
    "Bir qarashing yetar meni hayratga soladi,\nSen mening hamrohimsan abadiyatga.",
    "Yuragimning har zarbasi senga atalgandir,\nSevgi bizni abadiyatga bog‘laydi."
]
MUSIC_LINKS = [
    ("Song 1 🎵", "https://example.com/song1.mp3"),
    ("Song 2 🎵", "https://example.com/song2.mp3"),
    ("Song 3 🎵", "https://example.com/song3.mp3"),
    ("Song 4 🎵", "https://example.com/song4.mp3"),
    ("Song 5 🎵", "https://example.com/song5.mp3"),
    ("Song 6 🎵", "https://example.com/song6.mp3"),
    ("Song 7 🎵", "https://example.com/song7.mp3"),
    ("Song 8 🎵", "https://example.com/song8.mp3"),
    ("Song 9 🎵", "https://example.com/song9.mp3"),
    ("Song 10 🎵", "https://example.com/song10.mp3"),
    ("Song 11 🎵", "https://example.com/song11.mp3"),
    ("Song 12 🎵", "https://example.com/song12.mp3"),
    ("Song 13 🎵", "https://example.com/song13.mp3"),
    ("Song 14 🎵", "https://example.com/song14.mp3"),
    ("Song 15 🎵", "https://example.com/song15.mp3")
]
# Asosiy tugmalar (Keyboard)
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("1️⃣ Xolisxon ❤️", callback_data="start_loop"),
        InlineKeyboardButton("2️⃣ Stop ❌", callback_data="stop_loop")
    )
    keyboard.add(
        InlineKeyboardButton("3️⃣ Romantik gaplar 💌", callback_data="romantic_text"),
        InlineKeyboardButton("4️⃣ Sher 📜", callback_data="poem")
    )
    keyboard.add(InlineKeyboardButton("5️⃣ Musiqa 🎵", callback_data="music"))
    return keyboard
# /start buyrug'i
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Xush kelibsiz! Quyidagi tugmalardan birini tanlang:", reply_markup=get_main_keyboard())
# Cheksiz loopni boshlash (Xolisxon ❤️)
@dp.callback_query_handler(lambda c: c.data == 'start_loop')
async def process_start_loop(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if user_id in active_loops and active_loops[user_id]:
        await bot.answer_callback_query(callback_query.id, "Jarayon allaqachon boshlangan!")
        return
    active_loops[user_id] = True
    await bot.answer_callback_query(callback_query.id, "Cheksiz sevgi boshlandi... ❤️")
    
    # Xabarlarni cheksiz yuborish
    while active_loops.get(user_id):
        msg = random.choice(LOVE_MESSAGES_LOOP)
        await bot.send_message(user_id, msg)
        await asyncio.sleep(3) # Har 3 soniyada bitta xabar
# Jarayonni to'xtatish (Stop ❌)
@dp.callback_query_handler(lambda c: c.data == 'stop_loop')
async def process_stop_loop(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    active_loops[user_id] = False
    await bot.answer_callback_query(callback_query.id, "Barcha jarayonlar to'xtatildi! ❌")
    await bot.send_message(user_id, "Jarayon to'xtatildi. 🛑", reply_markup=get_main_keyboard())
# Romantik gaplar
@dp.callback_query_handler(lambda c: c.data == 'romantic_text')
async def process_romantic_text(callback_query: types.CallbackQuery):
    phrase = random.choice(ROMANTIC_PHRASES)
    await bot.send_message(callback_query.from_user.id, phrase)
    await bot.answer_callback_query(callback_query.id)
# Sherlar
@dp.callback_query_handler(lambda c: c.data == 'poem')
async def process_poem(callback_query: types.CallbackQuery):
    poem = random.choice(POEMS)
    await bot.send_message(callback_query.from_user.id, poem)
    await bot.answer_callback_query(callback_query.id)
# Musiqa yuklash
@dp.callback_query_handler(lambda c: c.data == 'music')
async def process_music(callback_query: types.CallbackQuery):
    music_kb = InlineKeyboardMarkup(row_width=1)
    # Tasodifiy 5 ta musiqani ko'rsatish
    selected_songs = random.sample(MUSIC_LINKS, 5)
    for name, url in selected_songs:
        music_kb.add(InlineKeyboardButton(f"Yuklab olish: {name}", url=url))
    
    await bot.send_message(callback_query.from_user.id, "Tasodifiy 5 ta musiqa yuklash uchun tayyor:", reply_markup=music_kb)
    await bot.answer_callback_query(callback_query.id)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
