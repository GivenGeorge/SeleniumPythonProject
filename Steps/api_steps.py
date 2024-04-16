import unittest
from selenium import webdriver
import requests


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")

    def test_api_scenario_1(self):
        response = requests.get("https://swapi.dev/api/films/")
        movies = response.json()['results']
        self.assertEqual(len(movies), 6)

    def test_api_scenario_2(self):
        response = requests.get("https://swapi.dev/api/films/3/")
        movie = response.json()
        self.assertEqual(movie['director'], 'Richard Marquand')

    def test_api_scenario_3(self):
        response = requests.get("https://swapi.dev/api/films/5/")
        movie = response.json()
        self.assertNotIn('Gary Kurtz, George Lucas', movie['producers'])

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
