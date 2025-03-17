from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


all_products = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="havo namlovchi", callback_data="havo"),    InlineKeyboardButton(text="qahva", callback_data="qahva")],
    [InlineKeyboardButton(text="krasovka", callback_data="krasovka"),      InlineKeyboardButton(text="kondisoner", callback_data="kondisoner")],
    [InlineKeyboardButton(text="televizor", callback_data="televizor"),    InlineKeyboardButton(text="naushnik", callback_data="naushnik")],
    [InlineKeyboardButton(text="kolonka_alisa", callback_data="kolonka"),  InlineKeyboardButton(text="dazmol", callback_data="dazmol")],
    [InlineKeyboardButton(text="muzlatgich", callback_data="muzlatgich"),  InlineKeyboardButton(text="sumka", callback_data="sumka")]
])

