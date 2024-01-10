import pytest
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_has_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed()


if __name__ == "__main__":
    pytest.main()

# pytest --language=es test_items.py
# pytest --language=fr test_items.py
