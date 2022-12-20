import logging
from database import db_connect, get_all_order, create_profile, edit_profile, delete_order, get_status_order, edit_status_order

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State


from keyboards import markup, markup_1, markup_2, markup_3, markup_4, markup_5, markup_6, markup_7, markup_8, markup_9, kb_1, admin_start_ikb, upload, get_edit, list_order, ekb_4, ekb_3, ekb_1, ekb_2, cancel, start

API_TOKEN = '5984456758:AAFovlxlzTPjI8ZgbtmSFxABySxBnrElSP0'

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage() #memory for state machine
bot = Bot(token = API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage = MemoryStorage())

HELP_COMMAND = """
/help - список команд
/start - запуск бота
/menu - список напитков
/info - информация о боте"""

class info_order(StatesGroup): #class for state machine 

    user = State()
    corps = State()
    product = State()
    product_order = State()
    verifi = State()
    photo = State()

class edit_order(StatesGroup):
    edit = State()


#function blocks access for other users, this is access for only admin 
def auth(func):
    async def wrapper(message):
        if message ['from']['id'] != 441395036:
            return await message.reply('Sorry, are you not admin', reply = False)
        
        return await func(message)

    return wrapper

#connect database
async def con(_):
    await db_connect()
    print('Подключение к БД прошло успешно')


#cmd for admin    
@dp.message_handler(commands=['admin'])
@auth
async def adm_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = f"Привет, <b>{message.from_user.first_name}</b>!\n\nЧтобы начать работу, нажми на кнопку 🙈", parse_mode='html', reply_markup = kb_1)

@dp.message_handler(Text(equals='За работу!'))
async def adm1_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = 'Чем ты хочешь заняться?', reply_markup = admin_start_ikb())

@dp.callback_query_handler(text='get_all_order')
async def cd_get_all_order(callback: types.callback_query):   
    orders = await get_all_order()
    if not orders:
        return await callback.message.answer('Заказов нет.')

    await show_all_order(callback, orders)
    await callback.answer()

@dp.callback_query_handler(text='complete_work')
async def cd_get_all_order(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = 'Хорошего отдыха!\n\nЧтобы вернуться к работе, введи команду /admin')

#delete order 
@dp.callback_query_handler(list_order.filter(action='delete'))
async def now_delete_order(callback: types.CallbackQuery, callback_data: dict):
    await delete_order(callback_data['id'])
    await callback.message.reply('Заказ выполнен!\nЧтобы вернуться к заказам, нажми на кнопку "Посмотреть все заказы"', reply_markup = admin_start_ikb())
    await callback.answer()


