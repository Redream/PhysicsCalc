# coding: utf-8
import math

GLOBAL_CONSTANT_GRAVITY = -9.81


def main():
    print("MAIN MENU:")
    menu = ["Rocket Height Calculator", "Height Fallen Calculator", "WebAssign Homework"]
    
    menucount = 0
    for s in menu:
        menucount += 1
        print(str(menucount)+") "+s)
    
    menuselect = input("Please select an option 1-"+str(len(menu))+": ")
    menuselect = check_valid_int(menuselect, 1, len(menu))
    if menuselect != -1:
        if menuselect == 1:
            vi = 9.81   # initial velocity in m/s
            vf = 0      # final velocity in m/s
            a = GLOBAL_CONSTANT_GRAVITY # displayed acceleration (a) or gravity (g)

            rocket_up_calc(vi, vf, a)
        elif menuselect == 2:
            d0 = 29.5 # initial altitude/displacement (distance in m)
            t0 = 1.55 # time in seconds, can use s or t for unit
            d0 = 30.0 # initial altitude/displacement (distance in m)
            t0 = 1.50 # time in seconds, use t or hr/m/s for unit
            height_fallen_calc(d0, t0, a)
        elif menuselect == 3:
            webmenu = ["WebAssign Week 1","WebAssign Week 2","WebAssign Week 3"]
            menucount = 0
            for s in webmenu:
                menucount += 1
                print(str(menucount)+") "+s)            
            weekselect = input("Please select an option 1-"+str(len(webmenu))+": ")
            weekselect = check_valid_int(weekselect, 1, len(webmenu))
            if weekselect != -1:
                qmenu = webassign_get_questions(weekselect)
                if type(qmenu) is str:
                    print(qmenu)
                    input("Press enter to exit. ")
                else:
                    menucount = 0
                    for s in qmenu:
                        menucount += 1
                        print(str(menucount)+") "+s)                
                    qselect = input("Please select an option 1-"+str(len(qmenu))+": ")
                    qselect = check_valid_int(qselect, 1, len(qmenu))
                    if qselect != -1:
                        webassign_do_question(weekselect, qselect)
                
def webassign_get_questions(week):
    return {
    2:["Question 1A / D",
    "Question 1B / C",
    "Question 2A",
    "Question 2B",
    "Question 3A",
    "Question 3B",
    "Question 4A",
    "Question 4B",
    "Question 4C",
    "Question 4D",
    "Question 4E",
    "Question 5A",
    "Question 5B",
    "Question 5C"]}.get(week, "Week not supported.")

def webassign_do_question(week, question):
    if week == 2:
        if question == 1:
            distance = float(input("Please enter the distance (m): "))
            force = float(input("Please enter the applied force (N): "))
            angle = float(input("Please enter the angle (degrees): "))
            answer = force*distance*math.cos(to_radians(angle))
            print("Answer to a) and d): "+str(round(answer,2))+" J")
        else:
            print("Question not supported.")
    else:
        #this shouldn't happen because we already checked for invalid weeks
        print("Week not supported.")
            
def to_radians(degrees):
    return degrees * (math.pi/180)

def to_degrees(radians):
    return radians * (180/math.pi)

def check_valid_int(number, min_num, max_num):
    try:
        number = int(number)  
    except ValueError:    
        show_invalid_option()
        return -1
    else:
        if number > max_num or number <= min_num-1:
            show_invalid_option()
            return -1
        else:
            return number
    
def show_invalid_option():
    print("Invalid option.")
    input("Press enter to exit. ")
    
def rocket_up_calc(vi, vf, a):
    """Calculate distance and time it takes a rocket to get up before it stops midair
        take initial velocity, final velocity and acceleration as arguments"""

    print('velocity initial       vi = {0} m/s'.format(vi))
    print('velocity final         vf = {0} m/s'.format(vf))
    print('acceleration (gravity) a  = {0} m/s⁻²'.format(a))
    print('█' * 30)

    print('The formula to get the DISTANCE (d) travelled before it will stop midair')
    print('░ d = (vf² - vi²) / 2a ░')
    print('change in velocity:                        ({0}² - {1}²) m/s = {2} m/s'.format(vf, vi, vf ** 2 - vi ** 2))
    print('acceleration is constant so multiply by 2: (2 x {0}) ms⁻² = {1} m/s⁻²'.format(a, 2 * a))
    print('DISTANCE travelled (d) =                   {0} m'.format((vf ** 2 - vi ** 2) / (2 * a)))

    print('█' * 30)

    print('The formula to get the TIME (t) travelled before it will stop midair')
    print('░ t = (vf - vi) / a ░')
    print('change in velocity:     ({0} - {1}) m/s = {2} m/s'.format(vf, vi, vf - vi))
    print('acceleration (gravity): ({0}) ms⁻² = {0} m/s⁻²'.format(a))
    print('TIME travelled (t) =    {0} s'.format((vf - vi) / a))

    print('█' * 30)  # http://www.fileformat.info/info/unicode/block/block_elements/images.htm


