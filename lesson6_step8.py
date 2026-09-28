from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ссылка на первую (рабочую) страницу
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля (Имя, Фамилия, Email)
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys("test@test.com")

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что регистрация прошла успешно
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations" in welcome_text, "Регистрация не прошла"

finally:
    # Небольшая задержка, чтобы успеть увидеть результат
    time.sleep(5)
    browser.quit()