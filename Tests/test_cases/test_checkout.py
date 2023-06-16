from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from typing import Optional
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def start_chrome(
    headless: bool = True,
    webapp_testing: Optional[bool] = True
) -> WebDriver:
    import helium
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.utils import ChromeType
    dc = DesiredCapabilities.CHROME
    if webapp_testing:
        dc["goog:loggingPrefs"] = {'performance': 'ALL', 'browser': 'ALL'}
    # log.info(f"Using helium with headless = {headless}")
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    helium.set_driver(driver=driver)

    return helium.get_driver()

user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver = start_chrome(headless=False)
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()