#!/usr/bin/python3
#coding=utf-8

from .base_page import BasePage # импорт базового класса BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): # создаём класс MainPage, наследник класса BasePage. BasePage тж называют 'класс-предок'

	#Переносим метод из предыдущего урока (файл в родительском каталоге test_main_page.py) в класс MainPage, с изменениями
	def go_to_login_page(self): # В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
		login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link") # Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self . Заодно заменим find на более универсальный (By)
		login_link.click()
