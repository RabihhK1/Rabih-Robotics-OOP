from .base_robot import Robot

class CleaningRobot(Robot):
    """
    A subclass representing a cleaning robot.

    Attributes:
        cleaning_tool (str): The tool used for cleaning (e.g., 'vacuum', 'mop').

    Methods:
        work():
            Implements the cleaning behavior of the cleaning robot. Decreases battery level by 20 for each cleaning session.
    """

    def __init__(self, name: str, cleaning_tool: str) -> None:
        """
        Initializes a new CleaningRobot instance.

        Args:
            name (str): The name of the cleaning robot.
            cleaning_tool (str): The tool used for cleaning.
        """
        self._name: str = name
        self._battery_level: int = 100  # Default to fully charged
        self._status: str = 'idle'
        self.cleaning_tool=cleaning_tool

    @property
    def cleaning_tool(self) -> str:
        """Getter for the cleaning tool used by the robot."""
        return self._cleaning_tool

    @cleaning_tool.setter
    def cleaning_tool(self, value: str) -> None:
        """
        Setter for the cleaning tool used by the robot.

        Args:
            value (str): The new cleaning tool to be set.
        """
        self._cleaning_tool = value

    def work(self) -> None:
        """
        Implements the cleaning behavior of the cleaning robot.
        Decreases battery level by 20 for each cleaning session.
        """
        if self.battery_level > 0:
            self.status = 'working'
            print(f"{self.name} is cleaning with {self.cleaning_tool}.")
            self.battery_level -= 20  # Decrease battery level by 20% per cleaning session
            if self.battery_level <= 0:
                self.battery_level = 0
                self.status = 'idle'
                print(f"{self.name}'s battery is dead. Please charge.")
        else:
            self.status = 'idle'
            print(f"{self.name} cannot work. Battery level is {self.battery_level}%.")
