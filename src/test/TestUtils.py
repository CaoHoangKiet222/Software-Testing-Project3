import time
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
        CreateAssignmentUtils.chooseSessionInCourse(sessionId)
        CreateAssignmentUtils.addAssignment(
            assignmentName, allowDate, dueDate, remindDate
        )
        try:
            """Submit assignment fail"""
            if driver.find_element(By.ID, "id_submitbutton2").is_displayed():
                submitStatus = False
        except NoSuchElementException:
            """Submit assignment successfully"""
            submitStatus = True

        CreateAssignmentUtils.deleteSessionInCourse(sessionId)

        RemoveCourseUtils.run()

        LUtils.logout()
        return submitStatus
