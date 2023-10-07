import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import text
import keyboards
from config import *

scheduler = AsyncIOScheduler()
bot = Bot(TOKEN)
dp = Dispatcher()
activity_flag = False

async def Subscribe(chat):
    return await bot.send_message(chat, text.sms2, reply_markup=keyboards.sms2)
async def insta_wait(chat):
    return await bot.send_message(chat, text.sms3)


async def continuation(chat):
    return await bot.send_message(chat, text.sms4, reply_markup=keyboards.sms4)

async def day_2_dont_reply(chat):
    if activity_flag !=True:
        return await bot.send_message(chat, text.sms7, reply_markup=keyboards.sms7)
    else:
        return 0

async def day_3_dont_reply(chat):
    if activity_flag != True:
        return await bot.send_message(chat, text.sms10, reply_markup=keyboards.sms10)
    else:
        return 0

async def day_5_dont_reply(chat):
    if activity_flag != True:
        return await bot.send_message(chat, text.sms12, reply_markup=keyboards.sms12)
    else:
        return 0

async def day_7_dont_reply(chat):
    if activity_flag != True:
        return await bot.send_message(chat, text.sms14, reply_markup=keyboards.sms14)
    else:
        return 0



@dp.message(F.text == '/start')
async def start(msg: Message):
    hui = msg.from_user.first_name
    text.first_name = hui
    await msg.answer(text.greeting, reply_markup=keyboards.sms1)

@dp.callback_query(F.data == "member")
async def if_member(callback: types.CallbackQuery):
    scheduler.add_job(subscribe, trigger='date', run_date=datetime.now() + timedelta(seconds=1),
                      args=[callback.message.chat.id])
    scheduler.add_job(insta_wait, trigger='date', run_date=datetime.now() + timedelta(minutes=30),
                      args=[callback.message.chat.id])
    scheduler.add_job(continuation, trigger='date', run_date=datetime.now() + timedelta(hours=1),
                      args=[callback.message.chat.id])

    scheduler.add_job(day_2_dont_reply, trigger='date', run_date=datetime.now() + timedelta(days=1),
                      args=[callback.message.chat.id])
    scheduler.add_job(day_3_dont_reply, trigger='date', run_date=datetime.now() + timedelta(days=3),
                      args=[callback.message.chat.id])
    scheduler.add_job(day_5_dont_reply, trigger='date', run_date=datetime.now() + timedelta(days=5),
                      args=[callback.message.chat.id])
    scheduler.add_job(day_7_dont_reply, trigger='date', run_date=datetime.now() + timedelta(days=7),
                      args=[callback.message.chat.id])


@dp.callback_query(F.data == "iwant")
async def iwant(callback: types.CallbackQuery):
    await callback.message.answer(text.sms5, reply_markup=keyboards.sms5)

@dp.callback_query(F.data == "iwantRazbor")
async def iwant(callback: types.CallbackQuery):
    await callback.message.answer(text.sms6)

@dp.callback_query(F.data == "get_it")
async def iwant(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms6)

def set_flag ():
    global activity_flag
    activity_flag = True

@dp.callback_query(F.data == "marketing")
async def marketing(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms8_1, reply_markup=keyboards.sms8)
@dp.callback_query(F.data == "sells")
async def sells(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms8_2, reply_markup=keyboards.sms8)
@dp.callback_query(F.data == "control")
async def control(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms8_3, reply_markup=keyboards.sms8)
@dp.callback_query(F.data == "product")
async def product(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms8_4, reply_markup=keyboards.sms8)
@dp.callback_query(F.data == "admin")
async def admin(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms8_5, reply_markup=keyboards.sms8)

@dp.callback_query(F.data == "want_again")
async def want_again(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms11, reply_markup=keyboards.sms13)

@dp.callback_query(F.data == "interesting")
async def interesting(callback: types.CallbackQuery):
    set_flag()
    await callback.message.answer(text.sms13, reply_markup=keyboards.sms13)


@dp.message()
async def message_handler(msg: Message):
    await msg.answer(f"ляляляля")


async def main():
    scheduler.start()
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())

