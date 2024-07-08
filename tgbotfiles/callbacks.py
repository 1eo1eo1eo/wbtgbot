import logging
import json
import math
import subprocess
import asyncio
import time
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from buybotInsta import balacne_before_purchase
from aiogram import Dispatcher

from database_manager import ManagerForTelegram, DatabaseManager
from models import (
    ComparedProductsConfirmPurchase,
    ComparedProductsInstaBuy,
    ComparedProductsConfirmPurchaseDuplicateTelegram,
    ComparedProductsInstaBuyDuplicateTelegram
)
from fetch_wbbalance import fetch_balance
from buybotConfirm import purchaseCheck_confirm
from modules import bot
from keyboards import (
    create_parser_controls,
    create_commands_keyboard,
    create_parsers_keyboard,
    create_parser1_controls,
    create_parser2_controls,
    create_parser3_controls,
    create_parser4_controls,
    create_parser5_controls,
    create_parser6_controls,
    create_parser7_controls,
    create_parser8_controls,
    create_parser9_controls,
    create_parser10_controls,
)
from constants import (
    CHAT_IDS,
    DB_URL_FIRST,
    DB_URL_SECOND,
    DB_URL_THIRD,
    DB_URL_FOURTH,
    DB_URL_FIFTH,
    DB_URL_SIXTH,
    DB_URL_SEVENTH,
    DB_URL_EIGHTH,
    DB_URL_NINETH,
    DB_URL_TENTH,
    PRODUCT_TEMPLATE,
    PURCHASE_TEMPLATE,
    CONFIRM_BUY_TEMPLATE,
    STATUS_TEMPLATE,
    PARSER_SCRIPTS,
    PID_FILE_PATHS
)
from helpers import is_process_running, read_pid_from_file, correct_image_url

db_manager_first = ManagerForTelegram(DB_URL_FIRST)
db_manager_1_first = DatabaseManager(DB_URL_FIRST)
db_manager_second = ManagerForTelegram(DB_URL_SECOND)
db_manager_1_second = DatabaseManager(DB_URL_SECOND)
db_manager_third = ManagerForTelegram(DB_URL_THIRD)
db_manager_1_third = DatabaseManager(DB_URL_THIRD)
db_manager_fourth = ManagerForTelegram(DB_URL_FOURTH)
db_manager_1_fourth = DatabaseManager(DB_URL_FOURTH)
db_manager_fifth = ManagerForTelegram(DB_URL_FIFTH)
db_manager_1_fifth = DatabaseManager(DB_URL_FIFTH)
db_manager_sixth = ManagerForTelegram(DB_URL_SIXTH)
db_manager_1_sixth = DatabaseManager(DB_URL_SIXTH)
db_manager_seventh = ManagerForTelegram(DB_URL_SEVENTH)
db_manager_1_seventh = DatabaseManager(DB_URL_SEVENTH)
db_manager_eighth = ManagerForTelegram(DB_URL_EIGHTH)
db_manager_1_eighth = DatabaseManager(DB_URL_EIGHTH)
db_manager_nineth = ManagerForTelegram(DB_URL_NINETH)
db_manager_1_nineth = DatabaseManager(DB_URL_NINETH)
db_manager_tenth = ManagerForTelegram(DB_URL_TENTH)
db_manager_1_tenth = DatabaseManager(DB_URL_TENTH)
balance_after_purchase = fetch_balance()

class PurchaseStates(StatesGroup):
    awaiting_quantity = State()

db_managers = {
    1: db_manager_1_first,
    2: db_manager_1_second,
    3: db_manager_1_third,
    4: db_manager_1_fourth,
    5: db_manager_1_fifth,
    6: db_manager_1_sixth,
    7: db_manager_1_seventh,
    8: db_manager_1_eighth,
    9: db_manager_1_nineth,
    10: db_manager_1_tenth,
}

