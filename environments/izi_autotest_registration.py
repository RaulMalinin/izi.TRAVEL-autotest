from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Данные для регистрации: 
#Имя: Ivan Организация: Autotest email: 01.01ivanpetrov1990@mail.ru Пароль: test123

#Позитивная проверка. Ввод валидных значений
try:
    browser = webdriver.Chrome()
    browser.get("https://www.izi.travel/ru")

    #Переход на страницу Вход
    enter = browser.find_element(By.CSS_SELECTOR, "li.navigation__item:nth-child(5) > a:nth-child(1)") 
    #enter = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/ul/li[5]/a") 
    enter.click() 

    #Переход на страницу Регистрация
    registration = browser.find_element(By.CLASS_NAME, "registration-link")
    registration.click()

    #Заполнение поля Имя
    reg_name = browser.find_element(By.ID, "registration_user_name")
    reg_name.send_keys("Ivan")

    #Заполнение поля Организация
    reg_org = browser.find_element(By.ID, "registration_content_provider_name")
    reg_org.send_keys("Autotest")

    #Заполнение поля email
    reg_email = browser.find_element(By.ID, "registration_user_email")
    reg_email.send_keys("01.01ivanpetrov1990@mail.ru")

    #Переход на следующую страницу при клике на кнопу Далее
    button_next1 = browser.find_element(By.CLASS_NAME, "btn-next")
    button_next1.click()

    #Выбор чек-бокса для согласия с Условиями
    #Так чек-бокс скрыт приходится использовать JS
    browser.execute_script("document.getElementById('registration_confirm').checked = true")


    time.sleep(5)
    #Кликаем на кнопку Далее
    button_next2 = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/form/div[4]/div[2]/button")
    button_next2.click()                         

finally:
    time.sleep(10)
    browser.quit()
