import time
from selenium.webdriver.common.by import By
from LoginUtils import driver
from DateUtils import DUtils


class CreateAssignmentUtils:
    @staticmethod
    def addAssignment(assignmentName, allowDate, dueDate, remindDate):
        driver.find_element(By.ID, "id_name").send_keys(assignmentName)
        time.sleep(2)

        DUtils.chooseDate("id_allowsubmissionsfromdate_", allowDate)
        DUtils.chooseDate("id_duedate_", dueDate)
        DUtils.chooseDate("id_gradingduedate_", remindDate)
        time.sleep(2)

        driver.find_element(By.ID, "id_submitbutton2").click()
        time.sleep(2)

    @staticmethod
    def chooseCourse(courseId):
        driver.find_element(By.XPATH, "//li[@data-key='mycourses']/a").click()
        driver.implicitly_wait(2)
        # driver.find_element(
        #     By.XPATH, "//div[@data-course-id='" + str(courseId) + "']/a"
        # ).click()
        driver.find_element(By.XPATH, "//div[@role='listitem']/a").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@name='setmode']").click()
        driver.implicitly_wait(2)

    @staticmethod
    def chooseSessionInCourse(sessionId):
        collapssesection = driver.find_element(
            By.CSS_SELECTOR, "a#collapssesection" + str(sessionId)
        )
        if collapssesection.get_attribute("aria-expanded") == False:
            collapssesection.click()
        time.sleep(2)

        activity_btn = driver.find_element(
            By.CSS_SELECTOR,
            "div#coursecontentcollapse" + str(sessionId) + " button",
        )
        activity_btn.click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@title='Add a new Assignment']").click()
        time.sleep(2)

    @staticmethod
    def deleteSessionInCourse(sessionId):
        dropDowns = driver.find_elements(
            By.CSS_SELECTOR,
            "div#coursecontentcollapse" + str(sessionId) + " div.dropdown",
        )
        for drop in dropDowns:
            if drop.is_displayed():
                drop.find_element(By.CSS_SELECTOR, "a").click()
                time.sleep(1)

                drop.find_element(
                    By.CSS_SELECTOR,
                    "div.dropdown-menu > a.editing_delete",
                ).click()
                time.sleep(1)

                driver.find_element(
                    By.CSS_SELECTOR,
                    "div.modal-content > div.modal-footer > button:last-child",
                ).click()

                time.sleep(1)
