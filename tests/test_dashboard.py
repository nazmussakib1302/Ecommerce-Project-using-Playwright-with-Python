from playwright.sync_api import expect

from pages.dashboard_page import DashboardPage


def test_navigate_to_base_url(dashboard_page: DashboardPage, base_url: str):
    dashboard_page.open()

    expect(dashboard_page.page).to_have_url(base_url)
    expect(dashboard_page.logo).to_be_visible()
