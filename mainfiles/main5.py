import asyncio
import os

from parser5.product_first_parser import ProductParser1
from parser5.product_second_parser import ProductParser2
from database_manager import DatabaseManager
from compareFirstProd import update_new_products_table
from parser5.compare import compare_with_excel, excel_data
from parser5.connect_csv_mysql import session1
from duplicateParsTable import duplicate_table
from models import ComparedProductsInstaBuyDuplicate, ComparedProductsConfirmPurchaseDuplicate
from buybotInsta import purchaseCheck
from add_new_product_if_not_exists import add_new_product_if_not_exists
from fetch_wbbalance import fetch_balance
from logger import setup_logger

logger5 = setup_logger('parser5logs', 'parser5.log')

product_id_set_telegram = set()
parsing_category = 'https://catalog.wb.ru/catalog/shorts/v2/catalog'

async def main():
    db_url = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfifth'
    db_manager_fifth = DatabaseManager(db_url)

    parser1 = ProductParser1(db_manager_fifth)
    parser2 = ProductParser2(db_manager_fifth)

    product_id_set_buying = set()
    count = 0
    while True:
        wallet_balance = fetch_balance()
        logger5.info(f"Цикл {count}")
        try:
            logger5.info("Парсер1: START")
            if not await parser1.parse_category(parsing_category):
                break
            logger5.info("Парсер1:  END")

            logger5.info("Сравнение 1 и 2 таблицы: START")
            update_new_products_table(db_url, 'pars_table1', 'pars_table2', 'new_product_table')
            logger5.info("Сравнение 1 и 2 таблицы: END")

            logger5.info("Сравнение с Excel: START")
            compare_with_excel(excel_data, session1)
            logger5.info("Сравнение с Excel: END")

            logger5.info("Дублирование compared_products_insta_buy в compared_products_insta_buy_duplicate: START")
            duplicate_table('compared_products_insta_buy', 'compared_products_insta_buy_duplicate', db_url, product_id_set_buying)
            logger5.info("Дублирование compared_products_insta_buy в compared_products_insta_buy_duplicate: END")

            logger5.info("Дублирование compared_products_confirm_purchase в compared_products_confirm_purchase_duplicate: START")
            duplicate_table('compared_products_confirm_purchase', 'compared_products_confirm_purchase_duplicate', db_url, product_id_set_buying)
            logger5.info("Дублирование compared_products_confirm_purchase в compared_products_confirm_purchase_duplicate: END")

            add_new_product_if_not_exists('compared_products_confirm_purchase_duplicate', 'compared_products_confirm_purchase_duplicate_telegram', db_url, product_id_set_telegram)

            logger5.info("BuyBot: START")
            await purchaseCheck(db_url, 'compared_products_insta_buy_duplicate', wallet_balance)
            logger5.info("BuyBot: END")

            logger5.info("Очистка compared_products_insta_buy_duplicate: START")
            db_manager_fifth.clear_table(ComparedProductsInstaBuyDuplicate)
            logger5.info("Очистка compared_products_insta_buy_duplicate: END")

            logger5.info("Очистка compared_products_confirm_purchase_duplicate: START")
            db_manager_fifth.clear_table(ComparedProductsConfirmPurchaseDuplicate)
            logger5.info("Очистка compared_products_confirm_purchase_duplicate: END")

            logger5.info("Парсер2: START")
            if not await parser2.parse_category(parsing_category):
                break
            logger5.info("Парсер2: END")

            count += 1

        except Exception as e:
            logger5.error(f"Произошла ошибка: {e}", exc_info=True)
            db_manager_fifth.update_parser_status(5, 'Ошибка')
            await asyncio.sleep(1)

if __name__ == "__main__":
    with open("main_pid5.txt", "w") as f:
        f.write(str(os.getpid()))
    asyncio.run(main())