db_managers_telegram = {
    1: db_manager_first,
    2: db_manager_second,
    3: db_manager_third,
    4: db_manager_fourth,
    5: db_manager_fifth,
    6: db_manager_sixth,
    7: db_manager_seventh,
    8: db_manager_eighth,
    9: db_manager_nineth,
    10: db_manager_tenth,
}

DB_URLS = {
    1: DB_URL_FIRST,
    2: DB_URL_SECOND,
    3: DB_URL_THIRD,
    4: DB_URL_FOURTH,
    5: DB_URL_FIFTH,
    6: DB_URL_SIXTH,
    7: DB_URL_SEVENTH,
    8: DB_URL_EIGHTH,
    9: DB_URL_NINETH,
    10: DB_URL_TENTH,
}

async def start_command(message: Message):
    user_id = str(message.from_user.id)
    if user_id not in CHAT_IDS:
        await message.answer("У вас нет доступа к этому боту.")
        return
    keyboard = create_commands_keyboard()
    await message.reply("Здравствуйте! Выберите команду:", reply_markup=keyboard)

async def manage_parsers_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parsers_keyboard())

async def manage_parser1_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser1_controls(enable_stop=True))

async def manage_parser2_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser2_controls(enable_stop=True))

async def manage_parser3_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser3_controls(enable_stop=True))

async def manage_parser4_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser4_controls(enable_stop=True))

async def manage_parser5_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser5_controls(enable_stop=True))

async def manage_parser6_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser6_controls(enable_stop=True))

async def manage_parser7_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser7_controls(enable_stop=True))

async def manage_parser8_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser8_controls(enable_stop=True))

async def manage_parser9_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser9_controls(enable_stop=True))

async def manage_parser10_callback(callback_query: CallbackQuery):
    await _manage_parsers_or_parser(callback_query, create_parser10_controls(enable_stop=True))

async def _manage_parsers_or_parser(callback_query: CallbackQuery, keyboard):
    user_id = str(callback_query.from_user.id)
    if user_id not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)
    await callback_query.answer()

async def back_to_parsers_callback(callback_query: CallbackQuery):
    await _back_to_callback(callback_query, create_parsers_keyboard())

async def back_to_main_callback(callback_query: CallbackQuery):
    await _back_to_callback(callback_query, create_commands_keyboard())

async def _back_to_callback(callback_query: CallbackQuery, keyboard):
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)
    await callback_query.answer()

async def start_parser1_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 1)

async def stop_parser1_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 1)

async def status_parser1_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 1)

async def start_parser2_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 2)

async def stop_parser2_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 2)

async def status_parser2_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 2)

async def start_parser3_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 3)

async def stop_parser3_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 3)

async def status_parser3_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 3)

async def start_parser4_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 4)

async def stop_parser4_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 4)

async def status_parser4_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 4)

async def start_parser5_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 5)

async def stop_parser5_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 5)

async def status_parser5_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 5)

async def start_parser6_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 6)

async def stop_parser6_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 6)

async def status_parser6_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 6)

async def start_parser7_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 7)

async def stop_parser7_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 7)

async def status_parser7_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 7)

async def start_parser8_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 8)

async def stop_parser8_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 8)

async def status_parser8_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 8)

async def start_parser9_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 9)

async def stop_parser9_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 9)

async def status_parser9_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 9)

async def start_parser10_callback(callback_query: CallbackQuery):
    await _start_parser(callback_query, 10)

async def stop_parser10_callback(callback_query: CallbackQuery):
    await _stop_parser(callback_query, 10)

async def status_parser10_callback(callback_query: CallbackQuery):
    await _status_parser(callback_query, 10)

