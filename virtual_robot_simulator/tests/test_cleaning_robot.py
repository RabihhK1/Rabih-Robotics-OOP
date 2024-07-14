import unittest
from unittest.mock import patch
from src.robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):

    def setUp(self):
        self.cleaning_robot = CleaningRobot("TestCleaningRobot", "vacuum")

    def test_initialization(self):
        self.assertEqual(self.cleaning_robot.name, "TestCleaningRobot")
        self.assertEqual(self.cleaning_robot.cleaning_tool, "vacuum")
        self.assertEqual(self.cleaning_robot.battery_level, 100)
        self.assertEqual(self.cleaning_robot.status, 'idle')

    def test_work(self):
        self.cleaning_robot.work()
        self.assertEqual(self.cleaning_robot.status, 'working')
        self.assertLessEqual(self.cleaning_robot.battery_level, 100)
        self.assertGreaterEqual(self.cleaning_robot.battery_level, 80)  # Decreases by 20%

    def test_report_status(self):
        with patch('builtins.print') as mocked_print:
            self.cleaning_robot.report_status()
            mocked_print.assert_called_with(
                f"Robot: {self.cleaning_robot.name}\nBattery Level: {self.cleaning_robot.battery_level}%\nStatus: {self.cleaning_robot.status}"
            )

if __name__ == "__main__":
    unittest.main()
