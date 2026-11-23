from playwright.sync_api import Locator, Page


class BasePage:
    """Common behaviour shared by every page object."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = "/") -> None:
        """Open a path relative to the base_url set in pytest.ini."""
        self.page.goto(path)

    def click_and_get_alert(self, locator: Locator) -> str:
        """Click an element that triggers a browser alert; accept it and return its text."""
        with self.page.expect_event("dialog") as dialog_info:
            locator.click()
        dialog = dialog_info.value
        message = dialog.message
        dialog.accept()
        return message

    @property
    def title(self) -> str:
        return self.page.title()

    @property
    def url(self) -> str:
        return self.page.url
