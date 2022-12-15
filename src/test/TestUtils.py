from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from CourseUtils import CreateCourseUtils, RemoveCourseUtils
from AssignmentUtils import CreateAssignmentUtils
from LoginUtils import LUtils, driver
from DateUtils import Date


class TestAddAssignment:
    @staticmethod
    def test(
        username,
        password,
        courseId,
        sessionId,
        assignmentName,
        allowDate,
        dueDate,
        remindDate,
    ):
        submitStatus = None
        LUtils.login(username, password)
        CreateCourseUtils.run(
            "Course 1",
            "C1",
            Date("21", "December", "2022", "8", "30"),
            Date("28", "December", "2022", "8", "30"),
            courseId,
        )
        CreateAssignmentUtils.chooseCourse(courseId)
        CreateAssignmentUtils.chooseSessionInCourse(sessionId)
        CreateAssignmentUtils.addAssignment(
            assignmentName, allowDate, dueDate, remindDate
        )
        CreateAssignmentUtils.deleteSessionInCourse(sessionId)

        try:
            """Submit assignment fail"""
            if driver.find_element(By.ID, "id_submitbutton2").is_displayed():
                submitStatus = False
        except NoSuchElementException:
            """Submit assignment successfully"""
            submitStatus = True

        RemoveCourseUtils.run()

        LUtils.logout()
        return submitStatus

    # @staticmethod
    # def login(username, password):
    #     driver.get(url)
    #     driver.find_element(By.ID, "username").clear()
    #     driver.find_element(By.ID, "password").clear()
    #     driver.find_element(By.ID, "username").send_keys(username)
    #     driver.find_element(By.ID, "password").send_keys(password)
    #     driver.find_element(By.ID, "loginbtn").click()
    #
    # @staticmethod
    # def logout():
    #     userMenu = driver.find_element(By.ID, "user-menu-toggle")
    #     if userMenu.is_displayed():
    #         userMenu.click()
    #         driver.find_element(
    #             By.XPATH,
    #             "//a[starts-with(@href, 'http://localhost/moodle/login/logout.php')]",
    #         ).click()

    # @staticmethod
    # def chooseCourse(courseId):
    #     driver.find_element(By.XPATH, "//li[@data-key='mycourses']/a").click()
    #     driver.implicitly_wait(2)
    #     driver.find_element(
    #         By.XPATH, "//div[@data-course-id='" + str(courseId) + "']/a"
    #     ).click()
    #     time.sleep(2)
    #
    #     driver.find_element(By.XPATH, "//input[@name='setmode']").click()
    #     driver.implicitly_wait(2)
    #
    # @staticmethod
    # def chooseSessionInCourse(sessionId):
    #     collapssesection = driver.find_element(
    #         By.CSS_SELECTOR, "a#collapssesection" + str(sessionId)
    #     )
    #     if collapssesection.get_attribute("aria-expanded") == False:
    #         collapssesection.click()
    #     time.sleep(2)
    #
    #     activity_btn = driver.find_element(
    #         By.CSS_SELECTOR,
    #         "div#coursecontentcollapse" + str(sessionId) + " button",
    #     )
    #     activity_btn.click()
    #     time.sleep(2)
    #
    #     driver.find_element(By.XPATH, "//a[@title='Add a new Assignment']").click()
    # time.sleep(2)

    # @staticmethod
    # def deleteSessionInCourse(sessionId):
    #     dropDowns = driver.find_elements(
    #         By.CSS_SELECTOR,
    #         "div#coursecontentcollapse" + str(sessionId) + " div.dropdown",
    #     )
    #     for drop in dropDowns:
    #         if drop.is_displayed():
    #             drop.find_element(By.CSS_SELECTOR, "a").click()
    #             time.sleep(1)
    #
    #             drop.find_element(
    #                 By.CSS_SELECTOR,
    #                 "div.dropdown-menu > a.editing_delete",
    #             ).click()
    #             time.sleep(1)
    #
    #             driver.find_element(
    #                 By.CSS_SELECTOR,
    #                 "div.modal-content > div.modal-footer > button:last-child",
    #             ).click()
    #
    #             time.sleep(1)

    # @staticmethod
    # def chooseDate(selectElId, date):
    #     for value in ["day", "month", "year", "hour", "minute"]:
    #         selectOptionsHandler(
    #             driver.find_element(By.ID, selectElId + value),
    #             date[value],
    #         )

    # @staticmethod
    # def addAssignment(assignmentName, allowDate, dueDate, remindDate):
    #     driver.find_element(By.ID, "id_name").send_keys(assignmentName)
    #     time.sleep(2)
    #
    #     TestAddAssignment.chooseDate("id_allowsubmissionsfromdate_", allowDate)
    #     TestAddAssignment.chooseDate("id_duedate_", dueDate)
    #     TestAddAssignment.chooseDate("id_gradingduedate_", remindDate)
    #     time.sleep(2)
    #
    #     driver.find_element(By.ID, "id_submitbutton2").click()
    #     time.sleep(2)


# class Date:
#     def __init__(self, day, month, year, hour, minute):
#         self.day = day
#         self.month = month
#         self.year = year
#         self.hour = hour
#         self.minute = minute
#
#     def __getitem__(self, item):
#         return getattr(self, item)
