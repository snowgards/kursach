from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

#keyboard num_1
markup = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
start = KeyboardButton(text = 'Заказать напиток')
markup.add(start)

#keyboard num_2
markup_1 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

item1 = KeyboardButton(text = 'ул. Ломоносова 9М')
item2 = KeyboardButton(text = 'пр-кт Кронверкский 49')
item3 = KeyboardButton(text = 'ул. Чайковского 11/2')
item4 = KeyboardButton(text = 'Вернуться в начало')

markup_1.add(item1, item2).add(item3, item4)

#keyboard num_3
markup_2 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

latte = KeyboardButton(text = 'Латте')
raf = KeyboardButton(text = 'Раф')
capuchino = KeyboardButton(text = 'Капучино')
kakao = KeyboardButton(text = 'Какао')
tea = KeyboardButton(text = 'Горячий шоколад')
americano = KeyboardButton(text = 'Американо')
new = KeyboardButton(text = 'Вернуться в начало')

markup_2.add(latte, raf).add(capuchino, kakao).add(tea, americano).add(new)

#keyboard num_4
markup_3 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

num_1 = KeyboardButton(text = 'Латте 250 мл')
num_2 = KeyboardButton(text = 'Латте 380 мл')
num_3 = KeyboardButton(text = 'Латте 510 мл')
num_4 = KeyboardButton(text = 'Вернуться в начало')

markup_3.add(num_1, num_2).add(num_3, num_4)

#keyboard num_5

markup_4 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

num_1 = KeyboardButton(text = 'Раф 250 мл')
num_2 = KeyboardButton(text = 'Раф 380 мл')
num_3 = KeyboardButton(text = 'Раф 510 мл')
num_4 = KeyboardButton(text = 'Вернуться в начало')

markup_4.add(num_1, num_2).add(num_3, num_4)

#keyboard num_6

markup_5 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

num_1 = KeyboardButton(text = 'Капучино 250 мл')
num_2 = KeyboardButton(text = 'Капучино 380 мл')
num_3 = KeyboardButton(text = 'Капучино 510 мл')
num_4 = KeyboardButton(text = 'Вернуться в начало')

markup_5.add(num_1, num_2).add(num_3, num_4)

#keyboard num_7

markup_6 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

num_1 = KeyboardButton(text = 'Какао 250 мл')
num_2 = KeyboardButton(text = 'Какао 380 мл')
num_3 = KeyboardButton(text = 'Какао 510 мл')
num_4 = KeyboardButton(text = 'Вернуться в начало')

markup_6.add(num_1, num_2).add(num_3, num_4)

#keyboard num_8

markup_7 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

num_1 = KeyboardButton(text = 'Горячий шоколад 250 мл')
num_2 = KeyboardButton(text = 'Горячий шоколад 380 мл')
num_3 = KeyboardButton(text = 'Горячий шоколад 510 мл')
num_4 = KeyboardButton(text = 'Вернуться в начало')

markup_7.add(num_1, num_2).add(num_3, num_4)

#keyboard num_9

markup_8 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

num_1 = KeyboardButton(text = 'Американо 250 мл')
num_2 = KeyboardButton(text = 'Американо 380 мл')
num_3 = KeyboardButton(text = 'Американо 510 мл')
num_4 = KeyboardButton(text = 'Вернуться в начало')

markup_8.add(num_1, num_2).add(num_3, num_4)

#keyboard num_10

markup_9 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

number_1 = KeyboardButton(text = 'Оплата')
number_2 = KeyboardButton(text = 'Вернуться в начало')

markup_9.add(number_1).add(number_2)


#keyboard num_11

def upload() -> InlineKeyboardMarkup:
    update = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Обновить статус заказа', callback_data='update_info')]
    ])
    return update

#keyboard num 12
cancel = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

cup = KeyboardButton(text = 'Вернуться в начало')

cancel.add(cup)

#keyboard num 13

start = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

st = KeyboardButton(text = 'Старт')

start.add(st)

#keyboard adm_1

kb_1 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

adm = KeyboardButton(text = 'За работу!')

kb_1.add(adm)

#keyboard 2
list_order = CallbackData('order', 'id', 'action')

def admin_start_ikb() -> InlineKeyboardMarkup:
    ikb_1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Посмотреть все заказы', callback_data='get_all_order')],
        [InlineKeyboardButton('Закончить прием заказов', callback_data='complete_work')]
    ])
    return ikb_1


def get_edit(user_id: int) -> InlineKeyboardMarkup:
    ikb_2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Изменить статус на "Заказ в обработке"', callback_data=list_order.new(user_id, 'edit'))],
        [InlineKeyboardButton('Изменить статус на "Заказ готов"', callback_data=list_order.new(user_id, 'edit_1'))],
        [InlineKeyboardButton('Изменить статус на "Не прошла оплата"', callback_data=list_order.new(user_id, 'edit_2'))],
        [InlineKeyboardButton('Изменить статус на "Данное фото не является чеком"', callback_data=list_order.new(user_id, 'edit_3'))],
        [InlineKeyboardButton('Удалить заказ из "Активные заказы"', callback_data=list_order.new(user_id, 'delete'))]
    ])
    return ikb_2


#keyboard adm_3
ekb_1 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

adm = KeyboardButton(text = 'Заказ в обработке')
adm_1 = KeyboardButton(text = 'Отменить изменение статус')

ekb_1.add(adm).add(adm_1)

#keyboard adm_4
ekb_2 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

adm = KeyboardButton(text = 'Заказ готов')
adm_1 = KeyboardButton(text = 'Отменить изменение статус')

ekb_2.add(adm).add(adm_1)

#keyboard adm_5
ekb_3 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

adm = KeyboardButton(text = 'Не прошла оплата')
adm_1 = KeyboardButton(text = 'Отменить изменение статуса')

ekb_3.add(adm).add(adm_1)

#keyboard adm_6
ekb_4 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

adm = KeyboardButton(text = 'Данное фото не является чеком')
adm_1 = KeyboardButton(text = 'Отменить изменение статус')

ekb_4.add(adm).add(adm_1)