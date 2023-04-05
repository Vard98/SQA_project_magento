import selenium.common.exceptions as Ex


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def refresh_page(self):
        self.driver.refresh()

    def navigate_to_url(self, url: str):
        self.driver.get(url)

    def get_current_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def navigate_back(self):
        self.driver.back()

    def navigate_forward(self):
        self.driver.forward()

    def find_element_by(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
        except Ex.NoSuchElementException:
            print('Element not found')
        return element

    def find_list_of_elements(self, locator):
        elements = None
        try:
            elements = self.driver.find_elements(*locator)
        except Ex.NoSuchElementException:
            print('Element not found')
        return elements

    def click(self, element):
        if element:
            try:
                element.click()
                return True
            except (Ex.NoSuchElementException, Ex.ElementNotInteractableException,
                    Ex.ElementClickInterceptedException) as error:
                print(error)
                return False
        print("Element reference is None")
        return False

