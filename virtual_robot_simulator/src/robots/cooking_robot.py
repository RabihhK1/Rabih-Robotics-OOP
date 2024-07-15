from .base_robot import Robot

class CookingRobot(Robot):
    """
    A subclass representing a cooking robot.

    Attributes:
        _cooking_skill (str): The cooking skill level of the robot (e.g., 'beginner', 'intermediate', 'expert').

    Methods:
        work():
            Implements the cooking behavior of the cooking robot. Decreases battery level by 30 for each cooking session.
    """

    def __init__(self, name: str, cooking_skill: str) -> None:
        """
        Initializes a new CookingRobot instance.

        Args:
            name (str): The name of the cooking robot.
            cooking_skill (str): The skill level of the cooking robot ('beginner', 'intermediate', 'expert').
        """
        self._name: str = name
        self._battery_level: int = 100  # Default to fully charged
        self._status: str = 'idle'
        self.cooking_skill=cooking_skill

    @property
    def cooking_skill(self) -> str:
        """Getter for the cooking skill level of the robot."""
        return self._cooking_skill

    @cooking_skill.setter
    def cooking_skill(self, value: str) -> None:
        """
        Setter for the cooking skill level of the robot.

        Args:
            value (str): The new cooking skill level to be set.
        """
        self._cooking_skill = value

    def work(self) -> None:
        """
        Implements the cooking behavior of the cooking robot.
        Decreases battery level by 30 for each cooking session.
        """
        if self.battery_level > 0:
            self.status = 'working'
            print(f"{self.name} is cooking with {self.cooking_skill} skill.")
            self.battery_level -= 30  # Decrease battery level by 30% per cooking session
            if self.battery_level <= 0:
                self.battery_level = 0
                self.status = 'idle'
                print(f"{self.name}'s battery is dead. Please charge.")
        else:
            self.status = 'idle'
            print(f"{self.name} cannot work. Battery level is {self.battery_level}%.")
