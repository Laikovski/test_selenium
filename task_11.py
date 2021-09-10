import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r'driver/chromedriver')
    yield browser
    print("\nquit browser..")
    browser.quit()

lst = ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']

@pytest.mark.parametrize('lst', lst)
def test_guest_should_see_login_link(browser, lst):

    # link = 'https://stepik.org/lesson/236905/step/1'
    browser.get(lst)

    enter_field = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
    )
    answer = str(math.log(int(time.time())))
    enter_field.send_keys(answer)

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    feedback = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    )

    assert feedback.text == 'Correct!', f'{feedback.text}'