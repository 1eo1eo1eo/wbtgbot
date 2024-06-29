from alembic.config import Config
from alembic import command

databases = [
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfirst',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsersecond',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserthird',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfourth',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfifth',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsersixth',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserseventh',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsereighth',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsernineth',
    'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsertenth',
]

for db_url in databases:
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
    command.upgrade(alembic_cfg, "head")
