from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
import time

#Данные для авторизации: 
#Имя: Ivan Организация: Autotest email: 01.01ivanpetrov1990@mail.ru Пароль: test123

#Позитивная проверка. Ввод валидных значений
try:
    browser = webdriver.Chrome()
    browser.get("https://www.izi.travel/ru")

    #Переход на страницу Вход
    enter = browser.find_element(By.CSS_SELECTOR, "li.navigation__item:nth-child(5) > a:nth-child(1)") 
    #enter = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/ul/li[5]/a") 
    enter.click() 

    #Заполнение поля email
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.send_keys("01.01ivanpetrov1990@mail.ru")

    #Ввод пароля
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.send_keys("test123")

    #Выбор чек-бокса Запомнить меня
    browser.execute_script("document.getElementById('user_remember_me').checked = true")

    #Клик на кнопку Войди в систему
    button_enter = browser.find_element(By.CLASS_NAME, "btn")
    button_enter.click()

    time.sleep(2)
    #Открываем выпадающий список с опциями профиля
    profile = browser.find_element(By.CLASS_NAME, "dropdown")
    profile.click()

    #Выход из профиля
    exit = browser.find_element(By.LINK_TEXT, "Выход")
    exit.click()

finally:
    time.sleep(3)

#Негативная проверка 1
#Ввод несуществующей почты в поле Email. Тестовые данные petrovivan@mail.ru
try:
    #Заполнение поля email. Тестовые данные petrovivan@mail.ru
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.send_keys("petrovivan@mail.ru")

    #Ввод пароля
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.send_keys("test123")

    #Выбор чек-бокса Запомнить меня
    browser.execute_script("document.getElementById('user_remember_me').checked = true")

    #Клик на кнопку Войди в систему
    button_enter = browser.find_element(By.CLASS_NAME, "btn")
    button_enter.click()

    text1 = browser.find_element(By.XPATH, '//*[@id="gritter-item-1"]/div[2]/div[2]/p').text
    text2 = "Неверное имя пользователя или пароль."

    if text1 == text2:
        print("Тест №1 пройден")

finally:
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.clear()
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.clear()

#Негативная проверка 2
#Ввод пустое поле Email. Тестовые данные 
try:
    #Заполнение поля email. Тестовые данные " "
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.send_keys(" ")

    #Ввод пароля
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.send_keys("test123")

    #Выбор чек-бокса Запомнить меня
    browser.execute_script("document.getElementById('user_remember_me').checked = true")

    #Клик на кнопку Войди в систему
    button_enter = browser.find_element(By.CLASS_NAME, "btn")
    button_enter.click()

    text1 = browser.find_element(By.XPATH, '//*[@id="gritter-item-1"]/div[2]/div[2]/p').text
    text2 = "Неверное имя пользователя или пароль."

    if text1 == text2:
        print("Тест №2 пройден")

finally:
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.clear()
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.clear()


#Негативная проверка №3
#Ввод невалидных данных в поле Пароль. Тестовые данные "123test"
try:
    #Заполнение поля email. 
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.send_keys("01.01ivanpetrov1990@mail.ru")

    #Ввод пароля. Тестовые данные "123test"
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.send_keys("123test")

    #Выбор чек-бокса Запомнить меня
    browser.execute_script("document.getElementById('user_remember_me').checked = true")

    #Клик на кнопку Войди в систему
    button_enter = browser.find_element(By.CLASS_NAME, "btn")
    button_enter.click()

    text1 = browser.find_element(By.XPATH, '//*[@id="gritter-item-1"]/div[2]/div[2]/p').text
    text2 = "Неверное имя пользователя или пароль."

    if text1 == text2:
        print("Тест №3 пройден")

finally:
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.clear()
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.clear()

#Негативная проверка №4
#Пустое поле Пароль. Тестовые данные " "
try:
    #Заполнение поля email. 
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.send_keys("01.01ivanpetrov1990@mail.ru")

    #Ввод пароля. Тестовые данные " "
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.send_keys(" ")

    #Выбор чек-бокса Запомнить меня
    browser.execute_script("document.getElementById('user_remember_me').checked = true")

    #Клик на кнопку Войди в систему
    button_enter = browser.find_element(By.CLASS_NAME, "btn")
    button_enter.click()

    text1 = browser.find_element(By.XPATH, '//*[@id="gritter-item-1"]/div[2]/div[2]/p').text
    text2 = "Неверное имя пользователя или пароль."

    if text1 == text2:
        print("Тест №3 пройден")

finally:
    auth_email = browser.find_element(By.ID, "user_email")
    auth_email.clear()
    auth_password = browser.find_element(By.ID, "user_password")
    auth_password.clear()

    browser.quit()
