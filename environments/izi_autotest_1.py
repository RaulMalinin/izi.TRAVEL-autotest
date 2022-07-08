from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://www.izi.travel/ru")

    #Проверка перехода на страницу поиска аудиогида при клике на "аудиогиды"
    audioguides = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[1]/a")   
    audioguides.click()

    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL
    izi_logo = browser.find_element_by_link_text("izi.TRAVEL")
    izi_logo.click()

    #Проверка перехода на страницу создания аудиогида при клике на "создайте аудиогид"
    create_audio = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[2]/a")
    create_audio.click()

    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL
    izi_logo = browser.find_element_by_link_text("izi.TRAVEL")
    izi_logo.click()

    #Проверка перехода на страницу информации о нас при клике на "о нас"
    about_us = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[3]/a")
    about_us.click()

    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL
    izi_logo = browser.find_element_by_link_text("izi.TRAVEL")
    izi_logo.click()

    #Проверка перехода на страницу api при клике на "api"
    api = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[4]/a")
    api.click()

    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL
    izi_logo = browser.find_element_by_link_text("izi.TRAVEL")
    izi_logo.click()

    #Проверка перехода на страницу авторизации аудиогида при клике на "вход"
    enter = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[5]/a")
    enter.click()

    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL
    izi_logo = browser.find_element_by_link_text("izi.TRAVEL")
    izi_logo.click()

    #Проверка перехода на страницу спецпредложения аудиогида при клике на "спецпредложения"
    offer = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[6]/a")
    offer.click()

    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL
    izi_logo = browser.find_element_by_link_text("izi.TRAVEL")
    izi_logo.click()
    
    #Проверка появления выпадающего списка при клике на "RU"
    language_ru = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[7]/form/div/div/div[1]/abbr")
    language_ru.click()

    #Проверка сокрытия выпадающего списка языков при клике в другом месте страницы
    nav_cont = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div")
    time.sleep(2)
    nav_cont.click()

    #Проверка появления выпадающего списка при клике на "стрелку"
    language_arrow = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[7]/form/div/div/div[1]")
    language_arrow.click()    

    #Проверка сокрытия выпадающего списка языков при клике в другом месте страницы
    nav_cont = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div")
    time.sleep(2)
    nav_cont.click()      

    #Проверка открытия бокового гамбургер-меню
    hamburger = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/button")               
    hamburger.click()

    
    z = browser.find_element(By.CLASS_NAME, "navigation_close")               
    z.click()               


    #Проверка перехода на стартовую страницу при клике на лого izi.TRAVEL в боковом меню
    #izi_logo_ham = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/button")
    #izi_logo_ham.click()                           



finally:
    time.sleep(30)
    browser.quit()
