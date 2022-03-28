from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://google.com")
    driver.quit

def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/?hl=en")
    assert driver.title == "Instagram"
    driver.quit

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/login/device-based/regular/login")
    assert driver.title == "Log in to Facebook"
    driver.quit
    
