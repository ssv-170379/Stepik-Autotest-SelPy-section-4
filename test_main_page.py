from os import system

from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open() # открываем страницу
	page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина

def main():
	system(f'pytest -v --tb=line --language=en "{__file__}"')
if __name__ == "__main__":
	main()
