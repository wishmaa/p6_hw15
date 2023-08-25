import pytest
from selene import browser, be, have
from selene.support.shared import config


def mobile_settings(width, height):
    return width < height


@pytest.fixture(params=[(1280, 960), (1920, 1280), (820, 1180), (414, 896)])
def browser_parameters(request):
    config.timeout = 5
    config.window_width = request.param[0]
    config.window_height = request.param[1]
    config.base_url = 'https://github.com/'
    yield
    browser.quit()


def test_github_desktop(browser_parameters):
    if mobile_settings(browser.config.window_width, browser.config.window_height):
        pytest.skip('Разрешение только для мобильных тестов')
    browser.open('')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)


def test_github_mobile(browser_parameters):
    if not mobile_settings(browser.config.window_width, browser.config.window_height):
        pytest.skip('Разрешение только для десктопных тестов')
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    assert browser.element('.js-sign-in-button').should(be.visible)
