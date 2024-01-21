from pages.main_page import MainPage
from pages.base_page import BasePage


class TestGitHub:
    def test_create_new_rep(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site('https://github.com/')
        main_page.auth_on_the_github()
        main_page.create_new_rep()
        message = main_page.delete_new_rep()
        assert 'Your repository "luufqa/Selenium_test" was successfully deleted.' in message
