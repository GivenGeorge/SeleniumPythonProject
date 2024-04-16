from behave import *
from asserts import *
from PageObjects.common import CommonPageObject
from Steps.mapping import get_element


@step('the "{page_name}" page is open')
def step_impl(context, page_name=""):
    try:
        context.current_page = CommonPageObject()
        context.current_page.open(page_name)
    except Exception as expt:
        print(f"Thrown exception on {page_name}: {expt}")
        raise


@step('on page "{page_name}" the user clicks the "{element_name}"')
def step_impl(context, page_name="", element_name=""):
    try:
        print(f'on page "{page_name}" the user clicks the "{element_name}"')
        el = get_element(page_name, element_name)
        CommonPageObject().click_element(element_name, el)
    except Exception as expt:
        print(f"Thrown exception on {page_name}.{element_name}: {expt}")
        raise


@step('on page "{page_name}" the text "{text}" is displayed')
def step_impl(context, page_name="", text=""):
    try:
        print(f'on page "{page_name}" the text "{text}" is displayed')
        assert_boolean_true(context.current_page.get_find_tables(text),
                            msg_fmt="text {} is not displayed on the page {}".format(text, page_name))
        print(f"\t page {page_name} element with text '{text}' is displayed, value is {text}")
    except Exception as expt:
        print(f"Thrown exception on {page_name}, text '{text}': {expt}")
        raise
