import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_drive_custom_camping_option():
    driver = webdriver.Chrome()
    # Open the app - update the URL after starting the server
    driver.get('https://cnt-3caebb84-fe27-4fdd-b9d5-ab26217bd33c.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 1: Enter the "From" address
    urban_routes_page.enter_custom_camping_option().send_keys('East 2nd Street, 601')

    # Step 2: Enter the "To" address
    urban_routes_page.enter_custom_camping_option().send_keys('1300 1st St.')

    # Step 3: Choose "Custom"
    urban_routes_page.click_custom_camping_option().click()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 4: Click "Drive"
    urban_routes_page.click_custom_camping_option().click()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 5: Click "Book"
    urban_routes_page.click_booking_option().click()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 6: Choose "Camping"
    urban_routes_page.click_camping_option().click()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 7: Check if the text displays "Audi A3 Sedan"
    actual_value = urban_routes_page.get_audi_text()
    expected_value = "Audi A3 Sedan"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    time.sleep(2)
    driver.quit()
