from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models import Base
from models import ComparedProductsInstaBuy, NewProduct, ComparedProductsInstaBuyDuplicateTelegram, ComparedProductsInstaBuyDuplicate, ComparedProductsConfirmPurchaseDuplicate, ComparedProductsConfirmPurchase


db_url = 'mysql+mysqlconnector://wbbot:Wbbot12345!@localhost:3306/parserthird'
engine = create_engine(db_url)
Base.metadata.create_all(engine)
SessionFactory = sessionmaker(bind=engine)
session1 = scoped_session(SessionFactory)


results = session1.query(NewProduct).all()
new_product = NewProduct(name='Шорты', brand_name='ANNA PEKUN', product_id='191765972', price=800, url_name='https://www.wildberries.ru/catalog/191765972/detail.aspx')

product_to_delete = session1.query(NewProduct).filter_by(product_id='151212744').first()


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
