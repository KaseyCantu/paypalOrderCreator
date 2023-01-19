from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

user_email = input("Sandbox PayPal Account: ")
user_password = input("Sandbox PayPal Password: ")
recipient = input("Recipient Account: e.g. test.account+paypal99@auctane.com ")
number_of_orders_to_create = input("How many orders do you want to create? ")

browser = webdriver.Chrome()
browser.implicitly_wait(6)


def auto_browser() -> None:
    idx = 0
    number_of_orders = int(number_of_orders_to_create)

    try:
        paypal_login()
        navigate_to_send_money()
        sleep(1)

        while idx < number_of_orders:
            send_money_to_create_orders()
            idx += 1
            if idx == number_of_orders:
                break

    finally:
        print(f'{number_of_orders_to_create} orders were created!')
        browser.quit()


def paypal_login() -> None:
    # Open Sandbox PayPal homepage in Google Chrome
    browser.get("https://www.sandbox.paypal.com/us/home")

    # Homepage | Click login button
    init_login()

    # Login Page | Fill out user login form
    enter_user_email()
    enter_user_password()


def init_login() -> None:
    homepage_login = browser.find_element(By.ID, 'ul-btn')  # Homepage | Login Button
    homepage_login.click()


def enter_user_email() -> None:
    login_page_email_input = browser.find_element(By.ID, 'email')  # Login Page | Login Button
    login_page_email_input.clear()
    login_page_email_input.send_keys(user_email)


def enter_user_password() -> None:
    browser.find_element(By.ID, 'btnNext').click()  # Login Page | Password Input
    login_page_password_input = browser.find_element(By.ID, 'password')  # Login Page | Password Input
    login_page_password_input.clear()
    login_page_password_input.send_keys(user_password)
    browser.find_element(By.ID, 'btnLogin').click()


def navigate_to_send_money() -> None:
    browser.find_element(By.XPATH, '//div[contains(text(), "Send money")]').click()  # Dashboard | Send money button


def send_money() -> None:
    send_money_input = browser.find_element(By.XPATH, '//*[@id="fn-sendRecipient"]')  # Send Money Recipient | Input
    send_money_input.clear()
    send_money_input.send_keys(recipient)
    browser.find_element(By.XPATH, f'//div[contains(text(), "{recipient}")]').click()  # Send Money | Next button


def enter_funding_amount() -> None:
    funding_input = browser.find_element(By.XPATH, '//*[@id="fn-amount"]')  # Funding Page | Amount input
    funding_input.send_keys(str(randint(100, 999)))

    browser.find_element(By.XPATH, '//button[contains(text(), "Continue")]').click()  # Funding Page | Continue button


def send_payment_now() -> None:
    browser.find_element(By.XPATH, '//button[contains(text(), "Send Payment Now")]').click()


def send_more_money() -> None:
    browser.find_element(By.XPATH, '//a[contains(text(), "Send More Money")]').click()


def send_money_to_create_orders() -> None:
    send_money()
    enter_funding_amount()
    send_payment_now()
    send_more_money()


if __name__ == '__main__':
    auto_browser()
