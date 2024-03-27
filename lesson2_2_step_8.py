from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//label[text()='First name* ']/following-sibling::input")
    input1.send_keys("Artem")
    input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
    input2.send_keys("Lobzov")
    input3 = browser.find_element(By.XPATH, "//label[text()='Email * ']/following-sibling::input")
    input3.send_keys("test@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'passwords.txt')  # добавляем к этому пути имя файла
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()