async def start_all_parsers_callback(callback_query: CallbackQuery):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return

    already_running_parsers = []
    started_parsers = []

    for parser_number in db_managers.keys():
        try:
            pid = read_pid_from_file(PID_FILE_PATHS[parser_number])
            is_running = is_process_running(pid) if pid else False

            if is_running:
                already_running_parsers.append(parser_number)
            else:
                db_manager = db_managers.get(parser_number)
                db_manager.update_parser_status(parser_number, 'Запущен')
                
                process = subprocess.Popen(["/bin/bash", "-c", PARSER_SCRIPTS[parser_number]["start"]])
                db_manager.update_parser_pid(parser_number, process.pid)
                
                started_parsers.append(parser_number)
        except Exception as e:
            await callback_query.message.answer(f"Ошибка при запуске парсера {parser_number}: {str(e)}")
    
    if already_running_parsers:
        already_running_message = "Уже запущены парсеры: " + ", ".join(map(str, already_running_parsers))
        await callback_query.message.answer(already_running_message)
    
    if started_parsers:
        started_message = "Запущены парсеры: " + ", ".join(map(str, started_parsers))
        await callback_query.message.answer(started_message)

    await callback_query.answer()

async def stop_all_parsers_callback(callback_query: CallbackQuery):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return

    already_stopped_parsers = []
    stopped_parsers = []

    for parser_number in db_managers.keys():
        try:
            pid = read_pid_from_file(PID_FILE_PATHS[parser_number])
            is_running = is_process_running(pid) if pid else False

            if not is_running:
                already_stopped_parsers.append(parser_number)
            else:
                db_manager = db_managers.get(parser_number)
                db_manager.update_parser_status(parser_number, 'Остановлен')
                
                subprocess.Popen(["/bin/bash", "-c", PARSER_SCRIPTS[parser_number]["stop"]])
                db_manager.clear_parser_pid(parser_number)
                
                stopped_parsers.append(parser_number)
        except Exception as e:
            await callback_query.message.answer(f"Ошибка при остановке парсера {parser_number}: {str(e)}")
    
    if already_stopped_parsers:
        already_stopped_message = "Уже остановлены парсеры: " + ", ".join(map(str, already_stopped_parsers))
        await callback_query.message.answer(already_stopped_message)
    
    if stopped_parsers:
        stopped_message = "Остановлены парсеры: " + ", ".join(map(str, stopped_parsers))
        await callback_query.message.answer(stopped_message)

    await callback_query.answer()


async def _start_parser(callback_query: CallbackQuery, parser_number: int):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    try:
        pid = read_pid_from_file(PID_FILE_PATHS[parser_number])
        is_running = is_process_running(pid) if pid else False

        if is_running:
            await callback_query.message.answer(f"Парсер {parser_number} уже запущен.")
        else:
            await _update_parser_controls(callback_query, parser_number, enable_stop=False, delay=0)
            db_manager = db_managers.get(parser_number)
            db_manager.update_parser_status(parser_number, 'Запущен')
            
            process = subprocess.Popen(["/bin/bash", "-c", PARSER_SCRIPTS[parser_number]["start"]])
            db_manager.update_parser_pid(parser_number, process.pid)
            
            await callback_query.message.answer(f"Парсинг {parser_number} запущен")
            await _update_parser_controls(callback_query, parser_number, enable_stop=True, delay=5)
            await callback_query.message.answer("Выберите команду:", reply_markup=create_parser_controls(parser_number, enable_stop=True))
    except Exception as e:
        await callback_query.message.answer(f"Ошибка при запуске парсера: {str(e)}")
    await callback_query.answer()


async def _stop_parser(callback_query: CallbackQuery, parser_number: int):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    try:
        db_manager = db_managers.get(parser_number)
        db_manager.update_parser_status(parser_number, 'Остановлен')
        subprocess.Popen(["/bin/bash", "-c", PARSER_SCRIPTS[parser_number]["stop"]])
        db_manager.clear_parser_pid(parser_number)
        await callback_query.message.answer(f"Парсинг '{parser_number}' остановлен")
        await callback_query.message.answer("Выберите команду:", reply_markup=create_parser_controls(parser_number, enable_stop=True))
    except Exception as e:
        await callback_query.message.answer(f"Ошибка при остановке парсера: {str(e)}")
    await callback_query.answer()

