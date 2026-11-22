from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """The 'Log in' modal opened from the dashboard navbar."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.modal = page.get_by_role("dialog", name="Log in")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.log_in_button = page.get_by_role("button", name="Log in")

    def fill_credentials(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)

    def log_in(self, username: str, password: str) -> None:
        """Log in with valid credentials (no alert is shown on success)."""
        self.fill_credentials(username, password)
        self.log_in_button.click()

    def log_in_expecting_alert(self, username: str, password: str) -> str:
        """Log in with bad credentials and return the alert message."""
        self.fill_credentials(username, password)
        return self.click_and_get_alert(self.log_in_button)
