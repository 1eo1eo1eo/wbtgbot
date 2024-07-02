DB_URL_FIRST = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfirst'
DB_URL_SECOND = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsersecond'
DB_URL_THIRD = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserthird'
DB_URL_FOURTH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfourth'
DB_URL_FIFTH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserfifth'
DB_URL_SIXTH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsersixth'
DB_URL_SEVENTH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parserseventh'
DB_URL_EIGHTH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsereighth'
DB_URL_NINETH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsernineth'
DB_URL_TENTH = 'mysql+mysqlconnector://wbbot:Wbbot12345!@mysql:3306/parsertenth'

CHAT_IDS = {"1111741813"} #, "525119691", "5162952042", "599786558", "5246704356"

PARSER_SCRIPTS = {
    1: {
        "start": "/app/parser1/start_main.sh",
        "stop": "/app/parser1/stop_main.sh"
    },
    2: {
        "start": "/app/parser2/start_main.sh",
        "stop": "/app/parser2/stop_main.sh"
    },
    3: {
        "start": "/app/parser3/start_main.sh",
        "stop": "/app/parser3/stop_main.sh"
    },
    4: {
        "start": "/app/parser4/start_main.sh",
        "stop": "/app/parser4/stop_main.sh"
    },
    5: {
        "start": "/app/parser5/start_main.sh",
        "stop": "/app/parser5/stop_main.sh"
    },
    6: {
        "start": "/app/parser6/start_main.sh",
        "stop": "/app/parser6/stop_main.sh"
    },
    7: {
        "start": "/app/parser7/start_main.sh",
        "stop": "/app/parser7/stop_main.sh"
    },
    8: {
        "start": "/app/parser8/start_main.sh",
        "stop": "/app/parser8/stop_main.sh"
    },
    9: {
        "start": "/app/parser9/start_main.sh",
        "stop": "/app/parser9/stop_main.sh"
    },
    10: {
        "start": "/app/parser10/start_main.sh",
        "stop": "/app/parser10/stop_main.sh"
    },
}

PID_FILE_PATHS = {
    1: '/app/main_pid1.txt',
    2: '/app/main_pid2.txt',
    3: '/app/main_pid3.txt',
    4: '/app/main_pid4.txt',
    5: '/app/main_pid5.txt',
    6: '/app/main_pid6.txt',
    7: '/app/main_pid7.txt',
    8: '/app/main_pid8.txt',
    9: '/app/main_pid9.txt',
    10: '/app/main_pid10.txt',
}

PRODUCT_TEMPLATE = """
<b>💬 Название:</b> {product.name}
<b>💬 Название бренда:</b> {product.brand_name}
<b>💬 Цена:</b> {product.price}
<b>💬 Артикул:</b> {product.product_id}
<b>💬 Ссылка:</b> {product.url_name}
<b>💬 Категория:</b> {product.category}
"""

PURCHASE_TEMPLATE = """
<b> КУПЛЕН ТОВАР</b>
<b>💬 Название:</b> {product.name}
<b>💬 Название бренда:</b> {product.brand_name}
<b>💬 Цена:</b> {product.price}
<b>💬 Артикул:</b> {product.product_id}
<b>💬 Ссылка:</b> {product.url_name}
<b>💬 Категория:</b> {product.category}
"""

CONFIRM_BUY_TEMPLATE = """
<b> НАЙДЕН ТОВАР</b>
<b>💬 Название:</b> {product.name}
<b>💬 Название бренда:</b> {product.brand_name}
<b>💬 Цена:</b> {product.price}
<b>💬 Артикул:</b> {product.product_id}
<b>💬 Ссылка:</b> {product.url_name}
<b>💬 Категория:</b> {product.category}
"""

STATUS_TEMPLATE = """
<b>📊 Статус парсера {parser_number}</b>
<b>🔢 Номер:</b> {parser_number}
<b>🛠 Статус:</b> {status}
<b>📂 Категория:</b> {category}
"""
