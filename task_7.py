'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/alert_accept.html
    Нажать на кнопку
    Принять confirm
    На новой странице решить капчу для роботов, чтобы получить число с ответом

'''
import math
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
driver.get('http://suninjuly.github.io/alert_accept.html')



driver.find_element_by_xpath('/html/body/form/div/div/button').click()
time.sleep(1)
confirm = driver.switch_to.alert
confirm.accept()

time.sleep(1)
x = driver.find_element_by_id('input_value').text
res = str(math.log(abs(12*math.sin(int(x)))))

inp = driver.find_element_by_id('answer')
inp.send_keys(res)


button = driver.find_element_by_xpath('/html/body/form/div/div/button').click()