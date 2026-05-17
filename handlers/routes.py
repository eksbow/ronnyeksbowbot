from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,
    InlineKeyboardMarkup, InlineKeyboardButton
                           )
from aiogram.fsm.context import FSMContext
from pyexpat.errors import messages

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name} , вся интересующая тебя инфа ниже \n\n  ", reply_markup=get_main_inline_keyboard())

'''@router.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "/start - запуск бота",
        reply_markup = get_main_reply_keyboard())
    
    
@router.message(F.photo)
async def photo(message: Message):
    price_id = message.photo[-1]
    await message.answer(f'{price_id} ')


def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="СПисок команд")],
            [KeyboardButton(text="Прайс"),KeyboardButton(text="Информация")]

        ], resize_keyboard=True

    )
    return keyboard'''

def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Инфа',callback_data='inf'), InlineKeyboardButton(text='Прайс',callback_data='prc') ],
            [InlineKeyboardButton(text='Как получить скидку до 70%',url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
        ]
    )
    return keyboard
@router.callback_query(lambda c: c.data == 'inf')
async def inf_more(callback):
    await callback.message.answer("бем бем\n\nбам бам")
    await callback.answer()

@router.callback_query(lambda c: c.data == 'prc')
async def inf_more(callback):
    await callback.message.answer_photo(photo='AgACAgIAAxkBAANIagnOS72NdaZpDNv1K5_JwClhiXYAArYcaxsnMVBIBVSK0w8LRqoBAAMCAAN4AAM7BA')







