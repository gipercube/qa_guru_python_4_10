import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def window_size():
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