async def _status_parser(callback_query: CallbackQuery, parser_number: int):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    try:
        pid = read_pid_from_file(PID_FILE_PATHS[parser_number])
        is_running = is_process_running(pid) if pid else False
        db_manager = db_managers.get(parser_number)
        parser_status = db_manager.get_parser_status(parser_number)
        logging.info(f"Проверка статуса парсера {parser_number}: PID {pid}, запущен: {is_running}")
        if parser_status:
            status_message = STATUS_TEMPLATE.format(
                parser_number=parser_status.parser_number,
                status="Запущен" if is_running else "Остановлен",
                category=parser_status.category
            )
            await callback_query.message.answer(status_message, parse_mode='html')  
            await callback_query.message.answer("Выберите команду:", reply_markup=create_parser_controls(parser_number, enable_stop=True))
        else:
            await callback_query.message.answer(f"Статус парсера {parser_number} не найден.")
    except Exception as e:
        await callback_query.message.answer(f"Ошибка: {str(e)}")
        logging.error(f"Ошибка в status_parser_callback: {e}")
    await callback_query.answer()

async def get_status_all_parsers_callback(callback_query: CallbackQuery):
    user_id = str(callback_query.from_user.id)
    if user_id not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    
    retries = 5
    while retries > 0:
        try:
            status_messages = []
            for parser_number in db_managers.keys():
                pid = read_pid_from_file(PID_FILE_PATHS[parser_number])
                is_running = is_process_running(pid) if pid else False
                db_manager = db_managers.get(parser_number)
                parser_status = db_manager.get_parser_status(parser_number)
                logging.info(f"Проверка статуса парсера {parser_number}: PID {pid}, запущен: {is_running}")
                if parser_status:
                    status_message = STATUS_TEMPLATE.format(
                        parser_number=parser_status.parser_number,
                        status="Запущен" if is_running else "Остановлен",
                        category=parser_status.category
                    )
                    status_messages.append(status_message)
            if status_messages:
                await callback_query.message.answer("\n\n".join(status_messages), parse_mode='html')
                await callback_query.message.answer("Выберите команду:", reply_markup=create_commands_keyboard())
            else:
                await callback_query.message.answer("Статусы парсеров не найдены.")
            break  # Выход из цикла при успешном выполнении
        except Exception as e:
            logging.error(f"Ошибка: {str(e)}")
            await callback_query.message.answer(f"Ошибка: {str(e)}")
            retries -= 1
            if retries > 0:
                time.sleep(1)
            else:
                logging.error(f"Ошибка в get_status_all_parsers_callback: {e}")
    await callback_query.answer()

async def buy_product_callback(callback_query: CallbackQuery, state: FSMContext, parser_number: int):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    callback_data = json.loads(callback_query.data)
    logging.info(f"Buy product callback with data: {callback_query.data}")
    product_id = callback_data["p"]

    logging.info(f"Parser number: {parser_number}")
    logging.info(f"DB Managers: {db_managers_telegram}")

    db_manager = db_managers_telegram.get(parser_number)

    if db_manager is None:
        logging.error(f"No db_manager found for parser_number: {parser_number}")
        await callback_query.message.answer("Ошибка: db_manager не найден.")
        return
    
    product = db_manager.get_product_by_id(product_id, ComparedProductsConfirmPurchase)

        
    if product:
        await callback_query.message.answer(f"Покупка товара: {product.name} за {product.price}\nВведите количество товара для покупки:")
        await state.update_data(product_id=product_id, parser_number=parser_number)
        await state.set_state(PurchaseStates.awaiting_quantity)
    else:
        logging.error(f"Товар не найден для product_id: {product_id}")
        await bot.send_message(callback_query.from_user.id, "Ошибка: товар не найден.")
    await callback_query.answer()

