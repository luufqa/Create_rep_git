from pages.main_page import MainPage
from pages.base_page import BasePage
from data.user_data import User


class TestGitHub:
    def test_create_new_rep(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        base_page.go_to_site('https://github.com/')
        main_page.auth_on_the_github()
        main_page.create_new_rep()
        message = main_page.delete_new_rep()
        assert f'Your repository "{User.verif_for_delete_rep}" was successfully deleted.' in message
