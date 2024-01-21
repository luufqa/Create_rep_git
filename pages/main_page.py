from base_page import BasePage
from data.user_data import User
from locators.locators import Locators


class MainPage(BasePage):
    def auth_on_the_github(self):
        self.find_element_located_click(Locators.sign_in_button)
        self.find_element_located(Locators.login_field).send_keys(User.user_email)
        self.find_element_located(Locators.password_field).send_keys(User.user_password)
        self.find_element_located_click(Locators.commit_button)

    def create_new_rep(self):
        self.find_element_located_click(Locators.new_rep_button)
        self.find_element_located(Locators.enter_rep_name).send_keys(User.rep_name)
        self.find_element_located_click(Locators.private)
        self.find_element_located_click(Locators.add_readme)
        self.find_element_located_click(Locators.create_rep)
        self.find_element_located(Locators.settings_rep)

    def delete_new_rep(self):
        self.find_element_located_click(Locators.settings_rep)
        self.find_element_located_click(Locators.delete_rep)
        self.find_element_located_click(Locators.delete_rep_next_steps)
        self.find_element_located_click(Locators.delete_rep_next_steps)
        self.find_element_located(Locators.delete_verif_field).send_keys(User.verif_for_delete_rep)
        self.find_element_located_click(Locators.delete_rep_next_steps)
        return self.find_element_located(Locators.delete_message).text
