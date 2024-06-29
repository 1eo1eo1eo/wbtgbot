from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product1(Base):
    __tablename__ = 'pars_table1'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    brand_name = Column(String(255), nullable=False, index=True)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False, index=True)
    url_name = Column(String(255), nullable=False, index=True)


class Product2(Base):
    __tablename__ = 'pars_table2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    brand_name = Column(String(255), nullable=False, index=True)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False, index=True)
    url_name = Column(String(255), nullable=False, index=True)


class ComparedProductsInstaBuy(Base):
    __tablename__ = 'compared_products_insta_buy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=False)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False)
    url_name = Column(String(255), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)
    category = Column(String(255))
    dateadd = Column(DateTime)


class ComparedProductsInstaBuyDuplicate(Base):
    __tablename__ = 'compared_products_insta_buy_duplicate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=False)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False)
    url_name = Column(String(255), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)
    category = Column(String(255))
    dateadd = Column(DateTime)


class ComparedProductsInstaBuyDuplicateTelegram(Base):
    __tablename__ = 'compared_products_insta_buy_duplicate_telegram'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=False)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False)
    url_name = Column(String(255), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)
    category = Column(String(255))
    dateadd = Column(DateTime)

class ComparedProductsConfirmPurchase(Base):
    __tablename__ = 'compared_products_confirm_purchase'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=False)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False)
    url_name = Column(String(255), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)
    category = Column(String(255))
    dateadd = Column(DateTime)
    parser_number = Column(Integer)

class ComparedProductsConfirmPurchaseDuplicate(Base):
    __tablename__ = 'compared_products_confirm_purchase_duplicate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=False)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False)
    url_name = Column(String(255), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)
    category = Column(String(255))
    dateadd = Column(DateTime)
    parser_number = Column(Integer)

class ComparedProductsConfirmPurchaseDuplicateTelegram(Base):
    __tablename__ = 'compared_products_confirm_purchase_duplicate_telegram'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    brand_name = Column(String(255), nullable=False)
    product_id = Column(Integer, unique=True)
    price = Column(Integer, nullable=False)
    url_name = Column(String(255), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)
    category = Column(String(255))
    dateadd = Column(DateTime)
    parser_number = Column(Integer)
    

class NewProduct(Base):
    __tablename__ = 'new_product_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    brand_name = Column(String(255), nullable=False, index=True)
    product_id = Column(Integer, unique=True, index=True)
    price = Column(Integer, nullable=False, index=True)
    url_name = Column(String(255), nullable=False, index=True)


class ParserStatus(Base):
    __tablename__ = 'parsers_status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    parser_number = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
    category = Column(String(255), nullable=False)