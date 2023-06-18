## PREREQUISITES
## Installation
The installation process requires Python 3.9 or later.

To install the requirements, run
```
pip install -r /Challange-1/requirements.txt
```
## Chromedriver
The test uses the webdriver_manager toolkit which allows dynamic installation 
of up-to-date, system appropriate WebDrivers for every test run. The method 
start_chrome is located within the helper_methods.py file. 

## Testcases

The repository features two testcases which are combined into one test scenario.
The testcases test the users ability to add the cheapest available product on 
Amazon to the cart, and whether the sum total of the cart is calculated correctly 
can be expressed as follows:
```
Feature: Add cheapest available product to cart
    Given the name of the product
    When User enters name of the product into search
    And presses Enter
    And selects product name brand
    And sorts by lowest price
    And adds the first result to cart
    Then the cheapest available product should be in the cart
```
```
Feature: Check sum total of products in cart
    Given multiple products are in cart
    When user adds the product prices
    Then the sum total displayed matches the calculated total
```

## Running test scenario

### pytest based

The tests are aimed to be run via pytest. If needs be, can be executed from the Python Console 
or the terminal with the following command.

```
python -m pytest Tests/test_cases/test_checkout.py::test__user_flow
```

## For improvement
The testcases and repository setup are minimal at the moment and don't correspond to 
industry standarts. Here are some points that should be added to the testcase going forward.
Improvement of the repository structure (i.e separation of test cases, creating a separate object class 
for element locators, parametrization using fixtures, etc.), addition of logging compatibility for export of 
test results, as well as integration with reporting platforms for better display of the results.