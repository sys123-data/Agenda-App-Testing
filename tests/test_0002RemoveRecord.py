import pytest, time
from tests.framework.fixture import toDoAppPage
from tests.framework.fixture import app

from pytest_bdd import (
    scenario,
    given,
    when,
    then
)


@scenario('features/0002RemoveRecord.feature','Remove record')
def test_remove_record():
    """Remove record"""

@given('I access the website')
def i_access_the_website(toDoAppPage):
    assert toDoAppPage.go_to_web_site(), 'Web site not loaded'

@when('I remove record')
def i_remove_value(toDoAppPage):
    assert toDoAppPage.click_remove(), 'Msj not removed'


@then('<value> should not be available')
def look_for_added_item(toDoAppPage,value,app):
    assert not toDoAppPage.look_for_added_item(value), 'Item not removed'
    app.take_screenshot('0002')
    toDoAppPage.end_session()
