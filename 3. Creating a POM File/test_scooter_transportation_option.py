from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_custom_scooter():
    driver = webdriver.Chrome()
    driver.get('https://cnt-4d00fe1b-6b10-42b0-ad42-a6ec6cd95f61.containerhub.tripleten-services.com')
    driver.find_element(By.ID, 'from').send_keys('East 2nd Street, 601')
    driver.find_element(By.ID, 'to').send_keys('1300 1st St')
    driver.find_element(By.XPATH, '//div[text()="Custom"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]').click()
    time.sleep(2)
    actual_value = driver.find_element(By.XPATH, '//div[@class="results-text"]//div[@class="text"]').text
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Expected {expected_value} but got {actual_value}"
    time.sleep(2)
    driver.quit()

