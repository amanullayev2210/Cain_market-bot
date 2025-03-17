from aiogram import Router, types
from aiogram import F
from aiogram.types import FSInputFile
from aiogram.types import CallbackQuery

from .inlineMarkup import all_products

# Bu yerga o'zingizni user ingizni qo'ying
seller_username = "@Emore_6"
roots = Router()

@roots.message(F.text.lower() == "products")
async def productlar(message: types.Message):
    await message.reply("Barcha productlar", reply_markup=all_products)

@roots.callback_query(F.data == "havo")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")   
    image = FSInputFile("handlers/imgs/havo_namlovchi.png")
    text = f"product: Havo namlovchi\nnarx: 20$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "qahva")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/qahva.png")
    text = f"product: Qahva\nnarx: 10$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "krasovka")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/krasovka.png")
    text = f"product: Krasovka\nnarx: 50$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "kondisoner")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/kondisoner.png")
    text = f"product: Kondisioner\nnarx: 1000$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "televizor")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/televizor.png")
    text = f"product: Televizor\nnarx: 1500$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "naushnik")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/naushnik.png")
    text = f"product: Naushnik\nnarx: 300$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "kolonka")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/kolonka_alisa.png")
    text = f"product: Kolonka Alisa\nnarx: 400$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "dazmol")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/dazmol.png")
    text = f"product: Dazmol\nnarx: 80$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "muzlatgich")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/muzlatgich.png")
    text = f"product: Muzlatgich\nnarx: 1000$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)

@roots.callback_query(F.data == "sumka")
async def product_detail(callback_data: types.callback_query):
    await callback_data.answer("")
    image = FSInputFile("handlers/imgs/sumka.png")
    text = f"product: Sumka\nnarx: 40$\n\nbuyurtma berish uchun: {seller_username}"
    await callback_data.message.answer_photo(photo=image, caption=text)
    

@roots.callback_query()
async def product_chiqar(callback: CallbackQuery):
   await callback.answer(callback.data)
   file = open("handlers/db/products.txt", "r")
   piece_products = [product for product in file.readlines()]
   file.close()
   for i in piece_products:
        product = i.replace("\n", "").split("|")
        if product[0] == callback.data:
            caption = f"product: {product[0]}\nnarx: {product[1]}\n\nbuyurtma berish uchun: {seller_username}"
            await callback.message.answer_photo(photo=product[2], caption=caption)


    
