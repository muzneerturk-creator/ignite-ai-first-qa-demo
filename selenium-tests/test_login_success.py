from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    password.send_keys(Keys.RETURN)

    time.sleep(2)

    message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in message.text

    driver.quit()
