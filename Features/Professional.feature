Feature: Sort movies by ’Title’ and assert the last movie in the list is ‘The Phantom Menace’
  View the movie ‘The Empire Strikes Back’ and check if the ‘Species’ list has ‘Wookie’
  Assert that ‘Planets’ ‘Camino’ is not part of the movie ‘The Phantom Menace’

  Scenario: UI Scenarios
    Given the "professional_page" page is open
    When on page "professional_page" the user clicks the "title_element"
    And on page "professional_page" the text "last_movie" is displayed
    And on page "professional_page" the user clicks the "first_link"
    When on page "professional_page" the text "wookie_element" is displayed
    And on page "professional_page" the user clicks the "back_button"
    And on page "professional_page" the user clicks the "second_link"
    When on page "professional_page" the text "what_element" is displayed
    And on page "professional_page" the user clicks the "back_button"

