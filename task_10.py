'''
Попробуйте оформить тесты из первого модуля в стиле unittest.

    Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
    Создайте новый файл
    Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
    Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
    Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
    Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
    Запустите получившиеся тесты из файла
    Просмотрите отчёт о запуске и найдите последнюю строчку
    Отправьте эту строчку в качестве ответа на это задание

Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.
'''
import unittest
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
driver.get('http://suninjuly.github.io/registration1.html')


class TestReg(unittest.TestCase):

    def test_form(self):
        driver.get('http://suninjuly.github.io/registration1.html')
        self.field = driver.find_elements_by_class_name('form-control')

        for item in self.field:
            item.send_keys('text')
        btn = driver.find_element_by_xpath('/html/body/div/form/button').click()
        result = driver.find_element_by_class_name('container').text
        self.assertEqual('Congratulations! You have successfully registered!', result), 'text'

    def test_for(self):
        driver.get('http://suninjuly.github.io/registration2.html')
        self.field = driver.find_elements_by_class_name('form-control')

        for item in self.field:
            item.send_keys('text')
        btn = driver.find_element_by_xpath('/html/body/div/form/button').click()
        result = driver.find_element_by_class_name('container9').text
        self.assertEqual('Congratulations! You have successfully registered!', result), 'text'

if __name__ == '__main__':
    unittest.main()