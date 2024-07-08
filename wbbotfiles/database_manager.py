from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker, scoped_session
from wbbotfiles.models import Base, ComparedProductsInstaBuyDuplicateTelegram, ParserStatus
import logging
   

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(self.engine)
        self.SessionFactory = sessionmaker(bind=self.engine)

    def product_exists(self, product_id, database):
        session = scoped_session(self.SessionFactory)
        try:
            exists_flag = session.query(exists().where(database.product_id == product_id)).scalar()
            return exists_flag
        except Exception as e:
            logging.error(f"Error checking if product exists: {e}")
            raise
        finally:
            session.close()

    def add_products(self, products, database):
        session = scoped_session(self.SessionFactory)
        try:
            new_products = [product for product in products if not self.product_exists(product.product_id, database)]
            if new_products:
                session.bulk_save_objects(new_products)
                session.commit()
            else:
                logging.info("No new products to add.")
        except Exception as e:
            session.rollback()
            logging.error(f"Failed to add products: {e}")
        finally:
            session.expire_all()
            session.close()

    def clear_table(self, database):
        session = scoped_session(self.SessionFactory)
        try:
            session.query(database).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f"Failed to clear table {database.__tablename__}: {e}")
        finally:
            session.close()

    def get_products(self, database):
        session = scoped_session(self.SessionFactory)
        try:
            products_query = session.query(database).all()
            products_list = [product for product in products_query]
            return products_list
        finally:
            session.close()

    def get_product_by_id(self, product_id):
        session = scoped_session(self.SessionFactory)
        try:
            product = session.query(ComparedProductsInstaBuyDuplicateTelegram).filter_by(product_id=product_id).first()
            return product
        finally:
            session.close()

    def get_product_ids_from_table(self, database):
        session = scoped_session(self.SessionFactory)
        try:
            products = session.query(database.product_id).all()
            return [product_id for (product_id,) in products]
        finally:
            session.close()

    def update_parser_status(self, parser_number, status):
        session = scoped_session(self.SessionFactory)
        try:
            parser_status = session.query(ParserStatus).filter_by(parser_number=parser_number).first()
            if parser_status:
                parser_status.status = status
            else:
                parser_status = ParserStatus(parser_number=parser_number, status=status)
                session.add(parser_status)
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f"Failed to update parser status: {e}")
        finally:
            session.close()

    def get_parser_status(self, parser_number):
        session = scoped_session(self.SessionFactory)
        try:
            parser_status = session.query(ParserStatus).filter_by(parser_number=parser_number).first()
            return parser_status
        finally:
            session.close()

    def update_parser_pid(self, parser_number, pid):
        session = scoped_session(self.SessionFactory)
        parser_status = session.query(ParserStatus).filter_by(parser_number=parser_number).first()
        if parser_status:
            parser_status.pid = pid
            session.commit()
            session.close()

    def clear_parser_pid(self, parser_number):
        session = scoped_session(self.SessionFactory)
        parser_status = session.query(ParserStatus).filter_by(parser_number=parser_number).first()
        if parser_status:
            parser_status.pid = None
            session.commit()
            session.close()

    def get_parser_status(self, parser_number):
        session = scoped_session(self.SessionFactory)
        return session.query(ParserStatus).filter_by(parser_number=parser_number).first()

class ManagerForTelegram:
    def __init__(self, db_url_1):
        self.engine1 = create_engine(db_url_1, pool_pre_ping=True)
        Base.metadata.create_all(self.engine1)
        self.SessionFactory1 = sessionmaker(bind=self.engine1)
        self.session1 = scoped_session(self.SessionFactory1)

    def get_products(self, database):
        session1 = scoped_session(self.SessionFactory1)
        try:
            products_query = session1.query(database).all()
            products_list = [product for product in products_query]
            return products_list
        finally:
            session1.close()

    def get_product_by_id(self, product_id, database):
        session1 = scoped_session(self.SessionFactory1)
        try:
            product = session1.query(database).filter_by(product_id=product_id).first()
            return product
        finally:
            session1.close()
    
    def clear_table(self, database):
        session1 = scoped_session(self.SessionFactory1)
        try:
            session1.query(database).delete()
            session1.commit()
        except Exception as e:
            session1.rollback()
            logging.error(f"Failed to clear table {database.__tablename__}: {e}")
        finally:
            session1.close()
