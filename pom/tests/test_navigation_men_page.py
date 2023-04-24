import pytest
from pom.pages.home_page import HomePage


@pytest.mark.usefixtures("set_up")
class TestNavigationMenPage:


    def test_navigation_to_men_page(self):
        home_page = HomePage(self.driver)
        home_page.wait_for_page_load()
        home_page.navigate_men_page()
        assert home_page.get_current_page_title() == "Men"





