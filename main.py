# coding: utf-8
import math

GLOBAL_CONSTANT_GRAVITY = -9.81


def main():
    print("MAIN MENU:")
    menu = ["WebAssign Homework", "Manual"]
    
    menucount = 0
    for s in menu:
        menucount += 1
        print(str(menucount)+") "+s)
    
    menuselect = input("Please select an option 1-"+str(len(menu))+": ")
    menuselect = check_valid_int(menuselect, 1, len(menu))
    if menuselect != -1:

        if menuselect == 1:
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
                        input("Press enter to exit. ")

        elif menuselect == 2:
            manualmenu = ["Rocket Height Calculator",
                       "Height Fallen Calculator",
                       "Race car on a circular race track",
                       "Bucket falling",
                        ]
            menucount = 0
            for s in manualmenu:
                menucount += 1
                print(str(menucount)+") "+s)

            manualselect = input("Please select an option 1-"+str(len(manualmenu))+": ")
            manualselect = check_valid_int(manualselect, 1, len(manualmenu))
            if manualselect != -1:
                if manualselect == 1:
                    vi = 119   # initial velocity in m/s 
                    vf = 0      # final velocity in m/s
                    a = GLOBAL_CONSTANT_GRAVITY # displayed acceleration (a) or gravity (g)
                    rocket_up_calc(vi, vf, a)
                elif manualselect == 2:
                    d0 = 25.0 # initial altitude/displacement (distance in m) 
                    t0 = 1.80 # time in seconds, use t or hr/m/s for unit
                    a = GLOBAL_CONSTANT_GRAVITY # displayed acceleration (a) or gravity (g)
                    height_fallen_calc(d0, t0, a)
                elif manualselect == 3:
                    race_car_circular_track()
                elif manualselect == 4:
                    bucket_falling_into_well()

def webassign_get_questions(week):
    return {
    1:["Question 3",
    "Question 4"],
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
    "Question 5C"],
    3:["Question 1A",
    "Question 1B",
    "Question 2A",
    "Question 2B",
    "Question 2C",
    "Question 3A",
    "Question 3B",
    "Question 4A",
    "Question 4B",
    "Question 5A/B"]}.get(week, "Week not supported.")

def webassign_do_question(week, question):
    if week == 1:
        if question == 1:
            vi = float(input("Please enter the initial velocity (m/s): "))
            rocket_up_calc(vi, 0, GLOBAL_CONSTANT_GRAVITY)
        if question == 2:
            d0 = float(input("Please enter the last distance (m): "))
            t0 = float(input("Please enter the last time (s): "))
            height_fallen_calc(d0, t0, GLOBAL_CONSTANT_GRAVITY)
    elif week == 2:
        if question == 1:
            distance = float(input("Please enter the distance (m): "))
            force = float(input("Please enter the applied force (N): "))
            angle = float(input("Please enter the angle (degrees): "))
            answer = force*distance*math.cos(to_radians(angle))
            print("Answer to a) and d): "+str(round(answer,2))+" J")
        else:
            print("Question not supported.")
    elif week == 3:
        if question == 10:
            m1 = float(input("Please input mass m1 (kg): "))
            m2 = float(input("Please input mass m2 (kg): "))
            radius = float(input("Please input radius (m): "))
            hm1 = float(input("Please input height of m1 from floor (m): "))
            moment = 0.5*5*radius**2 + m1*radius**2 + m2*radius**2
            tnet = (m1-m2)*9.81*radius
            alpha = tnet/moment
            lina = radius*alpha
            temp = hm1/0.5/lina
            time = math.sqrt(temp)
            print("Answer to 5a) "+str(round(time,4))+" s")
            
            moment = m1*radius**2 + m2*radius**2
            alpha = tnet/moment
            lina = radius*alpha
            temp = hm1/0.5/lina
            time = math.sqrt(temp)
            print("Answer to 5b) "+str(round(time,4))+" s")
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


