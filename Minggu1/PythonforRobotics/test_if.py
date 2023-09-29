from robot_control_class import RobotControl

robotcontrol = RobotControl()

a = robotcontrol.get_laser(360)

if a < 1:
    robotcontrol.stop_robot()

else:
    robotcontrol.move_straight()

print ("The laser value received was: ", a)