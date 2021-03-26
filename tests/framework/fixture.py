import pytest

from tests.pages.toDoAppPage import to_Do_App_Page

from tests.framework.appToDo import APP


@pytest.fixture
def app():
    app = APP()
    yield app

@pytest.fixture
def toDoAppPage(app):
    toDoAppPage = to_Do_App_Page(app)
    yield toDoAppPage