Feature: Star Wars Movies Page
  # Enter feature description here

  Scenario: UI Scenario’s:
    # Enter steps here
      Given the user open movies  page
        When the user click on title and very last movie title
        When the user click on link then user check if Wookie text is displayed
        Then the user click on back button
        When the user click on second link and check if element is not visible

