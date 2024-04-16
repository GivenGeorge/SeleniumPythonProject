from selenium.webdriver.common.by import By
from toolium.pageelements import Text
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import PageElement


class ProfessionalPageObject(PageObject):

    def init_page_elements(self):
        pass

    def get_element(self, element_name):

        switcher = \
            {
                "title_header": PageElement(By.XPATH, "//th[normalize-space()='Title']", wait=True),
                "last_movie_title": Text(By.XPATH, "//a[normalize-space()='The Phantom Menace']", wait=True),
                "empire_strikes_back_link": PageElement(By.XPATH,  "//a[normalize-space()='The Empire Strikes Back']", wait=True),
                "species_list": Text(By.XPATH, "//li[normalize-space()='Wookie']", wait=True),
                "phantom_menace_link": PageElement(By.XPATH, "//a[normalize-space()='The Phantom Menace']", wait=True),
                "planets_list":Text(By.XPATH, "//h1[normalize-space()='The Phantom Menace']"),
                "back_button": Text(By.XPATH, "//a[normalize-space()='Back']", wait=True)

            }

        el = switcher.get(element_name, None)

        if el is None:
            self.logger.error('Element "{}" is undefined'.format(element_name))
        else:
            return el
