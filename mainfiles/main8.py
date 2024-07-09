import asyncio
import os

from parserfiles.parser8.product_first_parser import ProductParser1
from parserfiles.parser8.product_second_parser import ProductParser2
from wbbotfiles.database_manager import DatabaseManager
from wbbotfiles.compareFirstProd import update_new_products_table
from parserfiles.parser8.compare import compare_with_excel, excel_data
from parserfiles.parser8.connect_csv_mysql import session1
from wbbotfiles.duplicateParsTable import duplicate_table
from wbbotfiles.models import ComparedProductsInstaBuyDuplicate, ComparedProductsConfirmPurchaseDuplicate
from wbbotfiles.buybotInsta import purchaseCheck
from wbbotfiles.add_new_product_if_not_exists import add_new_product_if_not_exists
from wbbotfiles.fetch_wbbalance import fetch_balance
from mainfiles.logger import setup_logger

logger8 = setup_logger('parser8logs', 'parser8.log')

product_id_set_telegram = set()
parsing_category = 'https://catalog.wb.ru/catalog/pants/v2/catalog'

async def main():
    db_url = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsereighth'
    db_manager = DatabaseManager(db_url)

    parser1 = ProductParser1(db_manager)
    parser2 = ProductParser2(db_manager)

    product_id_set_buying = set()
    count = 0
    while True:
        wallet_balance = fetch_balance()
        logger8.info(f"Цикл {count}")
        try:
            logger8.info("Парсер1: START")
            if not await parser1.parse_category(parsing_category):
                break
            logger8.info("Парсер1: END")

            logger8.info("Сравнение 1 и 2 таблицы: START")
            update_new_products_table(db_url, 'pars_table1', 'pars_table2', 'new_product_table')
            logger8.info("Сравнение 1 и 2 таблицы: END")

            logger8.info("Сравнение с Excel: START")
            compare_with_excel(excel_data, session1)
            logger8.info("Сравнение с Excel: END")

            logger8.info("Дублирование compared_products_insta_buy в compared_products_insta_buy_duplicate: START")
            duplicate_table('compared_products_insta_buy', 'compared_products_insta_buy_duplicate', db_url, product_id_set_buying)
            logger8.info("Дублирование compared_products_insta_buy в compared_products_insta_buy_duplicate: END")

            logger8.info("Дублирование compared_products_confirm_purchase в compared_products_confirm_purchase_duplicate: START")
            duplicate_table('compared_products_confirm_purchase', 'compared_products_confirm_purchase_duplicate', db_url, product_id_set_buying)
            logger8.info("Дублирование compared_products_confirm_purchase в compared_products_confirm_purchase_duplicate: END")

            add_new_product_if_not_exists('compared_products_confirm_purchase_duplicate', 'compared_products_confirm_purchase_duplicate_telegram', db_url, product_id_set_telegram)

            logger8.info("BuyBot: START")
            await purchaseCheck(db_url, 'compared_products_insta_buy_duplicate', wallet_balance)
            logger8.info("BuyBot: END")

            logger8.info("Очистка compared_products_insta_buy_duplicate: START")
            db_manager.clear_table(ComparedProductsInstaBuyDuplicate)
            logger8.info("Очистка compared_products_insta_buy_duplicate: END")

            logger8.info("Очистка compared_products_confirm_purchase_duplicate: START")
            db_manager.clear_table(ComparedProductsConfirmPurchaseDuplicate)
            logger8.info("Очистка compared_products_confirm_purchase_duplicate: END")

            logger8.info("Парсер2: START")
            if not await parser2.parse_category(parsing_category):
                break
            logger8.info("Парсер2: END")

            count += 1

        except Exception as e:
            logger8.error(f"Произошла ошибка: {e}", exc_info=True)
            db_manager.update_parser_status(8, 'Ошибка')
            await asyncio.sleep(1)

if __name__ == "__main__":
    with open("main_pid8.txt", "w") as f:
        f.write(str(os.getpid()))
    asyncio.run(main())
