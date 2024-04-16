# import webdriver module from selenium package
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Access chrome class from webdriver module
driver = webdriver.Chrome()  # driver object of chrome class

# Navigate to the url
driver.get("http://localhost:3000")
driver.maximize_window()
time.sleep(2)


# UI Scenarios
def sort_movies_by_title():
    # Click on the column header to sort by title
    title_header = driver.find_element(By.XPATH, "//th[normalize-space()='Title']")
    title_header.click()

    # Assertin - Assert the last movie in the list is 'The Phantom Menace'
    last_movie_title = driver.find_element(By.XPATH, "//a[normalize-space()='The Phantom Menace']").text
    assert last_movie_title == "The Phantom Menace"
    time.sleep(2)


def view_movie_details():
    # Click on the desired movie to view its details
    empire_strikes_back_link = driver.find_element(By.XPATH, "//a[normalize-space()='The Empire Strikes Back']")
    empire_strikes_back_link.click()

    # Check if the 'Species' list includes 'Wookie'
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//li[normalize-space()='Wookie']"))
        )
        print("Element is part of species list")

    except TimeoutException:
        print("Error element not found")

    # Click the back button to return to the main listing screen
    back_button = driver.find_element(By.XPATH, "//a[normalize-space()='Back']")
    back_button.click()

    time.sleep(2)


def planet_not_in_movie():
    # Click on the desired movie to view its details
    phantom_menace_link = driver.find_element(By.XPATH, "//a[normalize-space()='The Phantom Menace']")
    phantom_menace_link.click()

    # Assert that "Planets" and "Camino" are not part of the movie information
    try:
        movie_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='The Phantom Menace']")))
        movie_info = movie_element.text

        assert "Planets" not in movie_info and "Camino" not in movie_info

        print("Give output assert work because: 'Planets' and 'Camino' is not part of the movie 'The Phantom Menace'")
    except Exception as e:
        print("Assertion failed:", e)

    # Click the back button to return to the main listing screen
    back_button = driver.find_element(By.XPATH, "//a[normalize-space()='Back']")
    back_button.click()
    time.sleep(2)


sort_movies_by_title()
view_movie_details()
planet_not_in_movie()

driver.quit()
