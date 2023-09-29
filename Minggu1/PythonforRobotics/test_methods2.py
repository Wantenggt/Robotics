from robot_control_class import RobotControl

robotcontrol = RobotControl(robot_name="summit")

def get_laser_values(a,b,c):
    r1 = robotcontrol.get_laser_summit(a)
    r2 = robotcontrol.get_laser_summit(b)
    r3 = robotcontrol.get_laser_summit(c)

    return [r1, r2, r3]

l = get_laser_values(0, 500, 1000)

print ("Reading 1: ", l[0])
print ("Reading 2: ", l[1])
print ("Reading 3: ", l[2])