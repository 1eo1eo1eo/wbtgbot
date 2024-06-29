from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models import Base
from models import ParserStatus, ComparedProductsInstaBuy, NewProduct, ComparedProductsInstaBuyDuplicateTelegram, ComparedProductsInstaBuyDuplicate, ComparedProductsConfirmPurchaseDuplicate, ComparedProductsConfirmPurchase


db_url = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfirst'
engine = create_engine(db_url, pool_pre_ping=True)
Base.metadata.create_all(engine)
SessionFactory = sessionmaker(bind=engine)
session1 = scoped_session(SessionFactory)


results = session1.query(NewProduct).all()
new_product = NewProduct(name='Шорты спортивные женские 2в1 для бега фитнеса', brand_name='Skins', product_id='50562759', price=1500, url_name='https://www.wildberries.ru/catalog/50562759/detail.aspx')

product_to_delete = session1.query(NewProduct).filter_by(product_id='50562759').first()


session1.add(new_product)
session1.commit() 


""" if product_to_delete:
    session1.delete(product_to_delete)
    session1.commit()
else:
    print("Product not found") """


for result in results:
    print(f"ID: {result.id}, Name: {result.name}, Brand_Name: {result.brand_name}, Price: {result.price}, Product_Id: {result.product_id}, Url: {result.url_name}")

session1.close()
