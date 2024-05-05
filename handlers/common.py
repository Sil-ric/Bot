from aiogram import Router, types, F
from aiogram.filters.command import Command
import random
from keyboards.keyboards import keyboard
from utils.Fox_random import fox

router = Router()


@router.message(Command(commands=['start']))
@router.message(F.text.lower() == 'start')
async def start(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboard)


@router.message(Command(commands=['stop']))
@router.message(F.text.lower() == 'stop')
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'На этом мы закончим {message.chat.first_name}!')


@router.message(Command(commands=['info']))
@router.message(F.text.lower() == 'info')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'твоё число: {number}!')


@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('лови лису')
    await message.answer_photo(img_fox)