def height_fallen_calc(d0, t0, a):
    """Find the height something has fallen from, given the time and final distance before it hit the ground"""

    df = 0 # height final distance in m (eg when it hits the ground) - (s) is the standard unit for displacement
    vi = 0 # this is the initial velocity at which object started at, since it is free fall = 0 m/s

    print('Calculate the initial DISTANCE (di) given a time (t0) and final altitude (d0)')
    print('an object as last recorded at for when an object hits the ground from free-fall')
    print('█' * 30)
    print('displacement/altitude/height initial di = {0} m'.format('unknown'))
    print('displacement/altitude/height last    d0 = {0} m'.format(d0))
    print('displacement/altitude/height final   df = {0} m'.format(df))

    #print('time initial                         ti = {0} s'.format('unknown'))
    print('time last                            t0 = {0} s'.format(t0))
    #print('time final                           tf = {0} s'.format('unknown')

    print('velocity initial (because dropped)   vi = {0} m/s'.format(vi))        # u = the initial velocity (speed)
    print('velocity last                        v0 = {0} m/s'.format('unknown'))
    print('velocity final                       vf = {0} m/s'.format('unknown')) # v = the final velocity

    print('acceleration (gravity)               a  = {0} m/s⁻²'.format(a))
    print('█' * 30)


    print('The standard physics formula to find distance of (h) given the time change is:')
    print('░ h = v0t + (½)gt² ░')
    # print('The standard physics formula to find velocity of (v) given the time change is:')
    # print('░ v = v0 + at ░')

    print('Since last VELOCITY (v0) is unknown, find it by adjusting equation:')
    print('░ d0 = v0(t0) + (½)a(t0)² ░')
    print('░ v0 = (d0 -  (½)a(t0)²) / (t0) ░')

    print('  v0 = ({0} - (½)*{1}*{2}²) / {2}'.format(d0, a, t0))
    print('  v0 = ({0} - {1}) / {2} #{3}'.format(d0, 0.5 * a * t0 ** 2, t0, " NB: subtract not add here!!!"))
    print('  v0 = ({0}) / {1}'.format(d0 + 0.5 * a * t0 ** 2, t0))  # note: should be d0 - (½)a(t0)², but have changed to + sign
    print('░ v0 = {0} m/s ░'.format((d0 + 0.5 * a * t0 ** 2) / t0)) # because multiplying by negative gravity changes sign
    v0 = (d0 + 0.5 * a * t0 ** 2) / t0

    print('The kinematic equation to find VELOCITY (vf) given distance is:')
    print('░ vf² = v0² + 2aΔx ░')
    print('Calculate final VELOCITY (vf) when the object hits the ground')
    print('  vf² = v0² + 2a(df-d0)')
    print('  vf² = {0}² + 2*{1}*({2}-{3}) '.format(v0, a, df, d0))
    print('  vf² = {0} + {1}*({2}) '.format(v0 ** 2, 2 * a , df - d0))
    print('  vf² = {0} + {1} '.format(v0 ** 2, (2 * a) * (df - d0)))
    print('  vf² = {0} '.format(v0 ** 2 + (2 * a) * (df - d0)))
    print('  vf  = √{0} '.format(v0 ** 2 + (2 * a) * (df - d0)))
    print('░ vf  = {0} m/s ░'.format(math.sqrt(v0 ** 2 + (2 * a) * (df - d0))))
    vf = math.sqrt(v0 ** 2 + (2 * a) * (df - d0))

    print('The kinematic equation to find VELOCITY (vf) given distance (x) is:')
    print('░ vf² = v0² + 2aΔx ░')
    print('Since initial DISTANCE (di) is unknown, find it by adjusting equation:')
    print('░ vf² = vi² + 2a(di) ░')
    print('░ di  = (vi² - vf²) / 2a ░')

    print('  di  = ({0}² - {1}²) / 2*{2}'.format(vi, vf, a))
    print('  di  = ({0} - {1}) / {2}'.format(vi ** 2, vf ** 2, 2 * a))
    print('  di  = ({0}) / {1}'.format((vi ** 2) - vf ** 2, 2 * a))
    print('░ di  = {0} m ░'.format((vi ** 2) - vf ** 2 / (2 * a)))
    di = (vi ** 2) - vf ** 2 / (2 * a)

    print('The physics equation to find TIME (t) given displacement (d) and velocity (v) is:')
    print('░ Δt = Δd / v ░')
    print('   t = df - di / vf')
    print('   t = {0} - {1} / {2}'.format(df, di, vf))
    print('   t = {0} / {1}'.format(df - di, vf))
    print('   t = {0} s'.format(df - di / vf))
    print('This value is wrong because it not a scalar? vector?')

    print('The physics equation to find TIME (t) given acceleration (a) and velocity (v) is:')
    print('░ Δt = Δv / a ░')
    print('   t = vf - vi / a')
    print('   t = {0} - {1} / {2}'.format(vf, vi, a))
    print('   t = {0} / {1}'.format(vf - vi, a))
    print('░  t = {0} s ░ # NB: This value can be inverted'.format((vf - vi) / a))
    t = (vf - vi) / a * -1

    print('█' * 30)
    print('A certain freely falling object requires {0} s to travel the last {1} m before it hits the ground.'.format(t0, d0))
    print('Q: How fast was it travelling at the last {0} m?'.format(d0))
    print('A: {0:.2f} m/s'.format(v0))
    print('Q: How fast was it travelling when it hit the ground?')
    print('A: {0:.2f} m/s'.format(vf))
    print('Q: From what height above the ground did it fall?')
    print('A: {0:.2f} m'.format(di))
    print('Q: What was the total time spent in falling?')
    print('A: {0:.2f} s'.format(t))

main()

"""
u = the initial velocity (speed)
v = the final velocity
Example: Car accelerates from 50mph to 70mph in 10seconds. What is the acceleration?
Answer a = (v-u)/t
= (70-50)/10
= 0.5 mph / second^2
"""