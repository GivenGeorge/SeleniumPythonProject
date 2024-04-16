from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import PageElement
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains


class CommonPageObject(PageObject):
    def open(self, page_name: str):
        # Open URL in browser

        # page_name: the name of the page to open
        page_name = page_name.strip().lower()
        switcher = {
            # URLs are defined in the properties.cfg
            page_name: self.config.get(page_name, 'url')
        }
        url = switcher.get(page_name, None)

        self.driver.get('{}'.format(url))
        return self

    def click_element(self, element_name: str, el: PageElement):
        self.logger.info("Attempting to click on the {}".format(element_name))
        self.utils.wait_until_element_visible(el)
        self.click_page_element(el)
        return self

    def click_page_element(self, el: PageElement):
        try:
            # Attempt to click the element
            self.utils.wait_until_element_clickable(el).click()
        except ElementClickInterceptedException:
            try:
                # If the click fails due to an intercept exception, use ActionChains to move the mouse to the element and click it
                actions = ActionChains(self.driver_wrapper.driver)
                actions.move_to_element(el.web_element).click().perform()
            except ElementClickInterceptedException:
                # If the click fails due to an intercept exception, use JavaScript to click the element
                self.utils.driver_wrapper.driver.execute_script("arguments[0].scrollIntoView();", el.web_element)
                self.utils.driver_wrapper.driver.execute_script("arguments[0].click();", el.web_element)
        return self

    def element_is_displayed(self, element_name: str, el: PageElement):
        self.logger.info(
            "Checking if element {} is displayed".format(element_name))
        ret = self.utils.get_web_element(el).is_displayed()
        self.logger.info(
            "Element {} is displayed is {}".format(element_name, str(ret)))
        return self
