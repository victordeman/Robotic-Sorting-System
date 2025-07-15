from robodk import robolink
RDK = robolink.Robolink()
robot = RDK.Item('Kuka', robolink.ITEM_TYPE_ROBOT)
robot.MoveJ([0, 0, 0, 0, 0, 0])  # Example movement