def race_car_circular_track():
    """
    brief:    Race car on a circular race track
    from:     WebAssign Homework 5.1
    category: circular motion
    types:    velocity, angular momentum, tangential acceleration, angular momentum
    """

    # quantities
    # related to dimensions of the circle
    r = [444, 'm'] # r: radius length - m

    # related to angular momentum in the center of the circle
    O = [0, 'rad']     # θ: angular displacement - rad     (θ = ωt)
    w = [0, 'rad s⁻¹'] # ω: angular velocity     - rad s⁻¹ (ω = v/r)
    a = [0, 'rad s⁻²'] # α: angular acceleration - rad s⁻² (α = ω/r)

    # related to the kinematics of the car travelling on the circumference of the circle
    # http://www.slideshare.net/caitlinforan/rotational-motion-7142158
    d = [0, 'm']         # d: distance travelled       - m     (d = rθ)
    v = [0, 'm s⁻¹']     # v: velocity                 - m s⁻¹ (v = rω)
    aT = [0.34, 'm s⁻²'] # aT: tangential acceleration - m s⁻² (aT = v²/r) OR (aT = rα)
    t = [0, 's']         # t: time                     - s

    print('-' * 30)
    print("A race car starts from rest on a circular track of radius {} {}.".format(r[0], r[1]))
    print("The car's speed increases at the constant rate of {} {}.".format(aT[0], aT[1]))
    print("At the point where the magnitudes of the centripetal and tangential accelerations are equal, find the following.")
    print("(a) the speed of the race car m/s")
    print("(b) the distance traveled m")
    print("(c) the elapsed time s")

    print('░ question a ░')
    print('centripetal acceleration:   aT = v²/r')
    print('rearrange to solve velocity: v = √(aT * r)')
    print('v = √({} {} * {} {})'.format(aT[0], aT[1], r[0], r[1]))
    v[0] = math.sqrt(aT[0] * r[0])
    print('v = {:.2f} {}'.format(v[0], v[1]))

    print('░ question b ░')
    # http://physicsnet.co.uk/a-level-physics-as-a2/further-mechanics/circular-motion/
    print('angular velocity: ω = v/r')
    print('ω = {:.2f} {} / {} {}'.format(v[0], v[1], r[0], r[1]))
    w[0] = v[0] / r[0]
    print('ω = {:.5f} {}'.format(w[0], w[1]))

    print('angular acceleration: α = aT/R')
    print('α = {:.5f} {} / {} {}'.format(aT[0], aT[1], r[0], r[1]))
    a[0] = aT[0] / r[0]
    print('α = {:.2e} {}'.format(a[0], a[1]))

    print('constant angular acceleration (without time): ω² = ω₀² + 2αθ')
    print('since ω is zero initially: ω² = 2αθ')
    print('rearrange to solve angular displacement: θ = ω² / 2α')
    print('θ = ({0:.5f} {1} ²) / (2 * {2:.2e} {3})'.format(w[0], w[1], a[0], a[1]))
    O[0] = (w[0] ** 2) / (2 * a[0])
    print('θ = {:.2f} {}'.format(O[0], O[1]))

    print('linear angular displacement: d = rθ')
    print('d = {} {} * {} {}'.format(r[0], r[1], O[0], O[1]))
    d[0] = r[0] * O[0]
    print('d = {} {}'.format(d[0], d[1]))

    print('░ question c ░')
    print('angular position: θ₂ = θ₁ + ωt + ½αt²')
    print('since ω and θ is zero initially: θ = ½αt²')
    print('rearrange to solve time: t = √(2 * θ / α)')
    print('t = √(2 * {0} {1} / {2:.2e} {3})'.format(O[0], O[1], a[0], a[1]))
    t[0] = math.sqrt(2 * O[0] / a[0])
    print('t = {:.2f} {}'.format(t[0], t[1]))


