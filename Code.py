# Need create config.py with user_email / user_password
# Need add package selenium, pytest
# Code add new rep on the gitHub and after delete


from selenium import webdriver
from selenium.webdriver.common.by import By
import config_new
import time


def login_in_github(browser):
    browser.find_element(By.LINK_TEXT, 'Sign in').click()
    time.sleep(2)
    browser.find_element(By.ID, 'login_field').send_keys(config_new.user_email)
    browser.find_element(By.ID, 'password').send_keys(config_new.user_password)
    browser.find_element(By.NAME, 'commit').click()


def test_create_and_delete_repo():
    browser = webdriver.Chrome()
    browser.get('https://github.com/')

    login_in_github(browser)
    browser.get('https://github.com/luufqa')
    browser.find_element(By.ID, 'repositories-tab').click()
    time.sleep(2)
    browser.find_element(By.LINK_TEXT, 'New').click()
    time.sleep(3)
    browser.find_element(By.ID, ':r2:').send_keys('Selenium_test1')
    browser.find_element(By.ID, ':r6:').click()
    time.sleep(2)
    browser.find_element(By.ID, ':r8:').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button/span/span').click()
    time.sleep(4)
    # checking after creating repo
    repos = browser.find_element(By.LINK_TEXT, 'Selenium_test1')
    priv = browser.find_element(By.XPATH, '//*[@id="repository-container-header"]/div[1]/div[1]/div[1]/span[2]')
    readme = browser.find_element(By.LINK_TEXT, 'README.md')

    assert repos.text == 'Selenium_test1'
    assert priv.text == 'Private'
    assert readme.text == 'README.md'

    browser.find_element(By.ID, 'settings-tab').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="dialog-show-repo-delete-menu-dialog"]/span/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="verification_field"]').send_keys('luufqa/Selenium_test1')
    browser.find_element(By.XPATH, '//*[@id="verification_field"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="repo-delete-proceed-button"]/span/span').click()
    time.sleep(2)
    message_delete = browser.find_element(By.XPATH, '//*[@id="js-flash-container"]/div/div/div')

    assert message_delete.text == 'Your repository "luufqa/Selenium_test1" was successfully deleted.\n '

    browser.quit()
