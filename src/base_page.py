import os
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.common.exceptions import TimeoutException


def get_locator_by_string(locator_with_type):
    exploided_locator = locator_with_type.split(':', 1)
    by_type = exploided_locator[0]
    locator = exploided_locator[1]

    if by_type == 'xpath':
        return (By.XPATH, locator)
    elif by_type == 'css':
        return (By.CSS_SELECTOR, locator)
    elif by_type == 'id':
        return (By.ID, locator)
    elif by_type == 'class_name':
        return (By.CLASS_NAME, locator)
    elif by_type == 'name':
        return (By.NAME, locator)
    elif by_type == 'partial_link_text':
        return (By.PARTIAL_LINK_TEXT, locator)
    elif by_type == 'link_text':
        return (By.LINK_TEXT, locator)
    elif by_type == 'tag_name':
        return (By.TAG_NAME, locator)
    else:
        raise Exception(f'Cannot get type of locator. Locator {locator_with_type}')


class BasePage:

    def __init__(self, driver: webdriver) -> None:
        self._driver = driver

    def get_element(self, locator: str, timeout=10):
        by = get_locator_by_string(locator)
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(by), ' : '.join(by))

    def get_no_element(self, locator: str, timeout=10):
        by = get_locator_by_string(locator)
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.invisibility_of_element_located(by), ' : '.join(by))

    def get_elements(self, locator: str, timeout=10):
        by = get_locator_by_string(locator)
        return WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_any_elements_located(by), ' : '.join(by))

    def get_element_text(self, locator: str, timeout=10):
        by = get_locator_by_string(locator)
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(by), ' : '.join(by))
        return element.text

    def get_element_and_click(self, locator: str, timeout=15):
        by = get_locator_by_string(locator)
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(by), ' : '.join(by))
        return element.click()

    def get_element_and_send_keys(self, locator: str, data, timeout=15):
        by = get_locator_by_string(locator)
        element = WebDriverWait(self._driver, timeout).until(
            ex_cond.visibility_of_element_located(by), ' : '.join(by))
        return element.send_keys(data)

    def scroll_to_element(self, locator: str, timeout=2):
        by = get_locator_by_string(locator)

        def elem_none():
            try:
                WebDriverWait(self._driver, timeout).until(
                    ex_cond.invisibility_of_element_located(by), ' : '.join(by))
                return True

            except TimeoutException:
                return False

        for _ in range(10):
            if elem_none() is True:

                size = self._driver.get_window_size()
                startx, starty = int(size['width']) * 0.5, int(size['height']) * 0.8
                endx, endy = int(size['width']) * 0.5, int(size['height']) * 0.2
                self._driver.swipe(startx, starty, endx, endy, 1000)

                if elem_none() is False:
                    break
                else:
                    continue

    def hide_keyboard(self):
        size = self._driver.get_window_size()
        x, y = int(size['width']) * 0.99, int(size['height']) * 0.5
        self._driver.tap([(x, y)], 1000)

    def tap_to_show(self, locator: str, timeout=2):
        by = get_locator_by_string(locator)

        def elem_none():
            try:
                WebDriverWait(self._driver, timeout).until(
                    ex_cond.invisibility_of_element_located(by), ' : '.join(by))
                return True

            except TimeoutException:
                return False

        while elem_none() is True:

            size = self._driver.get_window_size()
            x, y = int(size['width']) * 0.5, int(size['height']) * 0.1
            self._driver.tap([(x, y)], 1000)

            if elem_none() is False:
                break
            else:
                continue

    def compare_image_with_screenshot(self, image_path: str):
        os.chdir('../src/screenshots/')

        with open(f'{image_path}.png', 'rb') as img:
            first_image = base64.b64encode(img.read()).decode('ascii')
        second_image = base64.b64encode(self._driver.get_screenshot_as_png()).decode('ascii')

        return self._driver.get_images_similarity(first_image, second_image)

    def find_element_bool(self, locator: str, timeout=2):
        by = get_locator_by_string(locator)

        try:
            WebDriverWait(self._driver, timeout).until(
                ex_cond.invisibility_of_element_located(by), ' : '.join(by))
            return True

        except TimeoutException:
            return False

    def long_tap_in_the_middle_page(self):

        size = self._driver.get_window_size()
        x, y = int(size['width']) * 0.5, int(size['height']) * 0.5

        self._driver.tap([(x, y)], 2000)
