
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
		assert 'login' in self.browser.current_url, "the 'Login page' URL does not include the 'login' substring"

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "the 'Login form' is not found on the 'Login page'"

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTRSTION_FORM), "the 'Registration form' is not found on the 'Login page'"

