#!/usr/bin/python3
#coding=utf-8

from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
	REGISTRSTION_FORM = (By.CSS_SELECTOR, "form#register_form")
