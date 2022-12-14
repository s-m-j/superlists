from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Василий узнал о новом онлайн приложении списка дел.
        # Он заходит на домашнюю страницу приложения
        self.browser.get('http://localhost:8000')
        # Он видит что в заголовке приложения упоминается 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # Василий видит приглашение ввести заметку
        # он вводит "Купить павлиньи перья" в текстовое поле ввода (Василий рыбак и его хобби изготовление приманок)
        # Когда Василий нажимает Ввод, страница обновляется и в списке дел появилась надпись
        # "1: Купить павлиньи перья"
        # Поле ввода остается на странице и доступно для ввода. Василий вводит
        # "Использовать перья для изготовления приманки" (он очень педантичен)
        # Страница снова обновляется, и показывает новые элементы списка
        # Василий задается вопросом, запомнит ли сайт ее список. Он видит
        # что для его списка сгенерирован уникальный URL -- по этому поводу
        # на странице есть какой то поясняющий текст.
        # Василий проверяет этот URL - его список дел на месте.
        # Довольный, он идет спать

if __name__ == '__main__':
    unittest.main(warnings='ignore')
