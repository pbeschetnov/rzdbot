import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class Checker:
    @staticmethod
    def check_type(seat_type):
        seat_type = seat_type.lower()
        return seat_type == 'плацкартный' or seat_type == 'сидячий'

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.set_script_timeout(10)
        self.driver.set_page_load_timeout(10)

    def check(self, train, date):
        try:
            url = train.url.format(date=date)
            self.driver.get(url)
        except TimeoutException:
            pass
        # sleeping because of selenium's weird behavior
        time.sleep(5)
        elements = self.driver.find_elements_by_class_name('route-carType-item')
        for element in elements:
            seat_type = element.find_element_by_class_name('col-xs-10').text
            if Checker.check_type(seat_type):
                found = True
                break
        else:
            found = False

        return found
