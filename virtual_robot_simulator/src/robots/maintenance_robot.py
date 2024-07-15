from .cleaning_robot import CleaningRobot
from .cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    """
    A robot that can perform both cleaning and cooking tasks.

    Attributes:
        name (str): The name of the robot.
        battery_level (int): The battery level of the robot, from 0 to 100.
        status (str): The status of the robot, can be 'idle', 'working', or 'charging'.
        cleaning_tool (str): The cleaning tool used by the robot.
        cooking_skill (str): The cooking skill level of the robot.
    """

    def __init__(self, name: str, cleaning_tool: str, cooking_skill: str)-> None:
        """
        Initialize a MaintenanceRobot instance.

        Args:
            name (str): The name of the robot.
            cleaning_tool (str): The cleaning tool used by the robot.
            cooking_skill (str): The cooking skill level of the robot.
        """
        
        CleaningRobot.__init__(self, name, cleaning_tool)
        CookingRobot.__init__( self, name, cooking_skill)

    def multi_task(self) -> None:
        """
        Perform a cleaning task followed by a cooking task.
        """
        print(f"{self.name} is starting multitasking.")
        CleaningRobot.work(self) 
        CookingRobot.work(self) 
        print(f"{self.name} has completed multitasking.")
        print("MRO: ", MaintenanceRobot.__mro__)