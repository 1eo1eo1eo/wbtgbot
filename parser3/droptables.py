from sqlalchemy import create_engine
from models import Product2, NewProduct, ComparedProductsInstaBuy
from database_manager import Base

# Создайте движок SQLAlchemy, соединяющийся с вашей базой данных
engine = create_engine('mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserthird')

# Удаление конкретной таблицы
NewProduct.__table__.drop(engine)
