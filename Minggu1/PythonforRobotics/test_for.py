from robot_control_class import RobotControl

robotcontrol = RobotControl()

l = robotcontrol.get_laser_full()

maxim = 0

for value in l:
    if value > maxim:
        maxim = value

print ("The higher value in the list is: ", maxim)