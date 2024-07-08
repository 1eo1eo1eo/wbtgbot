import logging
import asyncio
import json
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from constants import CHAT_IDS
from callbacks import (
    start_command,
    manage_parsers_callback,
    manage_parser1_callback,
    manage_parser2_callback,
    manage_parser3_callback,
    manage_parser4_callback,
    manage_parser5_callback,
    manage_parser6_callback,
    manage_parser7_callback,
    manage_parser8_callback,
    manage_parser9_callback,
    manage_parser10_callback,
    back_to_parsers_callback,
    back_to_main_callback,
    start_parser1_callback,
    stop_parser1_callback,
    status_parser1_callback,
    start_parser2_callback,
    stop_parser2_callback,
    status_parser2_callback,
    start_parser3_callback,
    stop_parser3_callback,
    status_parser3_callback,
    start_parser4_callback,
    stop_parser4_callback,
    status_parser4_callback,
    start_parser5_callback,
    stop_parser5_callback,
    status_parser5_callback,
    start_parser6_callback,
    stop_parser6_callback,
    status_parser6_callback,
    start_parser7_callback,
    stop_parser7_callback,
    status_parser7_callback,
    start_parser8_callback,
    stop_parser8_callback,
    status_parser8_callback,
    start_parser9_callback,
    stop_parser9_callback,
    status_parser9_callback,
    start_parser10_callback,
    stop_parser10_callback,
    status_parser10_callback,
    get_status_all_parsers_callback,
    start_all_parsers_callback,
    stop_all_parsers_callback,
    buy_product_callback,
    handle_quantity_input,
    confirm_buy_callback,
    change_quantity_callback,
    skip_product_callback,
    PurchaseStates
)

router = Router()
storage = MemoryStorage()

router.message(CommandStart())(start_command)

async def handle_buy_callback(callback_query: CallbackQuery, state: FSMContext):
    callback_data = json.loads(callback_query.data)
    parser_number = callback_data.get("pn")
    await buy_product_callback(callback_query, state, parser_number)

async def handle_confirm_callback(callback_query: CallbackQuery):
    callback_data = json.loads(callback_query.data)
    parser_number = callback_data.get("pn")
    await confirm_buy_callback(callback_query, parser_number)

router.callback_query(lambda c: c.data == "manage_parsers")(manage_parsers_callback)
router.callback_query(lambda c: c.data == "manage_parser1")(manage_parser1_callback)
router.callback_query(lambda c: c.data == "manage_parser2")(manage_parser2_callback)
router.callback_query(lambda c: c.data == "manage_parser3")(manage_parser3_callback)
router.callback_query(lambda c: c.data == "manage_parser4")(manage_parser4_callback)
router.callback_query(lambda c: c.data == "manage_parser5")(manage_parser5_callback)
router.callback_query(lambda c: c.data == "manage_parser6")(manage_parser6_callback)
router.callback_query(lambda c: c.data == "manage_parser7")(manage_parser7_callback)
router.callback_query(lambda c: c.data == "manage_parser8")(manage_parser8_callback)
router.callback_query(lambda c: c.data == "manage_parser9")(manage_parser9_callback)
router.callback_query(lambda c: c.data == "manage_parser10")(manage_parser10_callback)
router.callback_query(lambda c: c.data == "back_to_parsers")(back_to_parsers_callback)
router.callback_query(lambda c: c.data == "back_to_main")(back_to_main_callback)
router.callback_query(lambda c: c.data == "start_parser1")(start_parser1_callback)
router.callback_query(lambda c: c.data == "stop_parser1")(stop_parser1_callback)
router.callback_query(lambda c: c.data == "status_parser1")(status_parser1_callback)
router.callback_query(lambda c: c.data == "start_parser2")(start_parser2_callback)
router.callback_query(lambda c: c.data == "stop_parser2")(stop_parser2_callback)
router.callback_query(lambda c: c.data == "status_parser2")(status_parser2_callback)
router.callback_query(lambda c: c.data == "start_parser3")(start_parser3_callback)
router.callback_query(lambda c: c.data == "stop_parser3")(stop_parser3_callback)
router.callback_query(lambda c: c.data == "status_parser3")(status_parser3_callback)
router.callback_query(lambda c: c.data == "start_parser4")(start_parser4_callback)
router.callback_query(lambda c: c.data == "stop_parser4")(stop_parser4_callback)
router.callback_query(lambda c: c.data == "status_parser4")(status_parser4_callback)
router.callback_query(lambda c: c.data == "start_parser5")(start_parser5_callback)
router.callback_query(lambda c: c.data == "stop_parser5")(stop_parser5_callback)
router.callback_query(lambda c: c.data == "status_parser5")(status_parser5_callback)
router.callback_query(lambda c: c.data == "start_parser6")(start_parser6_callback)
router.callback_query(lambda c: c.data == "stop_parser6")(stop_parser6_callback)
router.callback_query(lambda c: c.data == "status_parser6")(status_parser6_callback)
router.callback_query(lambda c: c.data == "start_parser7")(start_parser7_callback)
router.callback_query(lambda c: c.data == "stop_parser7")(stop_parser7_callback)
router.callback_query(lambda c: c.data == "status_parser7")(status_parser7_callback)
router.callback_query(lambda c: c.data == "start_parser8")(start_parser8_callback)
router.callback_query(lambda c: c.data == "stop_parser8")(stop_parser8_callback)
router.callback_query(lambda c: c.data == "status_parser8")(status_parser8_callback)
router.callback_query(lambda c: c.data == "start_parser9")(start_parser9_callback)
router.callback_query(lambda c: c.data == "stop_parser9")(stop_parser9_callback)
router.callback_query(lambda c: c.data == "status_parser9")(status_parser9_callback)
router.callback_query(lambda c: c.data == "start_parser10")(start_parser10_callback)
router.callback_query(lambda c: c.data == "stop_parser10")(stop_parser10_callback)
router.callback_query(lambda c: c.data == "status_parser10")(status_parser10_callback)
router.callback_query(lambda c: c.data == "get_status_all_parsers")(get_status_all_parsers_callback)
router.callback_query(lambda c: c.data == "start_all_parsers")(start_all_parsers_callback)
router.callback_query(lambda c: c.data == "stop_all_parsers")(stop_all_parsers_callback)
router.callback_query(lambda c: c.data and json.loads(c.data).get("a") == "buy")(handle_buy_callback)
router.message(PurchaseStates.awaiting_quantity)(handle_quantity_input)
router.callback_query(lambda c: c.data and json.loads(c.data).get("a") == "confirm_buy")(handle_confirm_callback)
router.callback_query(lambda c: c.data and json.loads(c.data).get("a") == "change_quantity")(change_quantity_callback)
router.callback_query(lambda c: c.data and json.loads(c.data).get("a") == "skip")(skip_product_callback)
