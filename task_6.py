from selenium import webdriver
import os
'''

Напишите скрипт, который будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"


'''



driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
driver.get('http://suninjuly.github.io/file_input.html')

f_name = driver.find_element_by_css_selector('[name="firstname"]')
f_name.send_keys('Eugene')

f_name = driver.find_element_by_css_selector('[name="lastname"]')
f_name.send_keys('Laikov')

email = driver.find_element_by_css_selector('[name="email"]')
email.send_keys('zheka-se@ya.ru')

file = os.path.abspath('text.txt')

add_file = driver.find_element_by_id('file')
add_file.send_keys(file)

button = driver.find_element_by_xpath('/html/body/div/form/button')
button.click()