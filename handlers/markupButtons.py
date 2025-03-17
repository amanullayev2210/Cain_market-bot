from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


product_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="products")],
        [KeyboardButton(text="product_qoshish"), KeyboardButton(text="qoshgan_productlaringiz")]

],
                 resize_keyboard=True)


user_product_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="products")]
        
],
                 resize_keyboard=True)

