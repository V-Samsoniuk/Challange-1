from selenium.webdriver.common.keys import Keys
from helper_methods import start_chrome

###Setup
product = "Skittles"
driver = start_chrome(headless=False)
driver.get("https://www.amazon.de")
cookies = driver.find_element_by_id("sp-cc-accept")
cookies.click()

search = '//*[@id="twotabsearchtextbox"]'
marke_select = f'//li[contains(@id, "p_89/{product}")] //div'
sort = '//*[contains(@id, "s-result-sort-select")]//option[.="Preis: Aufsteigend"]'
result = '//div[contains(@cel_widget_id, "MAIN-SEARCH_RESULTS-3")]//div[2][contains(@class, "s-product")]'
price = '//*[contains(@class,"priceToPay")]//span[contains(@class, "a-offscreen")]'
add_to_basket = '//*[@id="add-to-cart-button"]'
basket = '//*[@id="nav-cart"]'
checkout = '//*[@id="sc-buy-box-ptc-button"]'
price = '//*[contains(@id,"sc-active")]/div[4]/div/div[2]/ul/div/p[1]/span'

def element(locator):
    return driver.find_element_by_xpath(locator)

def elements(locator):
    return driver.find_elements_by_xpath(locator)

def test__add_product_to_cart(
        driver: driver,
        products: product
):
    for product in products:
        marke = f'//li[contains(@id, "p_89/{product}")] //div'
        element(search).send_keys(product)
        element(search).send_keys(Keys.RETURN)
        element(marke).click()
        element(sort).click()
        element(result).click()
        element(add_to_basket).click()
        assert '/cart' in driver.current_url
    return driver
###Go to basket

basket.click()
checkout.click()

