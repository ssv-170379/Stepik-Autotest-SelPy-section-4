from os import system

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
	login_link = browser.find_element_by_css_selector("#login_link")
	login_link.click()

def test_guest_can_go_to_login_page(browser): 
	browser.get(link)
	go_to_login_page(browser)

def main():
	system(f'pytest -v --tb=line --language=en "{__file__}"')
if __name__ == "__main__":
	main()
