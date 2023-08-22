"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be, have
from selene.support.shared import config


desktop = pytest.mark.parametrize('browser_parameters', [(1280, 960), (1920, 1280)], indirect=True)
mobile = pytest.mark.parametrize('browser_parameters', [(820, 1180), (414, 896)], indirect=True)


@pytest.fixture()
def browser_parameters(request):
    config.timeout = 5
    config.window_width = request.param[0]
    config.window_height = request.param[1]
    config.base_url = 'https://github.com/'
    browser.quit()


@desktop
def test_github_desktop(browser_parameters):
    browser.open('')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)


@mobile
def test_github_mobile(browser_parameters):
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    assert browser.element('.js-sign-in-button').should(be.visible)
