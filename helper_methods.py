from typing import Optional
from selenium.webdriver.chrome.webdriver import WebDriver

def start_chrome(
    headless: bool = False,
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