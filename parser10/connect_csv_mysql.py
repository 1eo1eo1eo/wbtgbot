import pandas as pd
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models import Base
from constants import DB_URL_FIRST


db_url = DB_URL_FIRST
engine = create_engine(db_url, pool_pre_ping=True)
Base.metadata.create_all(engine)
SessionFactory = sessionmaker(bind=engine)
session1 = scoped_session(SessionFactory)

xlsx_file_path = 'exceltables/10.xlsx'
excel_data = pd.read_excel(xlsx_file_path)

