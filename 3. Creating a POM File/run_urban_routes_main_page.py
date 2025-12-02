from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb441c762.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_locator(self, driver):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys('from_text')

    def enter_to_locator(self, driver):
        self.driver.find_element(*self.TO_LOCATOR).send_keys('to_text')

    def test_custom_bike_option(self, driver):
        driver = webdriver.Chrome()

    # Update server URL
        driver.get('https://cnt-4d00fe1b-6b10-42b0-ad42-a6ec6cd95f61.containerhub.tripleten-services.com')
        urban_routes_page = UrbanRoutesPage(driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_bike_icon()
        time.sleep(2)
        actual_value = urban_routes_page.get_bike_text()
        expected_value = "Bike"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        driver.quit()
