# pytest для параметризации
import pytest

# импорт исключения, чтоб отлавливать случаи, когда элемент не найден
from selenium.common.exceptions import NoSuchElementException


# получение ссылок из файла
links = []
with open("links.txt", 'r') as file:
    links = file.readlines()


@pytest.mark.parametrize( "link", links)
def test_button_add_to_basket_must_be_visible(browser, link):
    browser.get(link)

    # расскоментируйте строку ниже для визуальной проверки
    # import time; time.sleep(10)

    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except (NoSuchElementException):
        assert False, "Кнопка для добавления товара в корзину не найдена."