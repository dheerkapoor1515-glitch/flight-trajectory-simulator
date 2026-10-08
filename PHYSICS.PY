import math
#-----------------------------------------------

g = 9.81


#------------------------------------------------ 

def calculate_horizontal_velocity(Initial_velocity, Radian):
	vx = Initial_velocity * math.cos(Radian)
	return vx

#---------------------------------------------------------------

def calculate_vertical_velocity(Initial_velocity , Radian):
	vy = Initial_velocity * math.sin(Radian)
	return vy

#-----------------------------------------------------------

def calculate_maximum_height(vy, g):
    mh = math.pow(vy, 2) / (2 * g)
    return mh

#---------------------------------------------------------------

def calculate_time(vy , g):
	t = 2 *vy / g
	return t

#---------------------------------------------------------------

def calculate_horizontal_range(vx , t):
	r = vx * t
	return r

#---------------------------------------------------------------

