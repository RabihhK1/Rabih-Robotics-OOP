import unittest
from unittest.mock import patch
from src.robots.cooking_robot import CookingRobot

class TestCookingRobot(unittest.TestCase):

    def setUp(self):
        self.cooking_robot = CookingRobot("TestCookingRobot", "expert")

    def test_initialization(self):
        self.assertEqual(self.cooking_robot.name, "TestCookingRobot")
        self.assertEqual(self.cooking_robot.cooking_skill, "expert")
        self.assertEqual(self.cooking_robot.battery_level, 100)
        self.assertEqual(self.cooking_robot.status, 'idle')

    def test_work(self):
        self.cooking_robot.work()
        self.assertEqual(self.cooking_robot.status, 'working')
        self.assertLessEqual(self.cooking_robot.battery_level, 100)
        self.assertGreaterEqual(self.cooking_robot.battery_level, 70)  # Decreases by 30%

    def test_report_status(self):
        with patch('builtins.print') as mocked_print:
            self.cooking_robot.report_status()
            mocked_print.assert_called_with(
                f"Robot: {self.cooking_robot.name}\nBattery Level: {self.cooking_robot.battery_level}%\nStatus: {self.cooking_robot.status}"
            )

if __name__ == "__main__":
    unittest.main()
