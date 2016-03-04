GLOBAL_CONSTANT_GRAVITY = -9.81


def main():
    vi = 9.81  # initial velocity in m/s
    vf = 0  # final velocity in m/s
    a = GLOBAL_CONSTANT_GRAVITY

    rocket_up_time(vi, vf, a)


def rocket_up_time(vi, vf, a):
    """ Calculate distance and time it takes a rocket to get up before it stops midair
        take initial velocity, final velocity and acceleration as arguments """

    print("velocity intial vi = {0} m/s".format(vi))in
    print("velocity final vf = {0} m/s".format(vf))
    print("acceleration (gravity) = {0} m/s^-2".format(a))

    print(u"\u2588" * 30)

    print("The formula to get the DISTANCE (d) travelled before it will stop midair")
    print(u"\u2591" + " (vf^2 - vi^2) / 2a " + u"\u2591")
    print("change in velocity ({0}^2 - {1}^2) m/s = {2} m/s".format(vf, vi, vf ** 2 - vi ** 2))
    print("acceleration is constant so multiply by 2 (2 x {0}) ms^-2 = {1} m/s^-2".format(a, 2 * a))

    print("DISTANCE travelled = {0} m".format((vf ** 2 - vi ** 2) / (2 * a)))

    print(u"\u2588" * 30)

    print("The formula to get the TIME (t) travelled before it will stop midair")
    print(u"\u2591" + " (vf - vi) / a " + u"\u2591")
    print('change in velocity ({0} - {1}) m/s = {2} m/s'.format(vf, vi, vf - vi))
    print("acceleration is just gravity acting down ({0}) ms^-2 = {0} m/s^-2".format(a))
    print("TIME travelled = {0} s".format((vf - vi) / (a)))

    print(u"\u2588" * 30)  # http://www.fileformat.info/info/unicode/block/block_elements/images.htm


main()
