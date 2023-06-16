import helium
import logging
import selenium
from typing import Optional
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from constants import create_log_file_handler, SCREENSHOTS_PATH
from Extensions.Enums import Enums
from WebApp.WebAppScreen import WebAppScreen

log = logging.getLogger(__name__)
log.addHandler(create_log_file_handler(__name__))


class ProfileScreen(WebAppScreen):
    url_path = "/profile"
    name = "Profile Screen"

    class ElementLocator(Enums):
        back_button = \
            '//button[contains(@class,"case")][contains(@type,"button")]'
        language_button = \
            '//div[contains(@class,"rightBtn")]'
        change_password_button = \
            '//a[contains(@href,"/change-password")]'
        change_address_button = \
            '//a[contains(@href,"/address")]'
        change_tax_button = \
            '//a[contains(@href,"/tax")]'
        edit_payment_method_button = \
            '//button[.="Edit"]'
        delete_payment_method_button = \
            '//button[.="Delete"]'
        add_payment_method_button = \
            '//button[.="Add payment method"]'
        manage_tab = \
            '//a[contains(@href, "/profile/manage")]'
        payments_tab = \
            '//a[contains(@href, "/profile/payments")]'


    def __init__(
        self,
        driver: WebDriver,
        test_id: Optional[str] = None,
        open_page: bool = False,
        url_base: Optional[str] = None,
    ):
        super().__init__(
            driver=driver,
            test_id=test_id,
            open_page=open_page,
            url_base=url_base

        )
        self.timeout = 60
        self.driver.save_screenshot(f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.__init__.__name__}.png')
        self.wait = WebDriverWait(self.driver, timeout=self.timeout)

    @property
    def add_payment_method_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.add_payment_method_button)

    @property
    def edit_payment_method_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.edit_payment_method_button)

    @property
    def delete_payment_method_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.delete_payment_method_button)

    @property
    def change_password_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.change_password_button)

    @property
    def change_address_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.change_address_button)

    @property
    def change_tax_data_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.change_tax_button)

    @property
    def manage_tab_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.manage_tab)

    @property
    def payments_tab_button(self) -> helium.S:
        return self.helium_selector(self.ElementLocator.payments_tab)

    def provide_vat_number(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.change_tax_button.name}'")
        helium.click(self.change_tax_data_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.provide_vat_number.__name__}.png')
        return self

    def add_payment_method(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.add_payment_method_button.name}'")
        helium.click(self.add_payment_method_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.add_payment_method.__name__}.png')
        return self


    def edit_payment_method(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.edit_payment_method_button.name}'")
        helium.click(self.edit_payment_method_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.edit_payment_method.__name__}.png')
        return self


    def delete_payment_method(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.delete_payment_method_button.name}'")
        helium.click(self.delete_payment_method_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.delete_payment_method.__name__}.png')
        return self

    @allure.step("ACTION: Change password")
    def change_password(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.change_password_button.name}'")
        helium.click(self.change_password_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.change_password.__name__}.png')
        return self

    @allure.step("ACTION: Switch to manage tab")
    def switch_to_manage_tab(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.manage_tab.name}'")
        helium.click(self.manage_tab_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.switch_to_manage_tab.__name__}.png')
        return self

    @allure.step("ACTION: Switch to payments tab")
    def switch_to_payments_tab(self):
        log.info(f"{self._prefix}Clicking on '{self.ElementLocator.payments_tab.name}'")
        helium.click(self.payments_tab_button)
        self.driver.save_screenshot(
            f'{SCREENSHOTS_PATH}{self.test_id}-{self.name}--{self.switch_to_payments_tab.__name__}.png')
        return self

    def get_added_payment_method_mbway(self, expected_payment_method):
        log.info(f'Verifying added Payment method details of {expected_payment_method}')
        self.wait.until(
            ec.presence_of_element_located((By.XPATH,
                                            "//*[contains(@class,'card withButtons')]//*[contains(text(),'MB')]"))
        )

        mbway_value = self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//*[contains(@class,'card withButtons')]//span"))
        )
        mbway_value_actual = mbway_value.text
        return mbway_value_actual

    def pms_check(self):
        self.switch_to_payments_tab()
        log.info(f"Checnig for active Payment Method")
        try:
            self.wait_for_element_visible(element_name=self.ElementLocator.edit_payment_method_button.name,
                                          locator_tuple=(By.XPATH, self.ElementLocator.edit_payment_method_button.value),
                                          timeout=2)
            msg = f'ACCOUNT ALREADY HAS ACTIVE PAYMENT METHOD'
            log.error(msg)
            raise ValueError(msg)
        except selenium.common.exceptions.TimeoutException:
            return self

    def pms_check_flow(self):
        try:
            self.pms_check().add_payment_method()
        except ValueError as e:
            print(e.args)
            if 'ACTIVE' in e.args[0]:
                self.edit_payment_method()
            else:
                raise ValueError
