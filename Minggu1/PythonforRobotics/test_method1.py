from robot_control_class import RobotControl
import time

robotcontrol = RobotControl(robot_name="summit")

def move_x_seconds(secs):
    robotcontrol.move_straight()
    time.sleep(secs)
    robotcontrol.stop_robot()


move_x_seconds(5)