from selenium.webdriver.common.by import By


class Locators:
    sign_in_button = (By.LINK_TEXT, 'Sign in')
    login_field = (By.ID, 'login_field')
    password_field = (By.ID, 'password')
    commit_button = (By.NAME, 'commit')

    new_rep_button = (By.XPATH, './/*[contains(@href, "/new") and contains(@class, "Button--primary") and contains(@class, "Button--small")]')
    enter_rep_name = (By.ID, ':r6:')
    private = (By.ID, ':ra:')
    add_readme = (By.ID, ':rc:')
    create_rep = (By.XPATH, ".//button[@class='types__StyledButton-sc-ws60qy-0 ccpeSR']")

    settings_rep = (By.ID, 'settings-tab')
    delete_rep = (By.ID, 'dialog-show-repo-delete-menu-dialog')
    delete_rep_next_steps = (By.ID, 'repo-delete-proceed-button')
    delete_verif_field = (By.ID, 'verification_field')
    delete_message = (By.XPATH, '//*[@id="js-flash-container"]/div/div/div')
