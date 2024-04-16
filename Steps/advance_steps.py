import time
from behave import given, when, then
from PageObjects.advance_page import AdvancePageObject


@given('the user open movies  page')
def step_impl(context):
    context.current_page = AdvancePageObject()
    context.current_page.open()
    time.sleep(5)


@when('the user click on title and very last movie title')
def step_impl(context):
    context.current_page.sort_by_title()
    time.sleep(2)


@when('the user click on link then user check if Wookie text is displayed')
def step_impl(context):
    context.current_page.view_movie_details()
    time.sleep(2)


@then('the user click on back button')
def step_impl(context):
    context.current_page.click_back_button()
    time.sleep(2)


@when('the user click on second link and check if element is not visible')
def step_impl(context):
    context.current_page.planet_not_in_movie()
    time.sleep(2)



