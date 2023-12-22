from .pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to('https://example.com/login')
    login_page.enter_credentials('user@example.com', 'password')
    login_page.submit_login_form()
    home_page = HomePage(driver)
    assert home_page.is_user_logged_in()


def test_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to('https://example.com/login')
    login_page.enter_credentials('invalid@example.com', 'invalid_password')
    login_page.submit_login_form()
