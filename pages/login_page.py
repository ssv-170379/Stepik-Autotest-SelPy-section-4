
from .base_page import BasePage # импорт базового класса BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		# реализуйте проверку на корректный url адрес
		assert 'login' in browser.current_url, "the Login page address is not found on the page"

	def should_be_login_form(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "the Login form is not found on the page"

	def should_be_register_form(self):
		assert self.is_element_present(*MainPageLocators.REGISTRSTION_FORM), "the Registration form is not found on the page"

