from src.robots.cleaning_robot import CleaningRobot
from src.robots.cooking_robot import CookingRobot
from src.robots.maintenance_robot import MaintenanceRobot  # Assuming you have implemented this class

def main():
    # Create instances of CleaningRobot, CookingRobot, and MaintenanceRobot
    cleaning_robot = CleaningRobot("CleanerBot", "vacuum")
    cooking_robot = CookingRobot("ChefBot", "expert")
    maintenance_robot = MaintenanceRobot("MaintenanceBot", "vacuum", "expert")

    # Display initial status
    print("\nInitial Status:")
    print("---------------")
    cleaning_robot.report_status()
    cooking_robot.report_status()
    maintenance_robot.report_status()

    # Perform tasks
    print("\nPerforming Tasks:")
    print("-----------------")
    cleaning_robot.work()
    cooking_robot.work()
    maintenance_robot.multi_task()

    # Display status after tasks
    print("\nStatus After Tasks:")
    print("-------------------")
    cleaning_robot.report_status()
    cooking_robot.report_status()
    maintenance_robot.report_status()

    # Charge the robots
    print("\nCharging Robots:")
    print("----------------")
    cleaning_robot.charge()
    cooking_robot.charge()
    maintenance_robot.charge()

    # Display final status after charging
    print("\nFinal Status After Charging:")
    print("-----------------------------")
    cleaning_robot.report_status()
    cooking_robot.report_status()
    maintenance_robot.report_status()

if __name__ == "__main__":
    main()
