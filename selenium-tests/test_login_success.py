from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_valid_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!" + Keys.RETURN)

    # 🔑 Kritik fark: explicit wait
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    # 🔑 Daha stabil assertion
    assert "secure area" in message.text.lower()

    driver.quit()

if __name__ == "__main__":
    test_valid_login()
