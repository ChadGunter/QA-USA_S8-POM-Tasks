from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        #Initialize the Chrome driver once for the class
        cls.driver = webdriver.Chrome()

    def test_custom_scooter_option(self):
        self.driver.get('https://cnt-dff1bf6b-fa6c-447a-9f02-378f402b91a2.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street 601', '1300 1st St')
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_scooter_icon()
        time.sleep(2)
        actual_value = urban_routes_page.get_scooter_text()
        expected_value = "Scooter"
        assert expected_value in actual_value, f"Expected: '{expected_value}', but got '{actual_value}'"

    def test_duration_custom_scooter_option(self)  :
        self.driver.get('https://cnt-dff1bf6b-fa6c-447a-9f02-378f402b91a2.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations('East 2nd Street 601', '1300 1st St')
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_scooter_icon()
        time.sleep(2)
        actual_value = urban_routes_page.get_duration_text()
        expected_value = "Duration"
        assert expected_value in actual_value, f"Expected: '{expected_value}', but got '{actual_value}'"

        @classmethod
        def teardown_class(cls):
            #Close the browser after all tests are done
            cls.driver.quit()