async def handle_quantity_input(message: Message, state: FSMContext):
    if str(message.from_user.id) not in CHAT_IDS:
        await message.answer("У вас нет доступа к этому боту.")
        return
    try:
        quantity = int(message.text)
        data = await state.get_data()
        product_id = data.get("product_id")
        parser_number = data.get("parser_number")
        logging.info(f"Обработка ввода количества для product_id: {product_id} с количеством: {quantity}")
        db_manager = db_managers_telegram.get(parser_number)
        product = db_manager.get_product_by_id(product_id, ComparedProductsConfirmPurchase)
        if product:
            total_cost = product.price * quantity
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Подтвердить", callback_data=json.dumps({"a": "confirm_buy", "p": product_id, "q": quantity, "pn": parser_number})),
                        InlineKeyboardButton(text="Изменить количество", callback_data=json.dumps({"a": "change_quantity", "p": product_id, "pn": parser_number}))
                    ]
                ]
            )
            await message.answer(f"Подтверждение покупки товара: {product.name}\nКоличество: {quantity}\nОбщая стоимость: {total_cost} рублей", reply_markup=keyboard)
        else:
            await message.answer("Ошибка: товар не найден.")
    except ValueError:
        await message.answer("Ошибка: введите корректное число.")
    await state.clear()

async def confirm_buy_callback(callback_query: CallbackQuery, parser_number: int):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    await callback_query.answer()
    try:
        callback_data = json.loads(callback_query.data)
        product_id = callback_data["p"]
        quantity = callback_data["q"]
        try:
            db_manager = db_managers_telegram.get(parser_number)
            product = db_manager.get_product_by_id(product_id, ComparedProductsConfirmPurchase)
            if product:
                total_cost = balacne_before_purchase - balance_after_purchase
                logging.info(f"Total cost calculated: {total_cost}")
                quantity_purchase = math.floor((balacne_before_purchase - balance_after_purchase) / product.price)
                logging.info(f"Quantity purchase calculated: {quantity_purchase}")
                
                db_url = DB_URLS.get(parser_number, DB_URL_FIRST)

                await purchaseCheck_confirm(db_url, 'compared_products_confirm_purchase', quantity)
                await bot.send_message(callback_query.from_user.id, f"Товар успешно куплен за {total_cost} рублей\nОстаток на балансе: {balance_after_purchase} рублей\nКоличество купленного товара: {quantity_purchase}")
            else:
                logging.error(f"Товар не найден для product_id: {product_id}")
                await bot.send_message(callback_query.from_user.id, "Ошибка: товар не найден.")
        except Exception as e:
            logging.error(f"Ошибка в confirm_buy: {e}")
            await bot.send_message(callback_query.from_user.id, "Ошибка обработки данных.")
    except ValueError as e:
        logging.error(f"Ошибка в confirm_buy: {e}")
        await bot.send_message(callback_query.from_user.id, "Ошибка обработки данных.")

async def change_quantity_callback(callback_query: CallbackQuery, state: FSMContext):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    callback_data = json.loads(callback_query.data)
    product_id = callback_data["p"]
    parser_number = callback_data["pn"]
    await callback_query.message.answer(f"Введите новое количество для товара {product_id}:")
    await state.update_data(product_id=product_id, parser_number=parser_number)
    await state.set_state(PurchaseStates.awaiting_quantity)
    await callback_query.answer()

async def skip_product_callback(callback_query: CallbackQuery):
    if str(callback_query.from_user.id) not in CHAT_IDS:
        await callback_query.message.answer("У вас нет доступа к этому боту.")
        return
    await bot.send_message(callback_query.from_user.id, "Товар пропущен.")
    await callback_query.answer()

