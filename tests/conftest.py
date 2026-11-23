import pytest
from playwright.sync_api import Page

from config import config
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def signup_page(page: Page) -> SignupPage:
    return SignupPage(page)


@pytest.fixture(scope="session")
def credentials() -> dict:
    if not config.USERNAME or not config.PASSWORD:
        pytest.skip("Set DEMOBLAZE_USERNAME and DEMOBLAZE_PASSWORD in .env")
    return {"username": config.USERNAME, "password": config.PASSWORD}
