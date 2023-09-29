from robot_control_class import RobotControl

robotcontrol = RobotControl()

laser1 = robotcontrol.get_laser(0)
print ("The laser value received is: ", laser1)

laser2 = robotcontrol.get_laser(360)
print ("The laser value received is: ", laser2)

laser2 = robotcontrol.get_laser(719)
print ("The laser value received is: ", laser2)