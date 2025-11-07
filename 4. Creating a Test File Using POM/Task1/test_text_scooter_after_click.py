import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class

def test_custom_scooter_option():
    # Open the app - update the URL after starting the server
    driver = webdriver.Chrome()
    driver.get('https://cnt-fb54dfc4-00e8-44d6-afed-f197da701aeb.containerhub.tripleten-services.com')

    # Create an instance of the page class
    # urban_routes_page is the instance name that you created from UrbanRoutesPage
    urban_routes_page = UrbanRoutesPage(driver)

    # Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')