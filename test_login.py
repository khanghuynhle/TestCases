import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginGUITest ()

    def setUp(self)

    def testLoginGUI
        user = "test"
         pwd = "test"
        firefox = webdriver.Firefox()
        firefox.get("http://demo.cairis.org/")
        elem = firefox.find_element_by_id("email")
        elem.send_keys(user)
        elem = firefox.find_element_by_id("password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        firefox.close()

        chrome = webdriver.Chrome()
        chrome.get("http://demo.cairis.org/")
        elem = chrome.find_element_by_id("email")
        elem.send_keys(user)
        elem = chrome.find_element_by_id("password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

    def tearDown(self)
        pass

if __name__ == '__main__':
    unittest.main()
