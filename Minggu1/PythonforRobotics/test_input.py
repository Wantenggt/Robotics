from robot_control_class import RobotControl

num = int(input("Select a number between 0 and 719: "))

rc = RobotControl()
a = rc.get_laser(num)

print ("The laser value received is: ", a)