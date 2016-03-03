GLOBAL_CONSTANT_GRAVITY = -9.81

def main():
    vi = 119 # initial velocity in m/s
    vf = 0   # final velocity in m/s
    a = GLOBAL_CONSTANT_GRAVITY

    rocket_up_time(vi, vf, a)

def rocket_up_time(vi, vf, a):
""" Calculate distance and time it takes a rocket to get up before it stops midair
    take initial velocity, final velocity and acceleration as operators """
  print("velocity intial vi = " + str(vi) + "m/s")
  print("velocity final vf = " + str(vf) + "m/s")
  print("acceleration (gravity) = " + str(a))
  
  print("The formula to get the DISTANCE (d) travelled before it will stop and come back down "
            u"\u2591" + " (vf^2 - vi^2) / 2a " + u"\u2591")
  print("change in velocity (" + str(vf) + "^2 - " + str(vi) + "^2) m/s = " + str(vf **2 - vi ** 2) + " m/s")
  print("acceleration is constant so multiply by 2 (2 x " + str(a) + ") ms^-2= " + str(2 * a) + " m/s^-2")
  print("DISTANCE travelled = " + str((vf ** 2 - vi ** 2) / (2 * a)) + " m")
  
  print(u"\u2588" * 30)
  
  print("The formula to get the TIME (t) travelled before it will stop and come back down "
            u"\u2591" + " (vf - vi) / a " + u"\u2591")
  print("change in velocity (" + str(vf) + " - " + str(vi) + ") m/s = " + str(vf - vi) + " m/s")
  print("acceleration is just gravity acting down (" + str(a) + ") ms^-2= " + str(a) + " m/s^-2")
  print("TIME travelled = " + str((vf - vi) / (a)) + " s")
  
  print(u"\u2588" * 30)

# http://www.fileformat.info/info/unicode/block/block_elements/images.htm

main()
