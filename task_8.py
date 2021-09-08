'''
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

    Открыть страницу http://suninjuly.github.io/redirect_accept.html
    Нажать на кнопку
    Переключиться на новую вкладку
    Пройти капчу для робота и получить число-ответ


'''
import math

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
driver.get('http://suninjuly.github.io/redirect_accept.html')

#click_bitton
first = driver.window_handles[0]
btn = driver.find_element_by_class_name('trollface').click()
second = driver.window_handles[1]
window = driver.switch_to.window(second)

x = driver.find_element_by_id('input_value').text
res = str(math.log(abs(12*math.sin(int(x)))))

answer = driver.find_element_by_id('answer').send_keys(res)
button = driver.find_element_by_xpath('/html/body/form/div/div/button').click()