from typing_extensions import Self
from unittest import TestCase
from unittest import main as unittest_main
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

RESULT = "Congratulations! You have successfully registered!"


class Test(TestCase):
    def test1(self: Self) -> None:
        result = test("http://suninjuly.github.io/registration1.html")
        self.assertEqual(result, RESULT)

    def test2(self: Self) -> None:
        result = test("http://suninjuly.github.io/registration2.html")
        self.assertEqual(result, RESULT)


def test(link: str) -> str:
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        input1.send_keys("Artem")
        input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        input2.send_keys("Lobzov")
        input3 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        input3.send_keys("test@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        return welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest_main()
