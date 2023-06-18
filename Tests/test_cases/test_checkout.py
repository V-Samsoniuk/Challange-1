import pytest
from selenium.webdriver.common.keys import Keys
from helper_methods import start_chrome
from selenium.webdriver.chrome.webdriver import WebDriver


search = '//*[@id="twotabsearchtextbox"]'
sort = '//*[contains(@id, "s-result-sort-select")]//option[.="Preis: Aufsteigend"]'
result = '//div[contains(@cel_widget_id, "MAIN-SEARCH_RESULTS-3")]//div[2][contains(@class, "s-product")]'
add_to_basket = '//*[@id="add-to-cart-button"]'
basket = '//*[@id="nav-cart"]'
checkout = '//*[@id="sc-buy-box-ptc-button"]'
price = '//span[contains(@class,"sc-product-price")]'
cart_total = '//*[@id="sc-subtotal-amount-activecart"]'


def element(locator):
    return WebDriver.find_element_by_xpath(locator)


def elements(locator):
    return WebDriver.find_elements_by_xpath(locator)

@pytest.fixture
def products():
    return ("Skittles", "M&M'S")


def test__add_product_to_cart(
        driver: WebDriver,
        product: str
):
    marke = f'//li[contains(@id, "p_89/{product}")] //div'
    element(search).send_keys(product)
    element(search).send_keys(Keys.RETURN)
    element(marke).click()
    element(sort).click()
    element(result).click()
    element(add_to_basket).click()
    assert '/cart' in driver.current_url
    return driver


def test__go_to_checkout(
    driver: WebDriver,
    products: list
):
    element(basket).click()
    total = ['']
    for i in len(products):
        total.append(elements(price)[i-1].text[:-1].replace(",","."))
    total = sum(float(total))
    assert total == element(cart_total).text[:-1]
    element(checkout).click()
    assert '/signin' in driver.current_url
    return driver


def test__user_flow(
        products: list):
    driver = start_chrome(headless=False)
    driver.get("https://www.amazon.de")
    cookies = driver.find_element_by_id("sp-cc-accept")
    cookies.click()
    for product in products:
        test__add_product_to_cart(driver=driver, product=product)
    test__go_to_checkout(driver=driver, products=products)
    return driver