#edit order
@dp.callback_query_handler(list_order.filter(action='edit'))
async def now_edit_order(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.message.answer('Подтверди изменение статуса', reply_markup=ekb_1)
    await edit_order.edit.set()

    async with state.proxy() as data:
        data['verifi'] = callback_data['id']

    await callback.answer()

@dp.message_handler(Text(equals='Заказ в обработке'), state=edit_order.edit)
async def load_edit(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        await edit_status_order(data['verifi'], message.text)
    
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Статус обновлен\nЧтобы вернуться к заказам, нажми на кнопку.', reply_markup=admin_start_ikb())


#edit_1 order
@dp.callback_query_handler(list_order.filter(action='edit_1'))
async def now_edit_order(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.message.answer('Подтверди изменение статуса', reply_markup=ekb_2)
    await edit_order.edit.set()

    async with state.proxy() as data:
        data['verifi'] = callback_data['id']
        
    await callback.answer()

@dp.message_handler(Text(equals='Заказ готов'), state=edit_order.edit)
async def load_edit(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        await edit_status_order(data['verifi'], message.text)
    
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Статус обновлен\nЧтобы вернуться к заказам, нажми на кнопку.', reply_markup=admin_start_ikb())


#edit_2 order
@dp.callback_query_handler(list_order.filter(action='edit_2'))
async def now_edit_order(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.message.answer('Подтверди изменение статуса', reply_markup=ekb_3)
    await edit_order.edit.set()

    async with state.proxy() as data:
        data['verifi'] = callback_data['id']
        
    await callback.answer()

@dp.message_handler(Text(equals='Не прошла оплата'), state=edit_order.edit)
async def load_edit(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        await edit_status_order(data['verifi'], message.text)
    
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Статус обновлен\nЧтобы вернуться к заказам, нажми на кнопку.', reply_markup=admin_start_ikb())


#edit_3 order
@dp.callback_query_handler(list_order.filter(action='edit_3'))
async def now_edit_order(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback.message.answer('Подтверди изменение статуса', reply_markup=ekb_4)
    await edit_order.edit.set()

    async with state.proxy() as data:
        data['verifi'] = callback_data['id']
        
    await callback.answer()

@dp.message_handler(Text(equals='Данное фото не является чеком'), state=edit_order.edit)
async def load_edit(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        await edit_status_order(data['verifi'], message.text)
    
    await state.finish()
    await bot.send_message(chat_id=message.from_user.id, text='Статус обновлен\nЧтобы вернуться к заказам, нажми на кнопку.', reply_markup=admin_start_ikb())


#show all order gui
async def show_all_order(callback: types.CallbackQuery, orders: list):
    for order in orders:
        await bot.send_photo(chat_id=callback.message.chat.id,
                            photo=order[6],
                            caption=f'ID: <b>{order[0]}</b>\nИСУ: <b>{order[1]}</b>\nКорпус: <b>{order[2]}</b>\nЗаказ: <b>{order[4]}</b>\nСтатус: <b>{order[5]}</b>',
                            parse_mode='HTML', 
                            reply_markup=get_edit(order[0]))

@dp.callback_query_handler(text='complete_work')
async def cd_complete_work(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = 'Хорошая работа!', reply_markup = kb_1)


#cmd for users 
@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = HELP_COMMAND, reply_markup=start)
    await message.delete()

@dp.message_handler(commands=['info'])
async def info_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = 'Какой-то текст о боте', reply_markup=start)

@dp.message_handler(commands=['menu'])
async def menu_message(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo = 'https://sun9-26.vkuserphoto.ru/impg/5UkFkOxfaj2PONYW0KIjAvy4dNQawFZBKFHexw/G2qz-qXsgyo.jpg?size=1584x2160&quality=95&sign=a408d02b13b53dec28cc6f6387f4f875&type=album', caption='Выбирай напиток и не выбирай вообще!', reply_markup=start)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                            text = f"Привет, <b>{message.from_user.first_name}</b>!\n\nЯ — бот, который поможет тебе заказать напиток в одном из корпусов Университета ИТМО.\n\nЧтобы сделать заказ, нажми на кнопку 🙈",
                            parse_mode='html', reply_markup=markup)
    await create_profile(user_id=message.from_user.id)


@dp.message_handler(Text(equals='Старт'))
async def start_message(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                            text = f"Привет, <b>{message.from_user.first_name}</b>!\n\nЯ — бот, который поможет тебе заказать напиток в одном из корпусов Университета ИТМО.\n\nЧтобы сделать заказ, нажми на кнопку 🙈",
                            parse_mode='html', reply_markup=markup)
    await create_profile(user_id=message.from_user.id)

#show status for user
async def show_status(callback: types.CallbackQuery, orders: list):
        await bot.send_message(chat_id=callback.message.chat.id,
                                text=f'Информация о заказе\n\nВаш ID: <b>{orders[0]}</b>\nКорпус: <b>{orders[1]}</b>\nВаш заказ: <b>{orders[2]}</b>\nСтатус заказа: <b>{orders[3]}</b>',
                                parse_mode='HTML', reply_markup = upload())


#return to start
@dp.message_handler(Text(equals='Вернуться в начало'), state='*')
async def return_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, 
                            text = f"Привет, <b>{message.from_user.first_name}</b>!\n\nЯ — бот, который поможет тебе заказать напиток в одном из корпусов Университета ИТМО.\n\nЧтобы сделать заказ, нажми на кнопку 🙈",
                            parse_mode='html', reply_markup=markup)
    if state is None:
        return
    
    await state.finish()
    await message.delete()

@dp.message_handler(Text(equals='Отменить изменение статуса'), state='*')
async def return_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, 
                            text = f"Статус заказа не изменен",
                            parse_mode='html', reply_markup=admin_start_ikb())
    if state is None:
        return
    
    await state.finish()
    await message.delete()


@dp.message_handler(Text(equals='Заказать напиток'))
async def start_order(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                            text = 'Для начала введи свой номер ИСУ 🙃', reply_markup=cancel)
    await info_order.user.set()

@dp.message_handler(lambda message: not message.text.isdigit() or int(message.text) > 355000, state=info_order.user)
async def check_isu(message: types.Message):
    await message.reply('Это не похоже на номер ИСУ!')


@dp.message_handler(content_types=['text'], state=info_order.user)
async def next_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери корпус:', reply_markup = markup_1) 
    async with state.proxy() as data:
        data['user'] = message.text
    await info_order.next()


#corps
@dp.message_handler(Text(equals='ул. Ломоносова 9М'), state=info_order.corps)
async def choice_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери напиток:', reply_markup = markup_2)
    async with state.proxy() as data:
        data['corps'] = message.text
    await info_order.next()
    
@dp.message_handler(Text(equals='пр-кт Кронверкский 49'), state=info_order.corps)
async def choice_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери напиток:', reply_markup = markup_2)
    async with state.proxy() as data:
        data['corps'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='ул. Чайковского 11/2'), state=info_order.corps)
async def choice_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери напиток:', reply_markup = markup_2)
    async with state.proxy() as data:
        data['corps'] = message.text
    await info_order.next()


#drinks
@dp.message_handler(Text(equals='Латте'), state=info_order.product)
async def drink_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери объем:', reply_markup = markup_3)
    async with state.proxy() as data:
        data['product'] = message.text
    await info_order.next() 
    

@dp.message_handler(Text(equals='Раф'), state=info_order.product)
async def drink_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери объем:', reply_markup = markup_4)
    async with state.proxy() as data:
        data['product'] = message.text
    await info_order.next() 

@dp.message_handler(Text(equals='Капучино'), state=info_order.product)
async def drink_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери объем:', reply_markup = markup_5)
    async with state.proxy() as data:
        data['product'] = message.text
    await info_order.next() 

@dp.message_handler(Text(equals='Какао'), state=info_order.product)
async def drink_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери объем:', reply_markup = markup_6)
    async with state.proxy() as data:
        data['product'] = message.text
    await info_order.next() 

@dp.message_handler(Text(equals='Горячий шоколад'), state=info_order.product)
async def drink_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери объем:', reply_markup = markup_7)
    async with state.proxy() as data:
        data['product'] = message.text
    await info_order.next() 

@dp.message_handler(Text(equals='Американо'), state=info_order.product)
async def drink_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Выбери объем:', reply_markup = markup_8)
    async with state.proxy() as data:
        data['product'] = message.text
    await info_order.next() 


#latte
@dp.message_handler(Text(equals='Латте 250 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>140 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Латте 380 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>200 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Латте 510 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>245 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()


#raf
@dp.message_handler(Text(equals='Раф 250 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>140 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Раф 380 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>245 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Раф 510 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>275 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

#capuchino
@dp.message_handler(Text(equals='Капучино 250 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>140 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Капучино 380 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>200 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Капучино 510 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>245 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()


#cocoa
@dp.message_handler(Text(equals='Какао 250 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>175 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Какао 380 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>245 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Какао 510 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>275 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()


#hot chocolate
@dp.message_handler(Text(equals='Горячий шоколад 250 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>210 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Горячий шоколад 380 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>280 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Горячий шоколад 510 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>310 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()


#americano
@dp.message_handler(Text(equals='Американо 250 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>120 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Американо 380 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>170 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()

@dp.message_handler(Text(equals='Американо 510 мл'), state=info_order.product_order)
async def bye_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Сумма заказа составила <b>205 рублей</b>\n\nНажми кнопку "Оплата", чтобы продолжить оформление заказа.', reply_markup = markup_9)
    async with state.proxy() as data:
        data['product_order'] = message.text
    await info_order.next()


#pay
@dp.message_handler(Text(equals='Оплата'), state=info_order.verifi)
async def pay_message(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text = 'Для оплаты переведи сумму заказа по номеру телефона: +7-921-314-90-45\n\nПришли чек об оплате в формате <b>JPEG</b> или <b>PNG</b>.')
    async with state.proxy() as data:
        data['verifi'] = message.text
    await info_order.next()

@dp.message_handler(lambda message: not message.photo, state=info_order.photo)
async def check_photo(message: types.Message):
    await message.reply('Это не фотография!')

@dp.message_handler(content_types=['photo'], state=info_order.photo)
async def check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        print(data)

    await edit_profile(state, user_id=message.from_user.id)
    await bot.send_message(chat_id=message.from_user.id, text='Твой заказ принят.\nЧтобы проверить статус заказа, нажми на кнопку ниже.', reply_markup = upload())
    await state.finish()

@dp.callback_query_handler(text='update_info')
async def cd_get_status_order(callback: types.callback_query):   
    order = await get_status_order(callback.message)
    if not order:
        return await callback.message.answer('Ты уже забрал свой напиток.\nЧтобы заказать новый, введи команду /start или нажми на кнопку ниже.', reply_markup = start)
    await show_status(callback, order)
    await callback.answer()

if __name__ == '__main__':
    executor.start_polling (dp, skip_updates = True,
                            on_startup = con)
