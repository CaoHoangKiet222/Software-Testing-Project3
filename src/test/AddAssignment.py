import unittest
from TestUtils import TestAddAssignment
from DateUtils import Date


class AddAssignmentSuite(unittest.TestCase):
    def test_1(self):
        """Missing assingment name"""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = ""
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("25", "December", "2022", "8", "30")
        remindDate = Date("26", "December", "2022", "8", "30")
        expect = "Missing assingment name"
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_2(self):
        """Maximum of 255 characters for assignment name"""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("25", "December", "2022", "8", "30")
        remindDate = Date("26", "December", "2022", "8", "30")
        expect = "Maximum of 255 characters for assignment name"
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_3(self):
        """Due date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "Assignment 1"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("20", "December", "2022", "8", "30")
        remindDate = Date("26", "December", "2022", "8", "30")
        expect = "Due date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_4(self):
        """Remind me to grade by date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "Assignment 1"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("25", "December", "2022", "8", "30")
        remindDate = Date("20", "December", "2022", "8", "30")
        expect = "Remind me to grade by date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_5(self):
        """Missing assingment name and due date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = ""
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("20", "December", "2022", "8", "30")
        remindDate = Date("26", "December", "2022", "8", "30")
        expect = "Missing assingment name and due date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_6(self):
        """Missing assingment name and remind me to grade by date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = ""
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("25", "December", "2022", "8", "30")
        remindDate = Date("20", "December", "2022", "8", "30")
        expect = "Missing assingment name and remind me to grade by date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_7(self):
        """Maximum of 255 characters for assignment name and due date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("20", "December", "2022", "8", "30")
        remindDate = Date("26", "December", "2022", "8", "30")
        expect = "Maximum of 255 characters for assignment name and due date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_8(self):
        """Maximum of 255 characters for assignment name and remind me to grade by date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("20", "December", "2022", "8", "30")
        remindDate = Date("26", "December", "2022", "8", "30")
        expect = "Maximum of 255 characters for assignment name and remind me to grade by date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_9(self):
        """Missing assingment name and due date cannot be earlier than the allow submissions from date and remind me to grade by date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = ""
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("20", "December", "2022", "8", "30")
        remindDate = Date("20", "December", "2022", "8", "30")
        expect = "Missing assingment name and due date cannot be earlier than the allow submissions from date and remind me to grade by date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_10(self):
        """Maximum of 255 characters for assignment name and due date cannot be earlier than the allow submissions from date and remind me to grade by date cannot be earlier than the allow submissions from date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("20", "December", "2022", "8", "30")
        remindDate = Date("20", "December", "2022", "8", "30")
        expect = "Missing assingment name and due date cannot be earlier than the allow submissions from date and remind me to grade by date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_11(self):
        """Maximum of 255 characters for assignment name and remind me to grade by date cannot be earlier than the due date."""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("25", "December", "2022", "8", "30")
        remindDate = Date("23", "December", "2022", "8", "30")
        expect = "Missing assingment name and due date cannot be earlier than the allow submissions from date and remind me to grade by date cannot be earlier than the allow submissions from date."
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )

    def test_12(self):
        """Add assingment correctly with nomal assignment name"""
        username = "user"
        password = "bitnami"
        courseId = 6
        sessionId = 1
        assignmentName = "Assignment 1"
        allowDate = Date("21", "December", "2022", "8", "30")
        dueDate = Date("25", "December", "2022", "8", "30")
        remindDate = Date("1", "January", "2023", "8", "30")
        expect = "Submit assignment successfully"
        self.assertTrue(
            TestAddAssignment.test(
                username,
                password,
                courseId,
                sessionId,
                assignmentName,
                allowDate,
                dueDate,
                remindDate,
            ),
            expect,
        )
