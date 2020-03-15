# Задание по курсу [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/syllabus)

Тест проверяет **наличие** на странице кнопки добавления в корзину (кнопка может быть не видна сразу).

Список проверяемых страниц хранится в links.txt, каждая ссылка на отдельной строке.

Параметры запуска по умолчанию: браузер - Chrome, язык - en.

Пример запуска теста:

    pytest -sv --tb=short --browser_name=chrome --language=es test_items.py
    pytest  --language=es
