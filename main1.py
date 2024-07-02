import asyncio
import os

from parser1.product_first_parser import ProductParser1
from parser1.product_second_parser import ProductParser2
from database_manager import DatabaseManager
from parser1.compareFirstProd import update_new_products_table
from parser1.compare import compare_with_excel, excel_data
from parser1.connect_csv_mysql import session1
from parser1.duplicateParsTable import duplicate_table
from models import ComparedProductsInstaBuyDuplicate, ComparedProductsConfirmPurchaseDuplicate
from buybotInsta import purchaseCheck
from add_new_product_if_not_exists import add_new_product_if_not_exists
from fetch_wbbalance import fetch_balance
from logger import setup_logger

logger1 = setup_logger('parser1logs', 'parser1.log')

product_id_set_telegram = set()
parsing_category = 'https://catalog.wb.ru/catalog/dresses/v2/catalog'

async def main():
    db_url = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfirst'
    db_manager_first = DatabaseManager(db_url)

    parser1 = ProductParser1(db_manager_first)
    parser2 = ProductParser2(db_manager_first)

    product_id_set_buying = set()
    count = 0
    while True:
        wallet_balance = fetch_balance()
        logger1.info(f"Цикл {count}")
        try:
            logger1.info("Парсер1: START")
            if not await parser1.parse_category(parsing_category):
                break
            logger1.info("Парсер1:  END")

            logger1.info("Сравнение 1 и 2 таблицы: START")
            update_new_products_table(db_url, 'pars_table1', 'pars_table2', 'new_product_table')
            logger1.info("Сравнение 1 и 2 таблицы: END")

            logger1.info("Сравнение с Excel: START")
            compare_with_excel(excel_data, session1)
            logger1.info("Сравнение с Excel: END")

            logger1.info("Дублирование compared_products_insta_buy в compared_products_insta_buy_duplicate: START")
            duplicate_table('compared_products_insta_buy', 'compared_products_insta_buy_duplicate', db_url, product_id_set_buying)
            logger1.info("Дублирование compared_products_insta_buy в compared_products_insta_buy_duplicate: END")

            logger1.info("Дублирование compared_products_confirm_purchase в compared_products_confirm_purchase_duplicate: START")
            duplicate_table('compared_products_confirm_purchase', 'compared_products_confirm_purchase_duplicate', db_url, product_id_set_buying)
            logger1.info("Дублирование compared_products_confirm_purchase в compared_products_confirm_purchase_duplicate: END")

            add_new_product_if_not_exists('compared_products_confirm_purchase_duplicate', 'compared_products_confirm_purchase_duplicate_telegram', db_url, product_id_set_telegram)

            logger1.info("BuyBot: START")
            await purchaseCheck(db_url, 'compared_products_insta_buy_duplicate', wallet_balance)
            logger1.info("BuyBot: END")

            logger1.info("Очистка compared_products_insta_buy_duplicate: START")
            db_manager_first.clear_table(ComparedProductsInstaBuyDuplicate)
            logger1.info("Очистка compared_products_insta_buy_duplicate: END")

            logger1.info("Очистка compared_products_confirm_purchase_duplicate: START")
            db_manager_first.clear_table(ComparedProductsConfirmPurchaseDuplicate)
            logger1.info("Очистка compared_products_confirm_purchase_duplicate: END")

            logger1.info("Парсер2: START")
            if not await parser2.parse_category(parsing_category):
                break
            logger1.info("Парсер2: END")

            count += 1

        except Exception as e:
            logger1.error(f"Произошла ошибка: {e}", exc_info=True)
            db_manager_first.update_parser_status(1, 'Ошибка')
            await asyncio.sleep(1)

if __name__ == "__main__":
    with open("main_pid1.txt", "w") as f:
        f.write(str(os.getpid()))
    asyncio.run(main())
