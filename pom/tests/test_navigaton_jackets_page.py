import pytest
from selenium.common import TimeoutException

from pom.pages.men_page import MenPage
from pom.pages.home_page import HomePage

@pytest.mark.usefixtures("set_up")
class TestJacketsPage:

    def test_navigation_jackets_page(self):
        home_page = HomePage(self.driver)
        men_page = MenPage(self.driver)
        home_page.navigate_men_page()
        men_page.navigate_jackets_page()
        assert men_page.get_current_page_title() == "Jackets - Tops - Men"


