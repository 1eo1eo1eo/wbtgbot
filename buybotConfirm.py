import asyncio
import logging
import time

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from sqlalchemy import create_engine, select, Table
from sqlalchemy.orm import sessionmaker
from models import Base
from fetch_wbbalance import fetch_balance

balacne_before_purchase = fetch_balance()
last_checked_id = 0
product_id_set_telegram = set()

async def add_to_cart_and_increase_quantity(page, remaining_quantity, url_basket):
    total_clicks = 1
    
    try:
        add_to_cart_btn = await page.wait_for_selector('button.btn-main')
        if await add_to_cart_btn.is_visible():
            await add_to_cart_btn.click()
            logging.info("Add to cart button clicked")
        else:
            logging.warning("Add to cart button is not visible, continuing.")
            return total_clicks
    except PlaywrightTimeoutError:
        logging.warning("Add to cart button not found, continuing.")
        return total_clicks

    await page.goto(url_basket)
    await asyncio.sleep(2)

    while total_clicks < remaining_quantity:
        try:
            add_product_quantity = await page.query_selector('.count__plus')
            if not add_product_quantity:
                logging.warning("Add product quantity button not found, breaking loop.")
                break
            if 'disabled' in await add_product_quantity.get_attribute('class'):
                logging.warning("Add product button is disabled, breaking loop.")
                break
            else:
                await add_product_quantity.click()
                total_clicks += 1
                logging.info(f"Clicked add product quantity button, total clicks: {total_clicks}")
                await asyncio.sleep(0.2)
        except PlaywrightTimeoutError:
            logging.warning("Failed to find or interact with the quantity button.")
            break

    return total_clicks

async def extract_sizes(page):
    sizes = []
    size_elements = await page.query_selector_all('.sizes-list__item')
    for size_element in size_elements:
        size_label = await size_element.query_selector('.sizes-list__size')
        size_text = await size_label.inner_text()
        sizes.append(size_text)
    return sizes

async def process_size(page, size_text, remaining_quantity, url, url_basket, processed_sizes):
    if size_text in processed_sizes:
        logging.info(f"Size {size_text} already processed, skipping.")
        return 0

    await page.goto(url)
    await asyncio.sleep(2)
    try:
        size_label = await page.query_selector(f'.sizes-list__size >> text="{size_text}"')
        if size_label:
            size_item = await size_label.query_selector('..')
            if 'disabled' not in await size_item.get_attribute('class'):
                await size_label.click()
                logging.info(f"Size {size_text} selected")
                await asyncio.sleep(1)
                clicks = await add_to_cart_and_increase_quantity(page, remaining_quantity, url_basket)
                return clicks
        else:
            logging.warning(f"Size {size_text} not found")
    except PlaywrightTimeoutError:
        logging.warning(f"Failed to interact with size element: {size_text}")
    return 0

async def payment_upon_receipt(page):
    logging.warning("payment upon inside")

    buy_btn = await page.query_selector('button.b-btn-do-order')

    payment_btn_selector = 'button.tabs-switch__text'

    payment_buttons = await page.query_selector_all(payment_btn_selector)
    
    payment_upon_receipt_btn = None

    for btn in payment_buttons:
        btn_text = await page.evaluate('(btn) => btn.innerText', btn)
        if "При получении" in btn_text:
            payment_upon_receipt_btn = btn
            break

    if payment_upon_receipt_btn:
        is_active = await page.evaluate('(btn) => btn.parentElement.classList.contains("active")', payment_upon_receipt_btn)
        if not is_active:
            logging.warning("Payment upon receipt button not active, ACTIVATING!.")
            await payment_upon_receipt_btn.click()
        logging.warning("Clicking payment upon receipt button, buying.")
        await buy_btn.click()
    else:
        logging.warning("Payment upon receipt button not found, buying.")
        await buy_btn.click()


async def purchase_product_with_sizes(page, product_id, quantity):
    url = f"https://www.wildberries.ru/catalog/{product_id}/detail.aspx"
    url_basket = "https://www.wildberries.ru/lk/basket"
    
    await page.goto(url)
    logging.info(f"Opened product page: {url}")
    await asyncio.sleep(2)

    sizes = await extract_sizes(page)
    processed_sizes = []
    total_added = 0

    priority_sizes = ['S', '42', 'M', '44', '40/42', '42/44']

    for size_text in priority_sizes:
        if size_text in sizes:
            clicks = await process_size(page, size_text, quantity - total_added, url, url_basket, processed_sizes)
            total_added += clicks
            processed_sizes.append(size_text)
            if total_added >= quantity:
                break

    for size_text in sizes:
        if total_added >= quantity:
            logging.warning("payment upon start")
            await payment_upon_receipt(page)
            time.sleep(3)
            break
        if size_text not in processed_sizes:
            clicks = await process_size(page, size_text, quantity - total_added, url, url_basket, processed_sizes)
            total_added += clicks
            processed_sizes.append(size_text)

    if total_added < quantity:
        await payment_upon_receipt(page)
        logging.warning(f"Desired quantity not reached. Processed all sizes. Total added: {total_added}")

async def purchase_product_without_sizes(page, product_id, quantity):
    url = f"https://www.wildberries.ru/catalog/{product_id}/detail.aspx"
    url_basket = "https://www.wildberries.ru/lk/basket"
    
    await page.goto(url)
    logging.info(f"Opened product page: {url}")
    await asyncio.sleep(2)

    total_added = await add_to_cart_and_increase_quantity(page, quantity, url_basket)
    
    if total_added < quantity:
        await payment_upon_receipt(page)
        logging.warning(f"Desired quantity not reached. Total added: {total_added}")
        time.sleep(3)

    if total_added >= quantity:
        await payment_upon_receipt(page)
        logging.warning(f"Max quantity: {total_added}")
        time.sleep(3)

async def purchase_product(product_id, quantity):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state='storage_state.json')
        page = await context.new_page()
        
        url = f"https://www.wildberries.ru/catalog/{product_id}/detail.aspx"
        await page.goto(url)
        logging.info(f"Opened product page: {url}")
        await asyncio.sleep(2)

        sizes = await extract_sizes(page)

        if sizes:
            logging.info("Sizes available, proceeding with size-based purchase.")
            await purchase_product_with_sizes(page, product_id, quantity)
        else:
            logging.info("No sizes available, proceeding with simple purchase.")
            await purchase_product_without_sizes(page, product_id, quantity)

        await browser.close()

async def purchaseCheck_confirm(db_url, original_table_name, quantity):
    global last_checked_id
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    original_table = Table(original_table_name, metadata, autoload_with=engine)

    new_product = session.execute(select(original_table).order_by(original_table.c.id.desc()).limit(1)).fetchone()

    if new_product is None:
        logging.info("Новые продукты не найдены.")
    else:
        product_id = new_product.product_id
        if product_id is None:
            logging.warning("Encountered product with None product_id: %s", new_product)
        elif product_id == last_checked_id:
            logging.info("Новые продукты не найдены.")
        else:
            product_id_str = str(product_id)
            logging.info(f"Attempting to purchase product: {product_id_str}")
            await purchase_product(product_id_str, quantity)
            logging.info(f"Purchased product: {product_id_str}")
            last_checked_id = product_id
            logging.info(f"Updated last_checked_id: {last_checked_id}")

    session.close()