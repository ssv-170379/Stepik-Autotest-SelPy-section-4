from os import system

def test_guest_can_go_to_login_page(browser):
	link = "http://selenium1py.pythonanywhere.com/"
	browser.get(link)
	login_link = browser.find_element_by_css_selector("#login_link")
	login_link.click()

def main():
	system(f'pytest -v --tb=line --language=en "{__file__}"')
if __name__ == "__main__":
	main()
