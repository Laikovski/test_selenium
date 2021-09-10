'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100,
 используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
'''
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
driver.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "100")
    )

button = driver.find_element_by_id('book').click()

x = driver.find_element_by_id('input_value').text
res = str(math.log(abs(12*math.sin(int(x)))))

answer = driver.find_element_by_id('answer').send_keys(res)
button_1 = driver.find_element_by_id('solve').click()

