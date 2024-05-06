from selenium import webdriver
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser


class AdvancePageObject(PageObject):
    @property
    def driver(self):
        return self._driver

    @property
    def config(self):
        return self._config

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self._config = None
        self._driver = None
        self.title_header = None
        self.last_movie_title = None
        self.empire_strikes_back_link = None
        self.species_list = None
        self.phantom_menace_link = None
        self.planets_list = None
        self.back_button = None
        self.config = ConfigParser()
        self.config.read('config/properties.cfg')
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.get(self.config.get('Test', 'url'))

    def sort_by_title(self):
        self.title_header = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//th[normalize-space()='Title']")))
        self.title_header.click()
        self.last_movie_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.driver.find_element(By.XPATH, "//tbody/tr[last()]/td[1]"))).text
        assert self.last_movie_title == "The Phantom Menace"
        return self

    def view_movie_details(self):
        self.empire_strikes_back_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='The Empire Strikes Back']")))
        self.empire_strikes_back_link.click()
        self.species_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.driver.find_element(By.XPATH,
                                                      "//li[normalize-space()='Wookie']"))).text
        assert "Wookie" in self.species_list

    def click_back_button(self):
        self.back_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Back']")))
        self.back_button.click()
        return self

    @config.setter
    def config(self, value):
        self._config = value

    @driver.setter
    def driver(self, value):
        self._driver = value

    def planet_not_in_movie(self):
        self.phantom_menace_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "The Empire Strikes Back")))
        self.phantom_menace_link.click()
        self.planets_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.driver.find_element(By.XPATH,
                                                      "//h1[normalize-space()='The Phantom Menace']"))).text
        assert "Camino" not in self.planets_list
        return self
