from sqlalchemy import exists, and_
from models import NewProduct, ComparedProductsInstaBuy, ComparedProductsInstaBuyDuplicateTelegram, ComparedProductsConfirmPurchase, ComparedProductsConfirmPurchaseDuplicate
from sqlalchemy.exc import SQLAlchemyError
from parser7.connect_csv_mysql import excel_data
import datetime
import pandas as pd

excel_data = excel_data.dropna(subset=['name', 'brand', 'basic_price'])

def product_already_compared(session1, product_id):
    return session1.query(exists().where(ComparedProductsInstaBuy.product_id == product_id)).scalar()


def compare_with_excel(excel_data, session1):
    if excel_data.empty:
        print("No data to process after removing missing values.")
        return

    product_names = excel_data['name'].unique()
    product_brands = excel_data['brand'].unique()
    products = session1.query(NewProduct).filter(
        NewProduct.name.in_(product_names),
        NewProduct.brand_name.in_(product_brands)
    ).all()

    for product in products:
        relevant_rows = excel_data[
            (excel_data['name'] == product.name) &
            (excel_data['brand'] == product.brand_name)
        ]
        for _, row in relevant_rows.iterrows():
            price_percentage = product.price / row['basic_price'] * 100
            """ if 1 <= price_percentage <= 2:
                if not session1.query(exists().where(ComparedProductsInstaBuy.product_id == product.product_id)).scalar():
                    compared_products_insta_buy = ComparedProductsInstaBuy(
                        product_id=product.product_id,
                        name=product.name,
                        brand_name=product.brand_name,
                        price=product.price,
                        url_name=product.url_name,
                        image_url=row['url_image'] if 'url_image' in row else None,
                        category=row['category'] if pd.notna(row['category']) else None,
                        dateadd=datetime.datetime.now()
                    )
                    session1.add(compared_products_insta_buy) """
            if 1 <= price_percentage <= 30:
                if not session1.query(exists().where(ComparedProductsConfirmPurchase.product_id == product.product_id)).scalar():
                    compared_producs_confirm_purchase = ComparedProductsConfirmPurchase(
                        product_id=product.product_id,
                        name=product.name,
                        brand_name=product.brand_name,
                        price=product.price,
                        url_name=product.url_name,
                        image_url=row['url_image'] if 'url_image' in row else None,
                        category=row['category'] if pd.notna(row['category']) else None,
                        dateadd=datetime.datetime.now(),
                        parser_number=1
                    )
                    session1.add(compared_producs_confirm_purchase)
    try:
        session1.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        session1.rollback()
    finally:
        session1.close()
