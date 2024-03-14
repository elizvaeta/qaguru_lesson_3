import pytest

from selene import browser, be, have


@pytest.fixture(autouse=True)
def set_browser_size():
    browser.open()
    browser.driver.set_window_size(1920, 1080)
    browser.open('https://google.com')
    yield
    browser.quit()


def test_google():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative():
    browser.element('[name="q"]').should(be.blank).type('someTextThatGoogleWillNeverFind').press_enter()
    browser.element('[id="botstuff"]').should(
        have.text('По запросу someTextThatGoogleWillNeverFind ничего не найдено.'))
