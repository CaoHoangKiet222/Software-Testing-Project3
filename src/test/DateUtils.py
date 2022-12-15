from selenium.webdriver.common.by import By
from LoginUtils import driver


class DUtils:
    @staticmethod
    def chooseDate(selectElId, date):
        for value in ["day", "month", "year", "hour", "minute"]:
            selectOptionsHandler(
                driver.find_element(By.ID, selectElId + value),
                date[value],
            )


class Date:
    def __init__(self, day, month, year, hour, minute):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute

    def __getitem__(self, item):
        return getattr(self, item)


def selectOptionsHandler(selectEl, value):
    options = selectEl.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.get_attribute("value") == str(value):
            option.click()
