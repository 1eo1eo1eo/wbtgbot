from sqlalchemy import create_engine, MetaData, Table, select, inspect, Column
import logging

def duplicate_table(original_table_name, new_table_name, db_url, product_id_set, condition=None):
    engine = create_engine(db_url, pool_pre_ping=True)
    metadata = MetaData()

    original_table = Table(original_table_name, metadata, autoload_with=engine)

    inspector = inspect(engine)
    if inspector.has_table(new_table_name):
        new_table = Table(new_table_name, metadata, autoload_with=engine)
        new_table.drop(engine)
        metadata.remove(new_table)

    new_table = Table(new_table_name, metadata)
    for column in original_table.columns:
        new_column = Column(column.name, column.type, primary_key=column.primary_key, nullable=column.nullable)
        new_table.append_column(new_column)

    new_table.create(engine)

    with engine.connect() as conn:
        if condition:
            select_stmt = select(original_table).where(condition)
        else:
            select_stmt = select(original_table)
        
        results = conn.execute(select_stmt)
        data_to_insert = []
        for row in results:
            product_id = row._mapping.get('product_id')
            if product_id is None:
                logging.warning("Encountered row with None product_id: %s", row)
                continue
            if product_id not in product_id_set:
                data_to_insert.append(dict(row._mapping))
                product_id_set.add(product_id)

        if data_to_insert:
            insert_stmt = new_table.insert().values(data_to_insert)
            conn.execute(insert_stmt)
            conn.commit()
        else:
            logging.info("Duplicate: Нет данных для вставки.")
