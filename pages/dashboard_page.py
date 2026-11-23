from playwright.sync_api import Page

from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Landing page served at the base_url (the product store home)."""

    PATH = "/"

    def __init__(self, page: Page):
        super().__init__(page)
        self.logo = page.locator("#nava")
        self.sign_up_link = page.get_by_role("link", name="Sign up")
        self.log_in_link = page.get_by_role("link", name="Log in")
        self.log_out_link = page.get_by_role("link", name="Log out")
        self.welcome_user = page.locator("#nameofuser")

    def open(self) -> None:
        self.navigate(self.PATH)

    def open_sign_up(self) -> None:
        self.sign_up_link.click()

    def open_log_in(self) -> None:
        self.log_in_link.click()
