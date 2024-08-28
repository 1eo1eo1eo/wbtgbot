from playwright.sync_api import sync_playwright
import time


def save_storage_state():
    url = "https://www.wildberries.ru/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='storage_state.json')
        page = context.new_page()
        page.goto(url)

        """ signin = page.wait_for_selector('text="Войти"')
        signin.click()
        phone_enter = page.wait_for_selector('.input-item')
        phone_enter.fill("phone number")
        phone_enter.press("Enter") """

        input("Введите код авторизации в открытом браузере и нажмите Enter здесь, чтобы продолжить...")

        """ context.storage_state(path='storage_state.json') """

        browser.close()

if __name__ == '__main__':
    save_storage_state()
