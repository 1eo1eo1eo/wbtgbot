from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_commands_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Управление парсерами", callback_data="manage_parsers")],
        [InlineKeyboardButton(text="Статус всех парсеров", callback_data="get_status_all_parsers")],
        [InlineKeyboardButton(text="Запуск всех парсеров", callback_data="start_all_parsers")],
        [InlineKeyboardButton(text="Остановка всех парсеров", callback_data="stop_all_parsers")],
    ])

def create_parsers_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Парсер 'Женщинам/Платья'", callback_data="manage_parser1")],
        [InlineKeyboardButton(text="Парсер 'Женщинам/Сарафаны'", callback_data="manage_parser2")],
        [InlineKeyboardButton(text="Парсер 'Женщинам/Верхняя одежда/Косухи'", callback_data="manage_parser3")],
        [InlineKeyboardButton(text="Парсер 'Женщинам/Юбки'", callback_data="manage_parser4")],
        [InlineKeyboardButton(text="Парсер 'Женщинам/Юбки/Шорты'", callback_data="manage_parser5")],
        [InlineKeyboardButton(text="Парсер 'Женщины/Джинсы/Джинсы'", callback_data="manage_parser6")],
        [InlineKeyboardButton(text="Парсер 'Женщины/Брюки/Брюки'", callback_data="manage_parser7")],
        [InlineKeyboardButton(text="Парсер 'Женщины/Брюки/Леггинсы'", callback_data="manage_parser8")],
        [InlineKeyboardButton(text="Парсер 'Женщины/Блузки и рубашки/Рубашка'", callback_data="manage_parser9")],
        [InlineKeyboardButton(text="Парсер 'Женщины/Пиджаки, жилеты и жакеты/Пиджаки'", callback_data="manage_parser10")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_main")]
    ])

def create_parser1_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщинам/Платья'", callback_data="start_parser1")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Платья'", callback_data="stop_parser1")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Платья' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщинам/Платья'", callback_data="status_parser1")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser2_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщинам/Сарафаны'", callback_data="start_parser2")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Сарафаны'", callback_data="stop_parser2")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Сарафаны' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщинам/Сарафаны'", callback_data="status_parser2")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser3_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщинам/Верхняя одежда/Косухи'", callback_data="start_parser3")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Верхняя одежда/Косухи'", callback_data="stop_parser3")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Верхняя одежда/Косухи' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщинам/Верхняя одежда/Косухи'", callback_data="status_parser3")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser4_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщинам/Юбки'", callback_data="start_parser4")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Юбки'", callback_data="stop_parser4")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Юбки' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщинам/Юбки'", callback_data="status_parser4")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser5_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщинам/Юбки/Шорты'", callback_data="start_parser5")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Юбки/Шорты'", callback_data="stop_parser5")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщинам/Юбки/Шорты' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщинам/Юбки/Шорты'", callback_data="status_parser5")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser6_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщины/Джинсы/Джинсы'", callback_data="start_parser6")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Джинсы/Джинсы'", callback_data="stop_parser6")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Джинсы/Джинсы' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщины/Джинсы/Джинсы'", callback_data="status_parser6")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser7_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщины/Брюки/Брюки'", callback_data="start_parser7")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Брюки/Брюки'", callback_data="stop_parser7")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Брюки/Брюки' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщины/Брюки/Брюки'", callback_data="status_parser7")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser8_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщины/Брюки/Леггинсы'", callback_data="start_parser8")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Брюки/Леггинсы'", callback_data="stop_parser8")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Брюки/Леггинсы' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщины/Брюки/Леггинсы'", callback_data="status_parser8")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser9_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщины/Блузки и рубашки/Рубашка'", callback_data="start_parser9")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Блузки и рубашки/Рубашка'", callback_data="stop_parser9")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Блузки и рубашки/Рубашка' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщины/Блузки и рубашки/Рубашка'", callback_data="status_parser9")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser10_controls(enable_stop=False):
    buttons = [
        [InlineKeyboardButton(text="Запустить парсер 'Женщины/Пиджаки, жилеты и жакеты/Пиджаки'", callback_data="start_parser10")]
    ]
    if enable_stop:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Пиджаки, жилеты и жакеты/Пиджаки'", callback_data="stop_parser10")])
    else:
        buttons.append([InlineKeyboardButton(text="Остановить парсер 'Женщины/Пиджаки, жилеты и жакеты/Пиджаки' (Недоступно)", callback_data="stop_parser_disabled")])
    buttons.append([InlineKeyboardButton(text="Статус парсера 'Женщины/Пиджаки, жилеты и жакеты/Пиджаки'", callback_data="status_parser10")])
    buttons.append([InlineKeyboardButton(text="Назад", callback_data="back_to_parsers")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def create_parser_controls(parser_number, enable_stop=False):
    if parser_number == 1:
        return create_parser1_controls(enable_stop)
    elif parser_number == 2:
        return create_parser2_controls(enable_stop)
    elif parser_number == 3:
        return create_parser3_controls(enable_stop)
    elif parser_number == 4:
        return create_parser4_controls(enable_stop)
    elif parser_number == 5:
        return create_parser5_controls(enable_stop)
    elif parser_number == 6:
        return create_parser6_controls(enable_stop)
    elif parser_number == 7:
        return create_parser7_controls(enable_stop)
    elif parser_number == 8:
        return create_parser8_controls(enable_stop)
    elif parser_number == 9:
        return create_parser9_controls(enable_stop)
    elif parser_number == 10:
        return create_parser10_controls(enable_stop)
