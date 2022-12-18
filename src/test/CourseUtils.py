from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from DateUtils import DUtils
from LoginUtils import driver


class CreateCourseUtils:
    URLCREATECOURSE = "http://localhost/course/edit.php?category=0"

    @staticmethod
    def run(fName, sName, startDate, endDate, id):
        driver.get(CreateCourseUtils.URLCREATECOURSE)
        # Course FullName
        CreateCourseUtils.textFieldHandler(fName, "id_fullname")

        # Course ShortName
        CreateCourseUtils.textFieldHandler(sName, "id_shortname")

        # Check for StartDate
        DUtils.chooseDate("id_startdate_", startDate)

        # Check for EndDate
        DUtils.chooseDate("id_enddate_", endDate)

        # Check for Course Id
        courseId = driver.find_element(By.ID, "id_idnumber")
        courseId.clear()
        courseId.send_keys(str(id))
        time.sleep(3)

        # Check SaveAndDisplay Btn
        btnSaveAndDisplay = driver.find_element(By.ID, "id_saveanddisplay")
        btnSaveAndDisplay.click()

        try:
            """Failly Add Course"""
            if driver.find_element(By.ID, "id_saveanddisplay").is_displayed():
                return False
        except NoSuchElementException:
            """Successfully Add Course"""
            return True

    @staticmethod
    def textFieldHandler(value, fieldId):
        textEl = driver.find_element(By.ID, fieldId)
        textEl.clear()
        textEl.send_keys(str(value))


class RemoveCourseUtils:
    URLREMOVECOURSE = "http://localhost/course/management.php"
    REMOVECOURSE_ICON_XPATH = (
        "//a[starts-with(@href, 'http://localhost/course/delete.php')]"
    )
    DELETECOURSE_BTN_XPATH = "//form[@method='post']//button[@type='submit']"

    @staticmethod
    def run():
        driver.get(RemoveCourseUtils.URLREMOVECOURSE)

        try:
            icon = driver.find_element(
                By.XPATH, RemoveCourseUtils.REMOVECOURSE_ICON_XPATH
            )
            if icon.is_displayed():
                time.sleep(0.5)
                icon.click()
                time.sleep(0.5)
                driver.find_element(
                    By.XPATH, RemoveCourseUtils.DELETECOURSE_BTN_XPATH
                ).click()
                driver.get(RemoveCourseUtils.URLREMOVECOURSE)
                return True
        except NoSuchElementException:
            return False
