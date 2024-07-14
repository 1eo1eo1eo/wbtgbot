from sqlalchemy import create_engine, Table, select, and_
from sqlalchemy.orm import sessionmaker
import logging
from .models import Base

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def update_new_products_table(db_url, original_table_name, comparison_table_name, new_products_table_name):
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    metadata = Base.metadata

    Session = sessionmaker(bind=engine)
    session = Session()

    original_table = Table(original_table_name, metadata, autoload_with=engine)
    comparison_table = Table(comparison_table_name, metadata, autoload_with=engine)
    new_products_table = Table(new_products_table_name, metadata, autoload_with=engine)

    original_first = session.execute(select(original_table)).fetchone()
    comparison_first = session.execute(select(comparison_table)).fetchone()

    if original_first and comparison_first and original_first.product_id == comparison_first.product_id:
        logging.info("Первые product_ids совпадают, обновление не требуется.")
    else:
        logging.info("Первые product_id различаются, проверяем наличие в таблице новых товаров.")
        existing_product = session.execute(select(new_products_table).where(new_products_table.c.product_id == original_first.product_id)).fetchone()
        
        if existing_product:
            logging.info(f"Товар с product_id {original_first.product_id} уже существует. Вставка пропускается.")
        else:
            logging.info("Вставка новой записи.")
            ins = new_products_table.insert().values(
                id=original_first.id, 
                name=original_first.name,
                brand_name=original_first.brand_name,
                product_id=original_first.product_id,
                price=original_first.price,
                url_name=original_first.url_name,
            )
            session.execute(ins)
            session.commit()

    session.close()