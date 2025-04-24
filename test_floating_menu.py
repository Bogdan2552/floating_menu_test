from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_floating_menu_visibility():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/floating_menu")
    driver.maximize_window()

    # Locate the floating menu
    menu = driver.find_element(By.ID, "menu")

    # Get initial Y position of the menu
    initial_y = menu.location['y']

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Check if menu is still displayed and didn't move
    assert menu.is_displayed(), "Floating menu is not visible after scrolling"
    new_y = menu.location['y']
    assert new_y == initial_y, "Floating menu moved after scrolling"

    driver.quit()
