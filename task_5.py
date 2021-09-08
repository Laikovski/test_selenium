import math
import time

from selenium import webdriver

'''

    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".

'''

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
driver.get('https://SunInJuly.github.io/execute_script.html')

x_element = driver.find_element_by_id('input_value').text
res = calc(x_element)
insert_value = driver.find_element_by_id('answer').send_keys(str(res))

time.sleep(1)
driver.execute_script("window.scrollTo(0, 300)")

robot = driver.find_element_by_id('robotCheckbox').click()
check = driver.find_element_by_css_selector('[for="robotsRule"]').click()

button = driver.find_element_by_xpath('/html/body/div/form/button').click()