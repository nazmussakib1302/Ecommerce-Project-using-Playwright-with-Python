from playwright.sync_api import Page

from pages.base_page import BasePage


class SignupPage(BasePage):
    """The 'Sign up' modal opened from the dashboard navbar."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.modal = page.get_by_role("dialog", name="Sign up")
        self.username_input = page.locator("#sign-username")
        self.password_input = page.locator("#sign-password")
        self.sign_up_button = page.get_by_role("button", name="Sign up")
        self.close_button = self.modal.get_by_label("Close")

    def sign_up(self, username: str, password: str) -> str:
        """Submit the form and return the alert message the site shows."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        return self.click_and_get_alert(self.sign_up_button)

    def close(self) -> None:
        self.close_button.click()
