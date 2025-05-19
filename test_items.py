from selenium.webdriver.common.by import By
import time


# Ссылка на тестируемую страницу товара
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_present(browser):
    """Проверка наличия кнопки 'Добавить в корзину' на странице товара.

    Шаги теста:
    1. Открываем страницу товара
    2. Проверяем наличие кнопки добавления в корзину
    3. Убеждаемся, что кнопка видима и активна

    Аргументы:
        browser: Экземпляр WebDriver из фикстуры.
    """
    # 1. Открываем страницу товара
    browser.get(LINK)

    # Пауза для визуальной проверки языка (можно убрать в продакшн)
    time.sleep(30)

    # 2. Ищем кнопку добавления в корзину
    add_to_cart_button = browser.find_element(
        By.CSS_SELECTOR,
        "button.btn-add-to-basket"
    )

    # 3. Проверочные утверждения
    assert add_to_cart_button.is_displayed(), (
        "Кнопка 'Добавить в корзину' должна быть видимой на странице"
    )
    assert add_to_cart_button.is_enabled(), (
        "Кнопка 'Добавить в корзину' должна быть кликабельной"
    )
