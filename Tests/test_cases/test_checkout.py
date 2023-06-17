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
price = '//span[contains(@class,"sc-product-price")]'
total = '//*[@id="sc-subtotal-amount-activecart"]'

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
test__add_product_to_cart(driver, ("Skittles", "M&M'S"))
element(basket).click()
p1 = elements(price)[1].text[:-1]
p2 = elements(price)[0].text[:-1]
t = elements(total)[0].text[:-1]

p1 = p1.replace(",",".")
p2 = p2.replace(",",".")
t = t.replace(",",".")
sum = float(p1) + float(p2)
assert float (t )== sum
element(checkout).click()
assert '/signin' in driver.current_url
