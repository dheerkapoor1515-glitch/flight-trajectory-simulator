import math
import PHYSICS


Angle = int(input("ENTER ANGLE: "))
Radian = math.radians(Angle)
Initial_velocity = int(input("ENTER INITIAL VELOCITY: "))

vx = PHYSICS.calculate_horizontal_velocity(Initial_velocity, Radian)
vy = PHYSICS.calculate_vertical_velocity(Initial_velocity, Radian)
g = PHYSICS.g
mh = PHYSICS.calculate_maximum_height(vy, g)
t = PHYSICS.calculate_time(vy, g)
r = PHYSICS.calculate_horizontal_range(vx, t)

print()
print(f"HORIZONTAL VELOCITY = {vx :.2f} m/s")
print(f"VERTICAL VELOCITY = {vy :.2f} m/s")
print(f"MAXIMUM HEIGHT = {mh :.2f} m")
print(f"TIME = {t :.2f} s")
print(f"HORIZONTAL RANGE = {r :.2f} m")