def bucket_falling_into_well():
    """
    brief:    Bucket attached via string to a spool falling down
    from:     WebAssign Homework 5.4
    category: circular motion
    types:    conservation of energy
    """

    # related to the spool
    M = [3.0, 'kg']    # M: mass of spool
    R = [0.6, 'm']     # r: radius length
    w = [0, 'rad s⁻¹'] # ω: angular velocity     - (ω = v/r)
    I = [0, 'kg m²']   # I: moment of inertia    - (I = MR²) * default model

    # related to the bucket
    mB = [3.0, 'kg']    # mB: mass of bucket
    d = [4.8, 'm']      # d: distance travelled
    g = [9.81, 'm s⁻²'] # g: gravity

    print('-' * 30)
    print("Use conservation of energy to determine the angular speed of a spool (solid cylinder about a central axis)")
    print("after the 3.00 kg bucket has fallen 4.80 m, starting from rest")
    print("The light string attached to the bucket is wrapped around the spool and does not slip as it unwinds.")
    print("(a) the angular speed rad/s")

    print('░ question a ░')

    print('GPEinit = KErotf + KEtransf')
    print('GPEinit = mgd')
    print('KErotf = ½Iω²')
    print('KEtransf = ½mv²')

    print('no-slip condition:')
    print('v = ωr')

    # http://spiff.rit.edu/classes/phys216/workshops/w9b/momi_table.png
    # rotational inertia
    print('rotational inertia (solid cylinder about a central axis): I = ½MR²')
    print('I = 0.5 * {} {} * {} {} ²'.format(M[0], M[1], R[0], R[1]))
    I[0] = 0.5 * M[0] * R[0]
    print('I = {} {}'.format(I[0], I[1]))

    print('You will end up deriving the angular speed of the spool to be this:')
    print('ω = √(2*mB*gd / (I + mB*r²))')
    print('ω = √(2 * {0} {1} * {2} {3} * {4} {5} / ({6} {7} + {0} {1} * {8} {9} ²))'.format(mB[0], mB[1], g[0], g[1], d[0], d[1], I[0], I[1], R[0], R[1]))
    w[0] = math.sqrt(2 * mB[0] * g[0] * d[0] / (I[0] + mB[0] * R[0] ** 2))
    print('ω = {:.2f} {}'.format(w[0], w[1]))

    print('where:')
    print('mB {} {}: is the mass of the bucket'.format(mB[0], mB[1]))
    print('r {} {}: is the radius of the spool'.format(R[0], R[1]))
    print('I {} {}: is the rotational inertia of the spool'.format(I[0], I[1]))
    print('g {} {}: is Earths gravitational field'.format(g[0], g[1]))
    print('d {} {}: is the distance of descent of the bucket from rest to final state.'.format(d[0], d[1]))




"""
T₁ - 0 = m₁∙a
T₁ = 3∙a . . . . . . . equation 1

Equation for m₂ :
m₂∙g - T₂ = m₂∙a
4∙9.8 - T₂ = 4∙a
39.2 - T₂ = 4∙a
T₂ = 39.2 - 4∙a . . . . . . . . equation 2

Equation for the pulley:
r∙T₂ - r∙T₁ = a ∙ I/r
0.3∙T₂ - 0.3∙T₁ = a∙0.5/0.3
0.18∙T₂ - 0.18∙T₁ = a . . . . . . . equation 3

Substitute equation 1 and 2 in equation 3
0.18∙(39.2 - 4∙a) - 0.18∙3∙a = a
7.056 - 0.72∙a - 0.54∙a = a

7.056 = 2.26∙a
a = 3.12 m/s² < - - - - - - - - - - - - - - - - - - - - - - - - answer

Substitute that value in equations 1 and 2

T₁ = 3∙3.12 = 9.36 N < - - - - - - - - - - - - - - - - - - - answer

T₂ = 39.2 - 4∙0.32 = 26.7 N < - - - - - - - - - - - - - -answer
"""



"""
Tₐ - Tᵦ = Iα
let mₐ = 4 kg, mᵦ = 3 kg
Tₐ = ?, Tᵦ = ? a = ?
moment due to the difference in tension is Tₐ - Tᵦ = Iα ---------------------> (i)
mₐg - Tₐ = mₐa
and mᵦa = Tᵦ
adding equations => mₐg -(Tₐ - Tᵦ) = a[mₐ + mᵦ] = mₐg - Iα [from equation (i)]
since α = a/r => 7a = 4g - 0.5(a)/0.290
=> 8.7a = 4(9.81)
or a = 4.498 m/s²
Tᵦ = mᵦa = 3(4.498) = 13.494 N
Tₐ = mₐ[g - a] = 21.25 N
Check: [equation (i)]
Tₐ - Tᵦ = Iα = 7.755 = 0.5(4.498/0.290) which is true
"""


"""
theta = theta0 + wt + .5angular acceleration * t^2
theta = .5at^2, since angular speed is zero initially and angular displacement is zero.
root(2theta/a) = t
t = root(2*.5/9.94x10^-4) = 31.7 s
"""



main()