async def _update_parser_controls(callback_query: CallbackQuery, parser_number: int, enable_stop: bool, delay: int):
    await asyncio.sleep(delay)
    if parser_number == 1:
        new_keyboard = create_parser1_controls(enable_stop=enable_stop)
    elif parser_number == 2:
        new_keyboard = create_parser2_controls(enable_stop=enable_stop)
    elif parser_number == 3:
        new_keyboard = create_parser3_controls(enable_stop=enable_stop)
    elif parser_number == 4:
        new_keyboard = create_parser4_controls(enable_stop=enable_stop)
    elif parser_number == 5:
        new_keyboard = create_parser5_controls(enable_stop=enable_stop)
    elif parser_number == 6:
        new_keyboard = create_parser5_controls(enable_stop=enable_stop)
    elif parser_number == 7:
        new_keyboard = create_parser5_controls(enable_stop=enable_stop)
    elif parser_number == 8:
        new_keyboard = create_parser5_controls(enable_stop=enable_stop)
    elif parser_number == 9:
        new_keyboard = create_parser5_controls(enable_stop=enable_stop)
    elif parser_number == 10:
        new_keyboard = create_parser5_controls(enable_stop=enable_stop)
    else:
        new_keyboard = create_commands_keyboard()
    if callback_query.message.reply_markup != new_keyboard:
        await callback_query.message.edit_reply_markup(reply_markup=new_keyboard)

async def notify_new_products(dispatcher: Dispatcher):
    while True:
        for db_manager, product_model, template in [
            (db_manager_first, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_second, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_third, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_fourth, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_fifth, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_sixth, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_seventh, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_eighth, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_nineth, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
            (db_manager_tenth, ComparedProductsInstaBuyDuplicateTelegram, PURCHASE_TEMPLATE),
        ]:
            try:
                products = db_manager.get_products(product_model)
                if products:
                    for product in products:
                        corrected_image_url = correct_image_url(product.image_url)
                        formatted_text = template.format(product=product)
                        quantity_purchase = math.floor((balacne_before_purchase - balance_after_purchase) / product.price)
                        for chat_id in CHAT_IDS:
                            if corrected_image_url:
                                await bot.send_photo(chat_id=chat_id, photo=corrected_image_url, caption=f"{formatted_text}\nКоличество купленных товаров: {quantity_purchase} шт\nБаланс: {balance_after_purchase} рублей", parse_mode='html')
                            else:
                                await bot.send_message(chat_id=chat_id, text=f"{formatted_text}\nКоличество купленных товаров: {quantity_purchase} шт\nБаланс: {balance_after_purchase} рублей", parse_mode='html')
                    db_manager.clear_table(product_model)
            except Exception as e:
                logging.error(f"Ошибка в notify_new_products: {e}")
        await asyncio.sleep(1)

async def notify_discounted_products(dispatcher: Dispatcher):
    while True:
        for db_manager, product_model, template in [
            (db_manager_first, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_second, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_third, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_fourth, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_fifth, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_sixth, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_seventh, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_eighth, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_nineth, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
            (db_manager_tenth, ComparedProductsConfirmPurchaseDuplicateTelegram, CONFIRM_BUY_TEMPLATE),
        ]:
            try:
                products = db_manager.get_products(product_model)
                balance = fetch_balance()
                if products:
                    for product in products:
                        corrected_image_url = correct_image_url(product.image_url)
                        formatted_text = template.format(product=product)

                        keyboard = InlineKeyboardMarkup(
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(text="Купить", callback_data=json.dumps({"a": "buy", "p": product.product_id, "pn": product.parser_number})),
                                    InlineKeyboardButton(text="Отклонить", callback_data=json.dumps({"a": "skip", "p": product.product_id}))
                                ]
                            ]
                        )

                        for chat_id in CHAT_IDS:
                            if corrected_image_url:
                                await bot.send_photo(chat_id=chat_id, photo=corrected_image_url, caption=f"{formatted_text}\nБаланс: {balance} рублей", reply_markup=keyboard, parse_mode='html')
                            else:
                                await bot.send_message(chat_id=chat_id, text=f"{formatted_text}\nБаланс: {balance} рублей", reply_markup=keyboard, parse_mode='html')
                    db_manager.clear_table(product_model)
            except Exception as e:
                if 'mysql.connector.errors.ProgrammingError' in str(e):
                    continue
                else:
                    logging.error(f"Ошибка в notify_discounted_products: {e}")
        await asyncio.sleep(1)