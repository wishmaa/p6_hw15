"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have, be
from selene.support.shared import config


'''Фикстура для открытия десктопного браузера с разрешением 1920х1280'''


@pytest.fixture
def open_browser_desktop():
    config.timeout = 5
    config.window_width = 1920
    config.window_height = 1280
    config.base_url = 'https://github.com/'
    yield
    browser.quit()


'''Фикстура для открытия мобильного браузера с разрешением iPhone XR'''


@pytest.fixture
def open_browser_mobile():
    config.timeout = 10
    config.window_width = 414
    config.window_height = 896
    config.base_url = 'https://github.com/'
    yield
    browser.quit()


def test_github_desktop(open_browser_desktop):
    browser.open('')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)


def test_github_mobile(open_browser_mobile):
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    assert browser.element('.js-sign-in-button').should(be.visible)
