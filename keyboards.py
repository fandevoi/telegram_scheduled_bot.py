from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove

sms1 = [
    [InlineKeyboardButton(text="Я подписан(а)👋", callback_data="member"),
     InlineKeyboardButton(text="ПОДПИСАТЬСЯ 🚀", url="https://t.me/sortceva")]
]
sms1 = InlineKeyboardMarkup(inline_keyboard=sms1)

sms2 = [
    [InlineKeyboardButton(text="Доступ открыт 🚀", url="https://www.youtube.com/")]
]
sms2 = InlineKeyboardMarkup(inline_keyboard=sms2)

sms4 = [
    [InlineKeyboardButton(text="КОНЕЧНО ХОЧУ🤩", callback_data="iwant")]
]
sms4 = InlineKeyboardMarkup(inline_keyboard=sms4)

sms5 = [
    [InlineKeyboardButton(text="Да, давайте 👍", callback_data="get_it")]
]
sms5 = InlineKeyboardMarkup(inline_keyboard=sms5)

sms7 = [
    [InlineKeyboardButton(text="Маркетинг", callback_data="marketing"),
     InlineKeyboardButton(text="Продажи", callback_data="sells")],

    [InlineKeyboardButton(text="Управление", callback_data="control"),
     InlineKeyboardButton(text="Продукт", callback_data="product")],

    [InlineKeyboardButton(text="Как выстроить работу с администратором", callback_data="admin")]
]
sms7 = InlineKeyboardMarkup(inline_keyboard=sms7)

sms8 = [
    [InlineKeyboardButton(text="ХОЧУ РАЗБОР", callback_data="iwantRazbor")]
]
sms8 = InlineKeyboardMarkup(inline_keyboard=sms8)

sms10 = [
    [InlineKeyboardButton(text=" ХОЧУ🚀", callback_data="want_again")]
]
sms10 = InlineKeyboardMarkup(inline_keyboard=sms10)

sms11 = [
    [InlineKeyboardButton(text="ХОЧУ🚀", url="https://docs.google.com/forms/d"
                                            "/1ksqFxRDxqhnwMoUN2A8QfaP7AsrV5sAtdvZjSp6U1Oc/edit")]
]
sms11 = InlineKeyboardMarkup(inline_keyboard=sms11)

sms12 = [
    [InlineKeyboardButton(text="Ого, интересно", callback_data="interesting")]
]
sms12 = InlineKeyboardMarkup(inline_keyboard=sms12)

sms13 = [
    [InlineKeyboardButton(text="Анкета", url="https://docs.google.com/forms/d"
                                             "/1ksqFxRDxqhnwMoUN2A8QfaP7AsrV5sAtdvZjSp6U1Oc/edit")]
]
sms13 = InlineKeyboardMarkup(inline_keyboard=sms13)

sms14 = [
    [InlineKeyboardButton(text="ЗАПИСАТЬСЯ НА РАЗБОР", url="https://docs.google.com/forms/d"
                                                           "/1ksqFxRDxqhnwMoUN2A8QfaP7AsrV5sAtdvZjSp6U1Oc/edit")]
]
sms14 = InlineKeyboardMarkup(inline_keyboard=sms14)
