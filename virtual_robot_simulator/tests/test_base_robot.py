import unittest
from unittest.mock import patch
from src.robots.base_robot import Robot

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("TestRobot")

    def test_initialization(self):
        self.assertEqual(self.robot.name, "TestRobot")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, 'idle')

    def test_charge(self):
        self.robot.battery_level = 50
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, 'charging')

    def test_work(self):
        # This is an abstract method, should raise NotImplementedError
        with self.assertRaises(NotImplementedError):
            self.robot.work()

    def test_report_status(self):
        with patch('builtins.print') as mocked_print:
            self.robot.report_status()
            mocked_print.assert_called_with(
                f"Robot: {self.robot.name}\nBattery Level: {self.robot.battery_level}%\nStatus: {self.robot.status}"
            )

if __name__ == "__main__":
    unittest.main()
