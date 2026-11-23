import pytest
from playwright.sync_api import expect

from pages.account_page import AccountPage


def test_login_success(home_page):
    login_page = home_page.go_to_login_page()
    login_page.fill_in_login_form("customer2@practicesoftwaretesting.com", "welcome01")
    login_page.click_login_button()
    account_page = AccountPage(login_page.page)

    expect(account_page.title_my_account).to_be_visible()


@pytest.mark.parametrize("email, password", [
    ("customer2@practicesoftwaretesting.com", "wrong1"),
    ("wrong@practicesoftwaretesting.com", "welcome01")], ids=["wrong_password", "wrong_email"])
def test_login_wrong_data(home_page, email, password):
    login_page = home_page.go_to_login_page()
    login_page.fill_in_login_form(email, password)
    login_page.click_login_button()

    expect(login_page.invalid_email_or_password_error).to_be_visible()