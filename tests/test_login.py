import pytest
from playwright.sync_api import expect

from utils.helpers import load_test_data

DATA = load_test_data("login_data.json")


def test_valid_login_shows_welcome(dashboard_page, login_page, credentials):
    dashboard_page.open()
    dashboard_page.open_log_in()
    login_page.log_in(credentials["username"], credentials["password"])

    expect(dashboard_page.welcome_user).to_have_text(f"Welcome {credentials['username']}")
    expect(dashboard_page.log_out_link).to_be_visible()


@pytest.mark.parametrize("case", DATA["invalid_logins"], ids=lambda c: c["id"])
def test_invalid_login_shows_alert(dashboard_page, login_page, credentials, case):
    username = credentials["username"] if case["username"] == "__ENV_USERNAME__" else case["username"]

    dashboard_page.open()
    dashboard_page.open_log_in()
    alert = login_page.log_in_expecting_alert(username, case["password"])

    assert alert == case["expected_alert"]
    expect(dashboard_page.welcome_user).to_be_hidden()


def test_signup_with_existing_user_shows_alert(dashboard_page, signup_page, credentials):
    dashboard_page.open()
    dashboard_page.open_sign_up()
    alert = signup_page.sign_up(credentials["username"], credentials["password"])

    assert alert == DATA["existing_user_signup_alert"]
