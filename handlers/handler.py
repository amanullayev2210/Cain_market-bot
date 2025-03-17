from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .markupButtons import product_keyboard
from .markupButtons import user_product_keyboard

root = Router()
# Admin menu ishlatish uchun bu yerga o'zingizni id ingzni qo'ying
admins_id = 1000247

@root.message(CommandStart())
async def SayHI(message: types.Message):
    if message.from_user.id == admins_id:
        await message.reply(f"Salom admin {message.from_user.full_name} Cain online marketga xush kelibsiz", reply_markup=product_keyboard)
    else:
        await message.reply(f"Salom {message.from_user.full_name} Cain online marketga xush kelibsiz", reply_markup=user_product_keyboard)

class Productt(StatesGroup):
    ism = State()
    narx = State()
    rasm = State()

def inline_buttons():
    file = open("handlers/db/products.txt", "r")
    piece_products = [product.replace("\n", "").split("|")[0] for product in file.readlines()]
    file.close()
    products = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=product, callback_data=product) for product in piece_products]
    ])
    return products

@root.message (F.text == "product_qoshish")
async def pr(message: types.Message, state: FSMContext):
    await state.set_state(Productt.ism)
    await message.reply("Salom bu yerga xush kelibsiz, productni ismini kiriitng", reply_markup=product_keyboard)

@root.message(Productt.ism, F.text)
async def narx_ol(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await state.set_state(Productt.narx)
    await message.reply("Tushunarli endi productni narxini yuboring")

@root.message(Productt.narx, F.text)
async def narx_ol(message: types.Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await state.set_state(Productt.rasm)
    await message.reply("Tushunarli endi productni rasmini yuboring")

@root.message(Productt.rasm, F.photo)
async def rasm_ol(message: types.Message, state: FSMContext):
    await state.update_data(rasm=message.photo[-1].file_id)
    data = await state.get_data()
    file = open("handlers/db/products.txt", "a")
    file.write(f"{data['ism']}|{data['narx']}|{data['rasm']}\n")
    file.close()
    await message.answer_photo(photo=data["rasm"], caption=f"{data['ism']}|{data['narx']}")


@root.message(F.text == "qoshgan_productlaringiz")
async def productlar(message: types.Message):
    await message.answer("Mana productlar", reply_markup=inline_buttons())


@root.message(Command("support"))
async def support(message: types.Message):
    await message.reply(f"{message.from_user.full_name} Agar qandaydir muammoga duch kelsangiz @Emore_6")


@root.message(F.text == "Xayr")
async def support(message: types.Message):
    await message.reply(f"{message.from_user.full_name} Xayr")


@root.message(F.text.lower() == "xayr")
async def support(message: types.Message):
    await message.reply(f"{message.from_user.full_name} xayr")


