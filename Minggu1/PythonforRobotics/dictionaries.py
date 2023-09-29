from robot_control_class import RobotControl

rc = RobotControl()

l = rc.get_laser_full()

dict = {"P0": l[0], "P100": l[100], "P200": l[200], "P300": l[300], "P400": l[400], "P500": l[500], "P600": l[600], "P719": l[719]}

print (dict)

'''
Muhammad Ikhwan Maulana
1103203219
TK-44-01
'''