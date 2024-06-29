from sqlalchemy import create_engine, MetaData, Table, select
import logging

def add_new_product_if_not_exists(original_table_name, new_table_name, db_url, product_id_set):
    engine = create_engine(db_url, pool_pre_ping=True)
    metadata = MetaData()

    original_table = Table(original_table_name, metadata, autoload_with=engine)
    new_table = Table(new_table_name, metadata, autoload_with=engine)

    try:
        with engine.begin() as conn:
            select_stmt = select(original_table)
            results = conn.execute(select_stmt)
            data_to_insert = []
            for row in results:
                product_id = row._mapping.get('product_id')
                if product_id is None:
                    continue
                if product_id not in product_id_set:
                    data_to_insert.append(dict(row._mapping))
                    product_id_set.add(product_id)

            if data_to_insert:
                conn.execute(new_table.insert().values(data_to_insert))
                
    except Exception as e:
        logging.error(f"Error during table update: {e}")
