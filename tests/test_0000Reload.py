import pytest, time
from tests.framework.fixture import toDoAppPage
from tests.framework.fixture import app

from pytest_bdd import (
    scenario,
    given,
    when,
    then
)


@scenario('features/0000Reload.feature','Reload Web App')
def test_reload_app():
    """Reload app"""

@given('I access the website')
def i_access_the_website(toDoAppPage):
    assert toDoAppPage.go_to_web_site(), 'Web site not loaded'

@when('I reload the webpage')
def i_reload_the_webpage(toDoAppPage):
    toDoAppPage.reload_page()

@then('App title should be available')
def app_title_should_be_available(toDoAppPage,app):
    assert toDoAppPage.look_for_page_title(), 'Title is not Todo app'
    app.take_screenshot('0000')
    toDoAppPage.end_session()