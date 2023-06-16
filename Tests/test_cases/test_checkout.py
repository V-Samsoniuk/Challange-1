from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()