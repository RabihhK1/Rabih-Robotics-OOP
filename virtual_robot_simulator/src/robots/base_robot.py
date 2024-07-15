from abc import ABC, abstractmethod
from typing import Dict
class Robot(ABC):
    """
    A base class representing a robot.

    Attributes:
        _name (str): The name of the robot.
        _battery_level (int): The battery level of the robot (0 to 100).
        _status (str): The current status of the robot ('idle', 'working', 'charging').

    Methods:
        __init__(name: str):
            Initializes a new Robot instance with the given name.
        charge():
            Increases the battery level of the robot to 100 and sets status to 'charging'.
        work():
            Abstract method to be implemented by subclasses.
        report_status():
            Prints the current status of the robot.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new Robot instance.

        Args:
            name (str): The name of the robot.
        """
        self._name: str = name
        self._battery_level: int = 100  # Default to fully charged
        self._status: str = 'idle'

    @property
    def name(self) -> str:
        """Getter for the name of the robot."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter for the name of the robot.

        Args:
            value (str): The new name of the robot.
        """
        self._name = value

    @property
    def battery_level(self) -> int:
        """Getter for the battery level of the robot."""
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value: int) -> None:
        """
        Setter for the battery level of the robot.

        Args:
            value (int): The new battery level of the robot (0 to 100).
        
        Raises:
            ValueError: If the battery level is outside the range 0 to 100.
        """
        if 0 <= value <= 100:
            self._battery_level = value
        else:
            raise ValueError("Battery level must be between 0 and 100")

    @property
    def status(self) -> str:
        """Getter for the status of the robot."""
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """
        Setter for the status of the robot.

        Args:
            value (str): The new status of the robot ('idle', 'working', 'charging').
        
        Raises:
            ValueError: If the status is not one of 'idle', 'working', or 'charging'.
        """
        if value in ['idle', 'working', 'charging']:
            self._status = value
        else:
            raise ValueError("Status must be 'idle', 'working', or 'charging'")

    def charge(self) -> None:
        """
        Charges the robot by setting the battery level to 100 and status to 'charging'.
        """
        self.battery_level = 100
        self.status = 'charging'
        print(f"{self.name} is now fully charged.")

    @abstractmethod
    def work(self) -> None:
        """
        Abstract method representing the work behavior of the robot.
        To be implemented by subclasses.
        """
        pass

    def report_status(self) -> None:
        """
        Prints the current status of the robot.
        """
        print(f"Robot: {self.name}")
        print(f"Battery Level: {self.battery_level}%")
        print(f"Status: {self.status}")


    def self_diagnose(self) -> Dict[str, str]:
        """
        Perform a self-diagnosis of the robot and report any issues.

        Returns:
            Dict[str, str]: A dictionary with diagnostic information.
        """
        diagnostics = {
            "name": self._name,
            "battery_level": "Low" if self._battery_level < 20 else "Normal",
            "status": self._status
        }
        return diagnostics

    @staticmethod
    def utility_method() -> str:
        """
        A static method for utility functions.

        Returns:
            str: A static message.
        """
        return "Utility method called"

    @classmethod
    def class_method(cls) -> str:
        """
        A class method for utility functions related to the class.

        Returns:
            str: A class method message.
        """
        return f"Class method called from {cls._name_}"