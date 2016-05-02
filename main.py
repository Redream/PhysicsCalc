# coding: utf-8
import math

def main():
    manualmenu = [
        "Water Bottle Experiment",
    ]

    webmenu = [
        "WebAssign Week 1",
        "WebAssign Week 2",
        "WebAssign Week 3",
        "WebAssign Week 4",
        "WebAssign Week 5",
        "WebAssign Week 6",
        "WebAssign Week 7",
    ]

    print("MAIN MENU:")
    menu = ["PHYS111 WebAssign Homework", "PHYS101 WebAssign Homework","Own"]

    menucount = 0
    for s in menu:
        menucount += 1
        print(str(menucount) + ") " + s)

    menuselect = input("Please select an option 1-" + str(len(menu)) + ": ")
    menuselect = check_valid_int(menuselect, 1, len(menu))
    if menuselect != -1:

        if menuselect == 1:
            ## webmenu
            menucount = 0
            for s in webmenu:
                menucount += 1
                print(str(menucount) + ") " + s)
            weekselect = input("Please select an option 1-" + str(len(webmenu)) + ": ")
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
                        print(str(menucount) + ") " + s)
                    qselect = input("Please select an option 1-" + str(len(qmenu)) + ": ")
                    qselect = check_valid_int(qselect, 1, len(qmenu))
                    if qselect != -1:
                        webassign_do_question(weekselect, qselect)
                        input("Press enter to exit. ")

        elif menuselect == 3:
            menucount = 0
            for s in manualmenu:
                menucount += 1
                print(str(menucount) + ") " + s)

            manualselect = input("Please select an option 1-" + str(len(manualmenu)) + ": ")
            manualselect = check_valid_int(manualselect, 1, len(manualmenu))
            if manualselect != -1:
                if manualselect == 1:
                    water_bottle_experiment()
                elif manualselect == 2:
                    v0 = input("Initial velocity (m/s): ")
                elif manualselect == 3:
                    t = input("Time (s): ")
                elif manualselect == 4:
                    race_car_circular_track()

def webassign_get_questions(week):
    return {
        1: ["Question 2",
            "Question 3",
            "Question 4"],
        2: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4"],
        3: ["Question 1",
            "Question 2",
            "Question 3"],
        4: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4"],
        5: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4"],
        6: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4"],        
        7: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            ]}.get(week, "Week not supported.")

def webassign_do_question(week, question):
    if week == 1:
        if question == 1:
            x = input("Length (m): ")
            v0 = input("Initial speed (km/h): ")
            vf = input("Final speed (km/h): ")
            if not (v0 and vf and x): train_stopping_time()
            else: train_stopping_time(v0c=float(v0), vfc=float(vf), xc=float(x))
        if question == 2:
            v0 = input("Initial velocity (m/s): ")
            if not v0: arrow_shot_up()
            else: arrow_shot_up(v0c=float(v0))
        if question == 3:
            t = input("Time (s): ")
            x = input("Distance (m): ")
            if not (x and t): original_height_fallen_from()
            else: original_height_fallen_from(xc=float(x), tc=float(t))
    elif week == 2:
        if question == 1:
            m = input("Mass (m): ")
            F = input("Force (F): ")
            vf = input("Final velocity (km/h): ")
            if not (m and F and vf): train_acceleration_time()
            else: train_acceleration_time(mc=float(m), Fc=float(F), vfc=float(vf))
        if question == 2:
            a = input("Acceleration (m/s²): ")
            m = input("Mass (kg): ")
            if not (a and m): tension_two_masses_elevator()
            else: tension_two_masses_elevator(mc=float(m), ac=float(a))
        if question == 3:
            m = input("Mass (kg): ")
            v0 = input("Initial velocity (m/s): ")
            vf = input("Final velocity (m/s): ")
            t = input("Time (s): ")
            if not (m and v0 and vf and t): force_distance_slowing_car()
            else: force_distance_slowing_car(mc=float(m), v0c=float(v0), vfc=float(vf), tc=float(t))
        if question == 4:
            m1 = input("Mass 1 (kg): ")
            m2 = input("Mass 2 (kg): ")
            if not (m1 and m2): m2_gtr_m1_atwood_machine()
            else: m2_gtr_m1_atwood_machine(m1c=float(m1), m2c=float(m2))
        #else:
            #distance = float(input("Please enter the distance (m): "))
            #force = float(input("Please enter the applied force (N): "))
            #angle = float(input("Please enter the angle (degrees): "))
            #answer = force * distance * math.cos(to_radians(angle))
            #print("Answer to a) and d): " + str(round(answer, 2)) + " J")
            #print("Question not supported.")
    elif week == 3:
        if question == 1:
            m = input("Mass (g): ")
            v0 = input("Initial velocity (m/s): ")
            x = input("Distance (cm): ")
            if not (m and v0): energy_and_force_of_bullet()
            else: energy_and_force_of_bullet(mc=float(m), v0c=float(v0), xc=float(x))
        if question == 2:
            m = input("Mass (kg): ")
            xh = input("Height (m): ")
            xd = input("Depth (mm): ")
            if not (m and xh and xd): impact_of_ball_on_plate()
            else: impact_of_ball_on_plate(mc=float(m), xhc=float(xh), xdc=float(xd))
        if question == 3:
            m1 = input("mass1 (kg): ")
            m2 = input("mass2 (kg): ")
            xh = input("height (m): ")
            if not (m1 and m2 and xh): atwood_machine_passing()
            else: atwood_machine_passing(m1c=float(m1), m2c=float(m2), xhc=float(xh))
        # if question == 10:
        #     m1 = float(input("Please input mass m1 (kg): "))
        #     m2 = float(input("Please input mass m2 (kg): "))
        #     radius = float(input("Please input radius (m): "))
        #     hm1 = float(input("Please input height of m1 from floor (m): "))
        #     moment = 0.5 * 5 * radius ** 2 + m1 * radius ** 2 + m2 * radius ** 2
        #     tnet = (m1 - m2) * 9.81 * radius
        #     alpha = tnet / moment
        #     lina = radius * alpha
        #     temp = hm1 / 0.5 / lina
        #     time = math.sqrt(temp)
        #     print("Answer to 5a) " + str(round(time, 4)) + " s")
        #
        #     moment = m1 * radius ** 2 + m2 * radius ** 2
        #     alpha = tnet / moment
        #     lina = radius * alpha
        #     temp = hm1 / 0.5 / lina
        #     time = math.sqrt(temp)
        #     print("Answer to 5b) " + str(round(time, 4)) + " s")
        # else:
        #     print("Question not supported.")
    elif week == 4:
        if question == 1:
            J = input("impulse (N s⁻¹): ")
            m = input("mass (kg): ")
            v0 = input("initial velocity (m s⁻¹): ")
            if not (J and m and v0): impulse_collision()
            else: impulse_collision(Jc=float(J), mc=float(m), v0c=float(v0))
        if question == 2:
            m = input("mass (kg): ")
            v = input("velocity (m s⁻¹): ")
            O = input("angle (degrees): ")
            t = input("time (s): ")
            if not (m and v and O and t): ball_bounce_wall_angle()
            else: ball_bounce_wall_angle(mc=float(m), vc=float(v), Oc=float(O), tc=float(t))
        if question == 3:
            m1 = input("mass golf club (g): ")
            m2 = input("mass golf ball (g): ")
            v0 = input("initial velocity (m s⁻¹): ")
            vf = input("final velocity (m s⁻¹): ")
            if not (m1 and m2 and v0 and vf): golf_ball_speed()
            else: golf_ball_speed(m1c=float(m1), m2c=float(m2), v0c=float(v0), vfc=float(vf))
        if question == 4:
            m1 = input("mass 1 (kg): ")
            v1 = input("velocity 1 (m s⁻¹): ")
            m2 = input("mass 2 (kg): ")
            O = input("angle (°): ")
            vf = input("final velocity (m s⁻¹): ")
            if not (m1 and v1 and m2 and O and vf): car_collision_angle()
            else: car_collision_angle(m1c=float(m1), v1c=float(v1), m2c=float(m2), Oc=float(O), vfc=float(vf))
    elif week == 5:
        if question == 1:
            race_car_circular_track()
        if question == 2:
            print("hi")
        if question == 3:
            print("hi")
        if question == 4:
            bucket_falling_into_well()
    elif week == 6:
        if question == 1:
            print("hi")
        if question == 2:
            print("hi")
        if question == 3:
            f = input("Please enter the frequency (Hz): ")
            if not f: wave_period_speed()
            else: wave_period_speed(fc=float(f))
        if question == 4:
            print("hi")
    elif week == 7:
        if question == 1:
            I = input("ampere (µA): ")
            if not (I): electrons_hitting_tv()
            else: electrons_hitting_tv(Ic=float(I))
        if question == 2:
            R = input("ohms (Ω): ")
            V = input("voltage (V): ")
            if not (R and V): current_light_bulb()
            else: current_light_bulb(Rc=float(R), Vc=float(V))

    else:
        # this shouldn't happen because we already checked for invalid weeks
        print("Week not supported.")





def to_radians(degrees):
    return degrees * (math.pi / 180)

def to_degrees(radians):
    return radians * (180 / math.pi)

def check_valid_int(number, min_num, max_num):
    try:
        number = int(number)
    except ValueError:
        show_invalid_option()
        return -1
    else:
        if number > max_num or number <= min_num - 1:
            show_invalid_option()
            return -1
        else:
            return number

def show_invalid_option():
    print("Invalid option.")
    input("Press enter to exit. ")


def print_maths_evaluate(operator, solve, t1, t2):
    """
    Prints solve, which is term 1 (t1) operated by term 2 (t2)
    Returns solve
    """
    if isinstance(t1, (int, float, complex)):
        print('{} = {} {} {:{}} {}'.format(solve[2], t1, operator, t2[1], t2[4], t2[3]))
        solve[1] = eval('{} {} {}'.format(t1, operator, t2[1]))
        print('{} = {:{}} {}'.format(solve[2], solve[1], solve[4], solve[3]))
    elif isinstance(t2, (int, float, complex)):
        print('{} = {:{}} {} {} {}'.format(solve[2], t1[1], t1[4], t1[3], operator, t2))
        solve[1] = eval('{} {} {}'.format(t1[1], operator, t2))
        print('{} = {:{}} {}'.format(solve[2], solve[1], solve[4], solve[3]))
    else:
        print('{} = {:{}} {} {} {:{}} {}'.format(solve[2], t1[1], t1[4], t1[3], operator, t2[1], t2[4], t2[3]))
        solve[1] = eval('{} {} {}'.format(t1[1], operator, t2[1]))
        print('{} = {:{}} {}'.format(solve[2], solve[1], solve[4], solve[3]))
    return solve

def print_convert_kmh_ms(a):
    """
    Divides a by 3.6
    Returns a
    """
    a[1] = a[1] / 3.6
    print('{0} = {1:{2}} {4} / 3.6 = {1:{2}} {3}'.format(a[2], a[1], a[4], a[3], 'km/h'))

def print_convert_ms_kmh(a):
    """
    Multiplies a by 3.6
    Returns a
    """
    a[1] = a[1] * 3.6
    print('{0} = {1:{2}} {3} * 3.6 = {1:{2}} {4}'.format(a[2], a[1], a[4], a[3], 'km/h'))

def print_convert_absolute(a):
    """
    converts a into absolute, may be useful for convert vector to scalar
    Returns a
    """
    print('convert vector to absolute value for scalar')
    a[1] = abs(a[1])
    print('abs({0}) = {1:{2}} {3}'.format(a[2], a[1], a[4], a[3]))
    
def print_area_of_circle(A, r):
    """
    Takes r (radius) and converts to area of a circle
    Returns A (Area)
    """
    print('area of a circle: πr²')
    A[1] = math.pi * r[1]**2
    print('{0} = {1:{2}} {3}'.format(A[2], A[1], A[4], A[3]))

def print_mechanics_motion1(solve, v, v0, a, t):
    """ velocity (without x): v = v₀ + at """
    print('velocity (without x): v = v₀ + at')

    if solve[2] == a[2]:
        print('rearrange to solve acceleration: a = Δv / t')
        print('{} = ({:{}} {} - {:{}} {}) / {:{}} {}'.format(a[2], v[1], v[4], v[3], v0[1], v0[4], v0[3], t[1], t[4], t[3]))
        a[1] = (v[1] - v0[1]) / t[1]
        print('{} = {:{}} {}'.format(a[2], a[1], a[4], a[3]))
        return a
    if solve[2] == t[2]:
        print('rearrange to solve time: t = Δv / a')
        print('{} = ({:{}} {} - {:{}} {}) / {:{}} {}'.format(t[2], v[1], v[4], v[3], v0[1], v0[4], v0[3], a[1], a[4], a[3]))
        t[1] = (v[1] - v0[1]) / a[1]
        print('{} = {:{}} {}'.format(t[2], t[1], t[4], t[3]))
        return t

def print_mechanics_motion2(solve, x, v0, v, t):
    """ change in x (without acceleration): Δx = ½(v₀ + v)t """
    print('change in x (without acceleration): Δx = ½(v₀ + v)t')

    if solve[2] == x[2]:
        print('solve distance: Δx = ∑v*t / 2')
        print('{} = (({:{}} {} + {:{}} {}) * {:{}} {}) / 2'.format(x[2], v0[1], v0[4], v0[3], v[1], v[4], v[3], t[1], t[4], t[3]))
        x[1] = ((v0[1] + v[1]) * t[1]) / 2
        print('{} = {:{}} {}'.format(x[2], x[1], x[4], x[3]))
        return x

def print_mechanics_motion3(solve, x, v0, t, a):
    """ change in x (without final velocity): Δx = v₀t + ½at """
    print('change in x (without final velocity): Δx = v₀t + ½at')

    if solve[2] == x[2]:
        print('{0} = ({1:{2}} {3} * {4:{5}} {6}) + (0.5 * {7:{8}} {9} * {4:{5}} {6})'.format(x[2], v0[1], v0[4], v0[3], t[1], t[4], t[3], a[1], a[4], a[3]))
        x[1] = (v0[1] * t[1]) + (0.5 * a[1] * t[1])
        print('{} = {:{}} {}'.format(x[2], x[1], x[4], x[3]))
        return x

    if solve[2] == v0[2]:
        print('rearrange to solve initial velocity: v₀ = Δx - ½at² / t')
        print('{0} = ({1:{2}} {3} - 0.5 * {4:{5}} {6} * {7:{8}} {9} ^2) / {7:{8}} {9}'.format(v0[2], x[1], x[4], x[3], a[1], a[4], a[3], t[1], t[4], t[3]))
        v0[1] = (x[1] - 0.5 * a[1] * t[1] ** 2) / t[1]
        print('{} = {:{}} {}'.format(v0[2], v0[1], v0[4], v0[3]))
        return v0

def print_mechanics_motion4(solve, v, v0, a, x):
    """ velocity (without time): v² = v₀² + 2aΔx """
    print('velocity (without time): v² = v₀² + 2aΔx')

    if v0 == 0:
        v0 = ['initial velocity', 0, 'v₀', 'm s⁻¹', '.2f', 'vector']

    if solve[2] == v[2]:
        print('{0} = sqrt({1:{2}} {3} ^2 + 2 * {4:{5}} {6} * {7:{8}} {9})'.format(v[2], v0[1], v0[4], v0[3], a[1], a[4], a[3], x[1], x[4], x[3]))
        v[1] = math.sqrt(v0[1] ** 2 + 2 * a[1] * x[1])
        print('{} = {:{}} {}'.format(v[2], v[1], v[4], v[3]))
        return v

    if solve[2] == a[2]:
        print('rearrange to solve acceleration: a = Δv / 2Δx')
        print('{} = ({:{}} {} ^2 - {:{}} {} ^2) / (2 * {:{}} {})'.format(a[2], v[1], v[4], v[3], v0[1], v0[4], v0[3], x[1], x[4], x[3]))
        a[1] = (v[1] ** 2 - v0[1] ** 2) / (2 * x[1])
        print('{} = {:{}} {}'.format(a[2], a[1], a[4], a[3]))
        return a
    if solve[2] == x[2]:
        print('rearrange to solve distance: Δx = Δv / 2a')
        print('{} = ({:{}} {} ^2 - {:{}} {} ^2) / (2 * {:{}} {})'.format(x[2], v[1], v[4], v[3], v0[1], v0[4], v0[3], a[1], a[4], a[3]))
        x[1] = (v[1] ** 2 - v0[1] ** 2) / (2 * a[1])
        print('{} = {:{}} {}'.format(x[2], x[1], x[4], x[3]))
        return x

def print_atwood_machine(solve, m1, m2, g, aT):
    """
    solve acceleration or tension in an atwood machine
    Both are solved independently of each other
    """
    a = ['acceleration', 0, 'a', 'm s⁻²', '.2f', 'scalar']
    T = ['tension', 0, 'T', 'N', '.1f', 'scalar']
    if aT[2] == 'a':
        a = aT
    elif aT[2] == 'T':
        T = aT
    else:
        print('ERROR')
    if m1[1] > m2[1]:
        x = m1 # x = heavier
        y = m2 # y = lighter
    if m2[1] > m1[1]:
        x = m2 # x = heavier
        y = m1 # y = lighter

    print('In an atwood machine: T1 = T2')
    print('where {} > {}'.format(x[2],y[2]))
    print('T - {0}g = {0}a'.format(y[2]))
    print('{0}g - T = {0}a'.format(x[2]))

    if solve[2] == a[2]:
        print('rearrange to solve for a')
        print('{0}g - T + T - {1}g = {0}a + {1}a'.format(x[2], y[2]))
        print('{0}g - {1}g = {0}a + {1}a'.format(x[2], y[2]))
        print('({0} - {1})g = ({0} + {1})a'.format(x[2], y[2]))
        print('({0} - {1})g = ({0} + {1})a'.format(x[2], y[2]))
        print('a = ({0} - {1})g / ({0} + {1})'.format(x[2], y[2]))
        print('{0} = (({1:{2}} {3} - {4:{5}} {6}) * {7:{8}} {9}) / ({4:{5}} {6} + {1:{2}} {3})'.format(a[2], x[1], x[4], x[3], y[1], y[4], y[3], g[1], g[4], g[3]))
        a[1] = ((x[1] - y[1]) * g[1]) / (y[1] + x[1])
        print('{} = {:{}} {}'.format(a[2], a[1], a[4], a[3]))
        return a
    if solve[2] == T[2]:
        print('rearrange to solve for T')
        print('a = (T - {0}g) / {0}'.format(y[2]))
        print('a = ({0}g - T) / {0}'.format(x[2]))
        print('(T - {0}g) / {0} = ({1}g - T) / {1}'.format(y[2], x[2]))
        print('{1}(T - {0}g) = {0}({1}g - T)'.format(y[2], x[2]))
        print('{1}T - {0}{1}g = {0}{1}g - {0}T'.format(y[2], x[2]))
        print('{1}T + {0}T = {0}{1}g + {0}{1}g'.format(y[2], x[2]))
        print('T({1} + {0}) = 2({0}{1}g)'.format(y[2], x[2]))
        print('T = (2({0}{1}g))/({1} + {0})'.format(y[2], x[2]))
        print('{0} = (2 * {1:{2}} {3} * {4:{5}} {6} * {7:{8}} {9}) / ({4:{5}} {6} + {1:{2}} {3})'.format(T[2], y[1], y[4], y[3], x[1], x[4], x[3], g[1], g[4], g[3]))
        T[1] = (2 * y[1] * x[1] * g[1]) / (y[1] + x[1])
        print('{} = {:{}} {}'.format(T[2], T[1], T[4], T[3]))
        return T

def print_impulse(solve, J, v, m):
    """
    Impulse: a quantity that describes the effect of a net force acting on an object (a kind of "moving force")
    a vector quantity (since force is a vector and time is a scalar)
    N s = kg m/s

    product of the average net force acting on an object and its duration
    J = FΔt

    The impulse-momentum theorem states that the change in momentum of an object equals the impulse applied to it.
    J = Δp
    p = mv

    If mass is constant
    FΔt = mΔv
    """

    print('impulse: J = FΔt = mΔv')

    if solve[2] == v[2]:
        print('rearrange to solve velocity: Δv = J/m')
        print_maths_evaluate('/', v, J, m)
        return v

def print_work_done(solve, W, F, x, O=1):
    """
    Work: ‘Transfer of energy’
    Quantitatively: The work W done by a constant force on an object is the product of the force along the direction of displacement and the magnitude of displacement.
    W = (Fcosθ)Δx
    Units: N/m = Joule
    Work: (Fcosθ)Δx
    ΔW = KE
    """

    print('work: W=(Fcosθ)Δx')

    if solve[2] == F[2]:
        print('rearrange to solve force: F = W/Δx')
        print_maths_evaluate('/',F,W,x)
        return F

def print_potential_spring_energy(solve, KE, k, v):
    """Potential Energy of spring: PEspring = ½kv²"""

def print_potential_energy_gravity(solve, PE, m, g, h):
    """
    Potential Energy of gravity: PE-grav = mgh
    """
    print('potential energy of gravity: PE-grav = mgh')
    if solve[2] == h[2]:
        print('rearrange to solve height: h = PE-grav/mg')
        print('{} = {:{}} {} / ({:{}} {} * {:{}} {})'.format(h[2], PE[1], PE[4], PE[3], m[1], m[4], m[3], g[1], g[4], g[3]))
        h[1] = PE[1] / (m[1] * g[1])
        print('{} = {:{}} {}'.format(h[2], h[1], h[4], h[3]))
        return PE

def print_kinectic_energy(solve, KE, m, v):
    """
    kinetic energy: KE = ½mv²
    ΔW = KE
    """
    print('kinetic energy: KE = ½mv²')

    if solve[2] == KE[2]:
        print('{} = 0.5 * {:{}} {} * {:{}} {} ^2'.format(KE[2], m[1], m[4], m[3], v[1], v[4], v[3]))
        KE[1] = 0.5 * m[1] * v[1] ** 2
        print('{} = {:{}} {}'.format(KE[2], KE[1], KE[4], KE[3]))
        return KE

def print_conservation_energy(solve, KE, PE, m, v, g, h):
    """
    kinetic energy: KE = ½mv²
    potential energy: PE = mgh
    KE = PE
    """
    print('kinetic energy: KE = ½mv²')

    if solve[2] == KE[2]:
        print('{} = 0.5 * {:{}} {} * {:{}} {} ^2'.format(KE[2], m[1], m[4], m[3], v[1], v[4], v[3]))
        KE[1] = 0.5 * m[1] * v[1] ** 2
        print('{} = {:{}} {}'.format(KE[2], KE[1], KE[4], KE[3]))
        return KE

def print_rotational_motion1(solve, s, r, O):
    """ rotational motion: s = rθ """
    print('linear angular displacement: s = rθ')

"""
    print('tangental velocity: v-tan = rω')
    print('tangental acceleration: a-tan = rα')

    print('centripetal acceleration: a-cen = v²/r = ω²r')


    τ = Iα
    τ = rFsinθ
    L = Iω

    Angular kinetic energy E in Joules: E = ½Iω²
    ω is angular velocity in radians/sec
    I = moment of inertia in kg*m²

    moment of inertia
    I is moment of inertia in kg•m²
    I = cMR²
    M is mass (kg), R is radius (meters)
    c = 1 for a ring or hollow cylinder
    c = 2/5 solid sphere
    c = ⅔ hollow sphere
    c = ½ solid cylinder or disk around its center
    c = 1/12 rod around its center, R = length
    c = ⅓ for a rod around its end, R = length
"""

def print_amps_and_coulomb_equivalent(solve, A, Q):
    """
    ⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉ ⁻
    SI multiples for coulomb (C) Submultiples 		Multiples
    Value 	SI symbol 	Name 	Value 	 	SI symbol 	Name
    10^−1 C 	dC 	decicoulomb 	10^1 C 	 	daC 	decacoulomb
    10^−2 C 	cC 	centicoulomb 	10^2 C 	 	hC 	hectocoulomb
    10^−3 C 	mC 	millicoulomb 	10^3 C 	 	kC 	kilocoulomb
    10^−6 C 	µC 	microcoulomb 	10^6 C 	 	MC 	megacoulomb
    10^−9 C 	nC 	nanocoulomb 	10^9 C 	 	GC 	gigacoulomb
    10^−12 C 	pC 	picocoulomb 	10^12 C 	TC 	teracoulomb
    10^−15 C 	fC 	femtocoulomb 	10^15 C 	PC 	petacoulomb
    10^−18 C 	aC 	attocoulomb 	10^18 C 	EC 	exacoulomb
    10^−21 C 	zC 	zeptocoulomb 	10^21 C 	ZC 	zettacoulomb
    10^−24 C 	yC 	yoctocoulomb 	10^24 C 	YC 	yottacoulomb

    Table of ampere unit prefixes
    name 	 	 	 	symbol 	 conversion 	 example    
    microampere (microamps) 	 	µA 	1µA = 10^-6A 	I = 50µA
    milliampere (milliamps) 	 	mA 	1mA = 10^-3A 	I = 3mA
    ampere (amps) 	 			 	A 	- 	 			I = 10A
    kiloampere (kiloamps) 		 	kA 	1kA = 10^3A 	I = 2kA

    """
    print('Ampere: a unit of electrical change equal to one coulomb of charge per second 1A = 1C/s')    
    print('Amperes are used to express flow rate of electric charge 1A = 1C/s')
    # print('C = amps/sec')
    # print('Amps = coul/sec')
    print('Current = Charge/Time')
    print('I = Q/t')
    print('Where:')
    print('I = Current in Amperes (A)')
    print('Q = Charge in Coulombs (C)')
    print('t = time (s)')
    
    if solve[2] == Q[2]:
        if A[3] == 'µA':
            print('equivalent of a microampere (µA) is microcoulomb (µC)')
            print('1 µA = 1 µC/s = 10⁻⁶ C/s')
            Q[1] = A[1] * 0.000001
            Q[3] = 'µC'
            print('{} = {:{}} {}'.format(Q[2], Q[1], Q[4], Q[3]))
            return Q

def print_ohms_law(solve, V, I, R):
    """
    Ohm's Law is V = I x R where V = Voltage, I = Current and R = Resistance
    One ohm is the resistance value through which one volt will maintain a current of one ampere
    """
    print('Ohms Law: V = IR')

    if solve[2] == V[2]:
        print('solve voltage: V = IR')
        print('{} = {:{}} {} * {:{}} {})'.format(V[2], I[1], I[4], I[3], R[1], R[4], R[3]))
        V[1] = I[1] * R[1]
        print('{} = {:{}} {}'.format(V[2], V[1], V[4], V[3]))
        return V

    if solve[2] == I[2]:
        print('rearrange to solve current: I = V/R')
        print('{} = {:{}} {} * {:{}} {}'.format(V[2], I[1], I[4], I[3], R[1], R[4], R[3]))
        I[1] = V[1] / R[1]
        print('{} = {:{}} {}'.format(I[2], I[1], I[4], I[3]))
        return I
    if solve[2] == R[2]:
        print('rearrange to solve resistance: R = V/I')
        print('{} = {:{}} {} * {:{}} {})'.format(V[2], I[1], I[4], I[3], R[1], R[4], R[3]))
        R[1] = V[1] / I[1]
        print('{} = {:{}} {}'.format(R[2], R[1], R[4], R[3]))
        return R


# webassign 1
def train_stopping_time(v0c=82.0, vfc=15.1, xc=350):
    """
    brief:    find time it takes for a train to pass during negative acceleration
    from:     WebAssign Homework 1.2
    category: acceleration
    types:    motion in 1D
    """
    
    v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.1f', 'vector']
    vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.1f', 'vector']
    x = ['change in distance', xc, 'Δx', 'm', '.0f', 'scalar']
    t = ['time', 0, 't', 's', '.1f', 'scalar']
    a = ['acceleration', 0, 'a', 'm s⁻²', '.2f', 'scalar']

    print('-' * 30)
    print("A train {:{}} {} long is moving on a straight track with a speed of {:{}} {}".format(x[1], x[4], x[3], v0[1], v0[4], 'km/h'))
    print("The engineer applies the brakes at a crossing, and later the last car passes the crossing with a speed of {:{}} {}.".format(vf[1], vf[4], 'km/h'))
    print("Disregard the width of the crossing and assume constant acceleration,")
    print("(a)determine how long the train blocked the crossing. s")

    print('░ question a ░')
    print('convert km/h to m/s: x / 3.6')
    print_convert_kmh_ms(vf)
    print_convert_kmh_ms(v0)

    # solve acceleration: a = Δv / 2Δx'
    print_mechanics_motion4(a, vf, v0, a, x)

    # solve time: t = Δv / a
    print_mechanics_motion1(t, vf, v0, a, t)

def arrow_shot_up(v0c=119, vfc=0, ac=-9.81):
    """
    brief:    find time and distance of an arrow that will stop midair
    from:     WebAssign Homework 1.3
    category: acceleration
    types:    motion in 1D
    """
    v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.2f', 'vector']
    vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.2f', 'vector']
    x = ['change in distance', 0, 'Δx', 'm', '.0f', 'scalar']
    g = ['gravity', ac, 'g', 'm s⁻²', '.2f', 'vector']
    t = ['time', 0, 't', 's', '.1f', 'scalar']

    print('-' * 30)
    print("It is possible to shoot an arrow at a speed as high as {:{}} {}".format(v0[1], v0[4], v0[3]))
    print("If friction is neglected")
    print("(a) how high would an arrow launched at this speed rise if shot straight up? m")
    print("(b) how long would the arrow be in the air? s")

    print('░ question a ░')
    # solve distance: Δx = Δv / 2a
    print_mechanics_motion4(x, vf, v0, g, x)

    print('░ question b ░')
    # solve time: t = Δv / a
    print_mechanics_motion1(t, vf, v0, g, t)
    print('multiply by 2 as the arrow must return to earth')
    print_maths_evaluate('*', t, t, 2)

def original_height_fallen_from(xc=25, tc=1.8, ac=9.81):
    """
    brief:    find height of an object fallen from
    from:     WebAssign Homework 1.4
    category: acceleration
    types:    motion in 1D
    """
    # height starts at 0 and increases, so use positive for both direction and acceleration
    xi = ['start height', +0, 'xi', 'm', '.1f', 'scalar']
    x0 = ['last height', xc, 'x₀', 'm', '.1f', 'scalar']
    #xf = ['final height', 0, 'xf', 'm', '.1f', 'scalar'] # y-axis starts at 0 here

    g = ['gravity', ac, 'g', 'm s⁻²', '.2f', 'vector']

    # velocity gets faster
    vi = ['start velocity', 0, 'vi', 'm s⁻¹', '.2f', 'vector']
    v0 = ['last velocity', +0, 'v₀', 'm s⁻¹', '.2f', 'vector']
    vf = ['final velocity', +0, 'vf', 'm s⁻¹', '.2f', 'vector']

    # time counts up
    #ti = ['start time', 0, 'ti', 's', '.2f', 'scalar']
    t0 = ['last time', tc, 't₀', 's', '.2f', 'scalar']
    #tf = ['final time', +0, 'tf', 's', '.2f', 'scalar']


    print('A certain freely falling object requires {:{}} {} to travel the last {:{}} {} before it hits the ground.'.format(t0[1], t0[4], t0[3], x0[1], x0[4], x0[3]))
    print('(a)From what height above the ground did it fall? m')

    print('░ question a ░')
    # solve last velocity: v₀ = Δx - ½at² / t
    print_mechanics_motion3(v0, x0, v0, t0, g)

    # solve final velocity: v² = v₀² + 2aΔx
    print_mechanics_motion4(vf, vf, v0, g, x0)

    # rearrange to solve start height: Δx = (v² - v₀²) / 2a
    print_mechanics_motion4(xi, vf, vi, g, xi)

# webassign 2
def train_acceleration_time(mc=17000000, Fc=740000, vfc=76, v0c=0):
    """
    brief:    find time it takes for object to reach speed
    from:     WebAssign Homework 2.1
    category: Newton's second law
    types:    force, constant acceleration
    """

    m = ['mass', mc, 'm', 'kg', '.1e', 'scalar']
    F = ['force', Fc, 'F', 'N', '.1e', 'scalar']
    t = ['time', 0, 't', 's', '.1f', 'scalar']
    v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.2f', 'vector']
    vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.2f', 'vector']
    a = ['acceleration', 0, 'a', 'm s⁻²', '.2f', 'scalar']

    print('A freight train has a mass of {:{}} {}.'.format(m[1], m[4], m[2]))
    print('If the locomotive can exert a constant pull of {:{}} {}'.format(F[1], F[4], F[2]))
    print('(a) how long does it take to increase the speed of the train from rest to {:{}} {}?'.format(vf[1], vf[4], 'km/h'))

    print('░ question a ░')
    print('convert km/h to m/s: x / 3.6')
    print_convert_kmh_ms(vf)
    print_convert_kmh_ms(v0)

    print('acceleration: a = F/m')
    print_maths_evaluate('/', a, F, m)

    # solve change in t
    print_mechanics_motion1(t, vf, v0, a, t)
    print('convert to minutes: x / 60')
    print_maths_evaluate('/', t, t, 60)

def tension_two_masses_elevator(ac=2.30, mc=13.5, gc=9.81):
    """
    brief:    find tension in 2 attached masses in a moving elevator
    from:     WebAssign Homework 2.2
    category: tension force
    types:    constant acceleration, opposing acceleration, Newton's second law
    """

    m = ['mass', mc, 'm', 'kg', '.1f', 'scalar']
    a = ['acceleration', ac, 'a', 'm s⁻²', '.2f', 'scalar']
    g = ['gravity', gc, 'a', 'm s⁻²', '.2f', 'scalar']
    ar = ['acceleration acting on the rope', ac, 'ar', 'm s⁻²', '.2f', 'scalar']
    T1 = ['force', 0, 'F', 'N', '.2f', 'scalar']
    T2 = ['force', 0, 'F', 'N', '.2f', 'scalar']
    Em = ['combined mass acting on the top rope', mc, '∑m', 'kg', '.1f', 'scalar']

    print('Two blocks are fastened to the ceiling of an elevator.')
    print('The elevator accelerates upward at {:{}} {}. The blocks both have a mass of {:{}} {}.'.format(a[1], a[4], a[3], m[1], m[4], m[3]))
    print('Find the tension in each rope.')
    print('(a) top rope N')
    print('(b) bottom rope N')

    print('░ question a ░')
    # tension will increase, because moving in opposite direction of gravity. combine acceleration and gravity
    print_maths_evaluate('+', ar, a, g)
    # tension in the top rope is the sum of all masses
    print_maths_evaluate('+', Em, m, m)
    # F = ma
    print_maths_evaluate('*', T1, Em, ar)

    print('░ question b ░')
    # F = ma
    print_maths_evaluate('*', T2, m, ar)

def force_distance_slowing_car(mc=2000, v0c=19.0, vfc=10.0, tc=5.60):
    """
    brief:    find force and distance of a car decelerating
    from:     WebAssign Homework 2.3
    category: Newton's second law
    types:    force, uniform negative acceleration,
    """

    m = ['mass', mc, 'm', 'kg', '.0f', 'scalar']
    v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.1f', 'vector']
    vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.1f', 'vector']
    t = ['time', tc, 't', 's', '.2f', 'scalar']
    F = ['force', 0, 'F', 'N', '.0f', 'scalar']
    x = ['change in distance', 0, 'Δx', 'm', '.1f', 'scalar']
    a = ['acceleration', 0, 'a', 'm s⁻²', '.2f', 'scalar']

    print('-' * 30)
    print('A {:{}} {} car is slowed down uniformly from {:{}} {} to {:{}} {} in {:{}} {}.'.format(m[1], m[4], m[3], v0[1], v0[4], v0[3], vf[1], vf[4], vf[3], t[1], t[4], t[3]))
    print('(a) What average total force acted on the car during that time? N')
    print('(b) How far did the car travel during that time? m')

    print('░ question a ░')
    # solve acceleration: a = Δv / t'
    print_mechanics_motion1(a, vf, v0, a, t)
    # F = ma
    print_maths_evaluate('*', F, m, a)

    print('░ question b ░')
    # solve distance: Δx = ∑v*t / 2'
    print_mechanics_motion2(x, x, v0, vf, t)

def m2_gtr_m1_atwood_machine(m1c=1, m2c=6):
    """
    brief:    find forces on an unbalance atwood machine
    from:     WebAssign Homework 2.4
    category: atwood machine
    types:    tension, force
    """

    m1 = ['mass1', m1c, 'm1', 'kg', '.2f', 'scalar']
    m2 = ['mass2', m2c, 'm2', 'kg', '.2f', 'scalar']

    T = ['tension', 0, 'T', 'N', '.1f', 'scalar']
    a = ['acceleration', 0, 'a', 'm s⁻²', '.2f', 'scalar']
    g = ['gravity', 9.81, 'a', 'm s⁻²', '.2f', 'scalar']

    t = ['time', 0, 't', 's', '.2f', 'scalar']
    x = ['change in distance', 0, 'Δx', 'm', '.2f', 'scalar']
    v0 = ['initial velocity', 0, 'v₀', 'm s⁻¹', '.2f', 'vector']


    print('-' * 30)
    print('Two objects with masses of {:{}} {} and {:{}} {} are connected by a light string that passes over a frictionless pulley'.format(m1[1], m1[4], m1[3], m2[1], m2[4], m2[3]))
    print('(a) Determine the tension in the string. N')
    print('(b) Determine the acceleration of each object. m/s²')
    print('(c) Determine the distance each object will move in the first second of motion if both objects start from rest. m')

    print('░ question a ░')
    # solve tension
    print_atwood_machine(T, m1, m2, g, T)

    print('░ question b ░')
    # solve acceleration
    print_atwood_machine(a, m1, m2, g, a)

    print('░ question c ░')
    # time is 1 second
    t[1] = 1
    # initial velocity = 0
    v0[1] = 0
    # solve distance: Δx = v₀t + ½at
    print_mechanics_motion3(x, x, v0, t, a)

# webassign 3
def energy_and_force_of_bullet(mc=2.0, v0c=280, xc=43):
    """
    brief:    find the kinetic energy and force of a bullet given its speed
    from:     WebAssign Homework 3.1
    category: kinetic energy
    types:    energy, work
    """

    m = ['mass', mc, 'm', 'kg', '.2e', 'scalar']
    v = ['velocity', v0c, 'v', 'm s⁻¹', '.2f', 'scalar']
    x = ['distance', xc, 'x', 'm', '.3f', 'scalar']
    F = ['force', 0, 'F', 'N', '.2f', 'scalar']
    KE = ['kinetic energy', 0, 'KE', 'J', '.1f', 'scalar']  # KE: kinetic energy (KE = ½mv²)
    W = ['work', 0, 'W', 'J', '.2f', 'scalar']  # W: work (W = Fd)

    print('-' * 30)
    print('A {:{}} g bullet leaves the barrel of a gun at a speed of {:{}} {}.'.format(m[1], m[4], v[1], v[4], v[3]))
    print('(a) Find its kinetic energy. J')
    print('(b) Find the average force exerted by the expanding gases on the bullet as it moves the length of the {:{}} cm long barrel. N'.format(x[1], x[4]))

    print('░ question a ░')
    print('convert g to kg: x / 1000')
    print_maths_evaluate('/', m, m, 1000)
    # solve KEf
    print_kinectic_energy(KE, KE, m, v)

    print('░ question b ░')
    print('convert cm to m: x / 100')
    print_maths_evaluate('/', x, x, 100)
    # F = W/d
    print_maths_evaluate('/', F, KE, x)

def impact_of_ball_on_plate(mc=5.30, xhc=10.0, xdc=2.90):
    """
    brief:    find the force exerted on a plate from a dropped ball
    from:     WebAssign Homework 3.2
    category: kinetic energy
    types:    energy, work, kinematics
    """

    m = ['mass', mc, 'mc', 'kg', '.2f', 'scalar']
    xh = ['change in height', xhc, 'Δheight', 'm', '.2f', 'scalar']
    xd = ['change in depth', xdc, 'Δdepth', 'm', '.4f', 'scalar']
    g = ['gravity', 9.81, 'a', 'm s⁻²', '.2f', 'scalar']
    F = ['force', 0, 'F', 'N', '.2f', 'scalar']
    v = ['velocity', 0, 'v', 'm s⁻¹', '.2f', 'scalar']
    KE = ['kinetic energy', 0, 'KE', 'J', '.1f', 'scalar']

    print('-' * 30)
    print('A {:{}} {} steel ball is dropped onto a copper plate from a height of {:{}} {}.'.format(m[1], m[4], m[3], xh[1], xh[4], xh[3]))
    print('If the ball leaves a dent {:{}} mm deep in the plate'.format(xd[1], xd[4]))
    print('(a) what is the average force exerted by the plate on the ball during the impact? N')

    print('░ question a ░')
    # solve final velocity: v² = v₀² + 2aΔx
    print_mechanics_motion4(v, v, 0, g, xh)
    # change in kinetic energy: KE = ½mv²
    print_kinectic_energy(KE, KE, m, v)
    print('convert mm to m: x / 1000')
    print_maths_evaluate('/', xd, xd, 1000)
    # solve Force: F = W/d
    print_work_done(F, KE, F, xd)

def atwood_machine_passing(m1c=5.15, m2c=3.45, xhc=4):
    """
    brief:    find the speed and distance of uneven masses on an atwood machine
    from:     WebAssign Homework 3.3
    category: atwood machine
    types:    energy, kinematics
    """

    m1 = ['mass1', m1c, 'm1', 'kg', '.2f', 'scalar']
    m2 = ['mass2', m2c, 'm2', 'kg', '.2f', 'scalar']
    xh = ['height', xhc, 'h', 'm', '.3f', 'scalar']

    g = ['gravity', 9.81, 'a', 'm s⁻²', '.2f', 'scalar']
    v = ['velocity', 0, 'v', 'm s⁻¹', '.2f', 'scalar']
    x = ['change in distance', 0, 'Δx', 'm', '.2f', 'scalar']
    a = ['acceleration', 0, 'a', 'm s⁻²', '.2f', 'scalar']
    KE = ['kinetic energy', 0, 'KE', 'J', '.1f', 'scalar'] # KE: kinetic energy (KE = ½mv²)

    print('-' * 30)
    print('Two masses are connected by a light string passing over a light, frictionless pulley')
    print('The {} = {:{}} {} object is released from rest at a point {:{}} {} above the floor, where the {} = {:{}} {} object rests.'.format(m1[2], m1[1], m1[4], m1[3], xh[1], xh[4], xh[3], m2[2], m2[1], m2[4], m2[3]))
    print('(a) Determine the speed of each object when the two pass each other. m/s')
    print('(b) Determine the speed of each object at the moment the {:{}} {} mass hits the floor. m/s'.format(m1[1], m1[4], m1[3]))
    print('(c) How much higher does the {:{}} {} mass travel after the {:{}} {} mass hits the floor? m'.format(m2[1], m2[4], m2[3], m1[1], m1[4], m1[3]))

    print('░ question a ░')
    # solve acceleration
    print_atwood_machine(a, m1, m2, g, a)
    # change in distance is half height
    x[1] = xh[1] / 2
    # solve velocity: v² = v₀² + 2aΔx
    print_mechanics_motion4(v, v, 0, a, x)

    print('░ question b ░')
    # change in distance is complete height
    x[1] = xh[1]
    # solve velocity: v² = v₀² + 2aΔx
    print_mechanics_motion4(v, v, 0, a, x)

    print('░ question c ░')
    # change in kinetic energy: KE = ½mv²
    print_kinectic_energy(KE, KE, m2, v)
    # solve PE=KE = h=KE/mg
    print_potential_energy_gravity(xh, KE, m2, g, xh)

# webassign 4

def impulse_collision(Jc=8, mc=2.2, v0c=-1.7):
    """
    brief:    determine final velocity of an object given its impact force
    from:     WebAssign Homework 4.1
    category: impulse
    types:
    """

    J = ['impulse', Jc, 'J', 'N s⁻¹', '.2f', 'vector']
    m = ['mass', mc, 'mc', 'kg', '.2f', 'scalar']
    v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.2f', 'vector']
    v = ['velocity', 0, 'v', 'm s⁻¹', '.2f', 'scalar']


    print('-' * 30)
    print('A {:{}} {} object has impulse force of {:{}} {} upon collision.'.format(m[1], m[4], m[3], J[1], J[4], J[3]))
    print('(b) Find the final velocity of the mass if it is initially at rest. m/s')
    print('(c) Find the final velocity of the mass if it is initially moving along the x axis with a velocity of {:{}} {}. m/s'.format(v0[1], v0[4], v0[3]))

    print('░ question b ░')
    # solve velocity: Δv = J/m
    print_impulse(v, J, v, m)

    print('░ question c ░')
    # solve velocity given initial velocity: v = v0 + vf
    print_maths_evaluate('+', v, v0, v)

def ball_bounce_wall_angle(mc=2.90, vc=10.0, Oc=60, tc=0.16):
    """
    brief:    force on a ball bouncing off a wall at an angle
    from:     WebAssign Homework 4.2
    category: impulsive force
    types:    momentum conservation
    """

    m = ['mass', mc, 'mc', 'kg', '.2f', 'scalar']
    v = ['velocity', vc, 'v', 'm s⁻¹', '.2f', 'vector']
    O = ['angle', Oc, 'θ', '°', '.0f', 'scalar']
    t = ['time', tc, 't', 's', '.3f', 'scalar']
    pi = ['initial momentum', 0, 'pi', 'kg m/s', '.2f', 'vector']
    pf = ['final momentum', 0, 'pf', 'kg m/s', '.2f', 'vector']
    p = ['change in momentum', 0, 'Δp', 'kg m/s', '.2f', 'vector']
    xF = ['x component force', 0, 'xF', 'N', '.0f', 'vector']

    print('-' * 30)
    print('A {:{}} {} steel ball strikes a wall with a speed of {:{}} {} at an angle of {:{}}{} with the surface.'.format(m[1], m[4], m[3], v[1], v[4], v[3], O[1], O[4], O[3]))
    print('It bounces off with the same speed and angle.')
    print('If the ball is in contact with the wall for {:{}} {}, what is the average force exerted on the ball by the wall?'.format(t[1], t[4], t[3]))
    print('(a) x-component N')
    print('(a) y-component N')

    print('░ question a ░')
    # Fm=Δp/Δt
    # Δpx = (m * v2 * sin(θ)) - (-m * v1 * sin(θ)) ; the negative sign in the second term is because the orientation of the trajectory reverses
    # Δpy = (m * v2 * cos(θ)) - (m * v1 * cos(θ)) = 0
    # Use the sin and cos in this way, as the angle is measured from the hypotenuse and opposite side

    print('velocity: x direction travelling y angle: sin=opp/hyp : v * sin(θ)')
    print_maths_evaluate('*', v, v, math.sin(to_radians(O[1])))
    print('initial momentum: : p = m * v')
    print_maths_evaluate('*', pi, m, v)
    print('final momentum, velocity vector reversed direction: : p = m * -v')
    print_maths_evaluate('*', pf, m, v[1] * -1)
    print('change in momentum: Δp = pf - pi')
    print_maths_evaluate('-', p, pf, pi)
    print('force: F = Δp/Δt')
    print_maths_evaluate('/', xF, p, t)
    print('Since the ball has reversed direction, an impulse has occurred')

    print('░ question b ░')
    print('Δpy = (m * v2 * cos(θ)) - (m * v1 * cos(θ)) = 0')
    print('Fm = 0/Δt = 0')
    print('Since the ball is still travelling in this direction, no impulse has occurred')

def golf_ball_speed(m1c=280, m2c=46, v0c=47, vfc=34):
    """
    brief:    initial velocity of a golf ball given impact force of being hit by a golf club
    from:     WebAssign Homework 4.3
    category: impulse
    types:    impulsive force, Newton's second law, momentum
    """

    m1 = ['mass1', m1c, 'm1', 'kg', '.3f', 'scalar']
    m2 = ['mass2', m2c, 'm2', 'kg', '.3f', 'scalar']
    v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.2f', 'vector']
    vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.2f', 'vector']
    v = ['velocity', 0, 'v', 'm s⁻¹', '.0f', 'vector']
    p0 = ['initial momentum', 0, 'p₀', 'kg m/s', '.2f', 'vector']
    pf = ['final momentum', 0, 'pf', 'kg m/s', '.2f', 'vector']
    p = ['momentum', 0, 'Δp₀', 'kg m/s', '.2f', 'vector']

    print('-' * 30)
    print('High-speed stroboscopic photographs show that the head of a {:{}} {} golf club is traveling at {:{}} {}'.format(m1[1], m1[4], m1[3], v0[1], v0[4], v0[3]))
    print('just before it strikes a {:{}} {} golf ball at rest on a tee.'.format(m2[1], m2[4], m2[3]))
    print('After the collision, the club head travels (in the same direction) at {:{}} {}.'.format(vf[1], vf[4], vf[3]))
    print('(a) Find the speed of the golf ball just after impact. m/s')

    print('░ question a ░')
    print('convert g to kg: x / 1000')
    print_maths_evaluate('/', m1, m1, 1000)
    print_maths_evaluate('/', m2, m2, 1000)

    print('initial momentum: : p₀ = m1 * v₀')
    print_maths_evaluate('*', p0, m1, v0)
    print('final momentum: : pf = m1 * vf')
    print_maths_evaluate('*', pf, m1, vf)
    print('change in momentum: Δp = pf - p₀')
    print_maths_evaluate('-', p, pf, p0)

    print('░ question b ░')
    # solve velocity: Δv = J/m = Δp/t
    print_impulse(v, p, v, m2)
    print_convert_absolute(v)

def car_collision_angle(m1c=2200, v1c=10, m2c=3000, Oc=42, vfc=5.69):
    """
    brief:    Calculate velocity of cars in a collision
    from:     WebAssign Homework 4.4
    category: inelastic collision at right angles
    types:
    """

    m1 = ['mass1', m1c, 'm1', 'kg', '.0f', 'scalar']
    v1 = ['velocity object 1', v1c, 'v1', 'm s⁻¹', '.2f', 'vector']
    m2 = ['mass2', m2c, 'm2', 'kg', '.0f', 'scalar']
    O = ['angle', Oc, 'θ', '°', '.0f', 'scalar']
    vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.2f', 'vector']
    pE = ['momentum East', 0, 'pE', 'kg m/s', '.0f', 'vector']
    pN = ['momentum North', 0, 'pN', 'kg m/s', '.0f', 'vector']
    v2 = ['velocity object 2', 0, 'v2', 'm s⁻¹', '.2f', 'vector']

    print('-' * 30)
    print('A {:{}} {} car moving east at {:{}} {} collides with a {:{}} {} car moving north.'.format(m1[1], m1[4], m1[3], v1[1], v1[4], v1[3], m2[1], m2[4], m2[3]))
    print('The cars stick together and move as a unit after the collision, at an angle of {:{}}{} north of east and at a speed of {:{}} {}.'.format(O[1], O[4], O[3], vf[1], vf[4], vf[3]))
    print('(a) Find the speed of the {:{}} {} car before the collision. m/s north'.format(m2[1], m2[4], m2[3]))

    print('░ question a ░')
    print('momentum car east (ADJ): : pE = m1 * v1')
    print_maths_evaluate('*', pE, m1, v1)

    print('momentum north (OPP): : pN = pE * tan(θ)')
    print_maths_evaluate('*', pN, pE, math.tan(to_radians(O[1])))

    print('velocity car north (OPP): pN=m2*v2 <==> v2=pN/m2')
    print_maths_evaluate('/', v2, pN, m2)

# webassign 5
def race_car_circular_track():
    """
    brief:    Race car on a circular race track
    from:     WebAssign Homework 5.1
    category: circular motion
    types:    velocity, angular momentum, tangential acceleration, angular momentum
    """

    # quantities
    # related to dimensions of the circle
    r = [444, 'm']  # r: radius length - m

    # related to angular momentum in the center of the circle
    O = [0, 'rad']  # θ: angular displacement - rad     (θ = ωt)
    w = [0, 'rad s⁻¹']  # ω: angular velocity     - rad s⁻¹ (ω = v/r)
    a = [0, 'rad s⁻²']  # α: angular acceleration - rad s⁻² (α = ω/r)

    # related to the kinematics of the car travelling on the circumference of the circle
    # http://www.slideshare.net/caitlinforan/rotational-motion-7142158
    d = [0, 'm']  # d: distance travelled       - m     (d = rθ)
    v = [0, 'm s⁻¹']  # v: velocity                 - m s⁻¹ (v = rω)
    aT = [0.34, 'm s⁻²']  # aT: tangential acceleration - m s⁻² (aT = v²/r) OR (aT = rα)
    t = [0, 's']  # t: time                     - s

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
    print('d = {} {} * {:.2f} {}'.format(r[0], r[1], O[0], O[1]))
    d[0] = r[0] * O[0]
    print('d = {:.0f} {}'.format(d[0], d[1]))

    print('░ question c ░')
    print('angular position: θ₂ = θ₁ + ωt + ½αt²')
    print('since ω and θ is zero initially: θ = ½αt²')
    print('rearrange to solve time: t = √(2 * θ / α)')
    print('t = √(2 * {0:.2f} {1} / {2:.2e} {3})'.format(O[0], O[1], a[0], a[1]))
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
    M = [3.0, 'kg']  # M: mass of spool
    R = [0.6, 'm']  # r: radius length
    w = [0, 'rad s⁻¹']  # ω: angular velocity     - (ω = v/r)
    I = [0, 'kg m²']  # I: moment of inertia    - (I = MR²) * default model

    # related to the bucket
    mB = [3.0, 'kg']  # mB: mass of bucket
    d = [4.8, 'm']  # d: distance travelled
    g = [9.81, 'm s⁻²']  # g: gravity

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
    print('I = 0.5 * {:.2f} {} * {} {} ²'.format(M[0], M[1], R[0], R[1]))
    I[0] = 0.5 * M[0] * R[0]
    print('I = {:.2f} {}'.format(I[0], I[1]))

    print('You will end up deriving the angular speed of the spool to be this:')
    print('ω = √(2*mB*gd / (I + mB*r²))')
    print('ω = √(2 * {0} {1} * {2} {3} * {4} {5} / ({6:.2f} {7} + {0} {1} * {8} {9} ²))'.format(mB[0], mB[1], g[0], g[1], d[0], d[1], I[0], I[1], R[0], R[1]))
    w[0] = math.sqrt(2 * mB[0] * g[0] * d[0] / (I[0] + mB[0] * R[0] ** 2))
    print('ω = {:.2f} {}'.format(w[0], w[1]))

    print('where:')
    print('mB {} {}: is the mass of the bucket'.format(mB[0], mB[1]))
    print('r {} {}: is the radius of the spool'.format(R[0], R[1]))
    print('I {:.2f} {}: is the rotational inertia of the spool'.format(I[0], I[1]))
    print('g {} {}: is Earths gravitational field'.format(g[0], g[1]))
    print('d {} {}: is the distance of descent of the bucket from rest to final state.'.format(d[0], d[1]))

# webassign 6
def spring_potential_energy_velocity():
    """
    brief:    find velocity of an object attached to horizontal spring
    from:     WebAssign Homework 6.1
    category: hookes law
    types:    spring potential energy, conservation of energy, kinematics
    """

    # related to the spring
    # https://scripts.mit.edu/~srayyan/PERwiki/images/e/e5/Hookeslawb.png
    k = [10.0, 'N m⁻¹']  # k: spring constant
    E = [0, 'J']  # E: spring potential energy (E = ½kx²)
    E0 = [0, 'J']  # E0: spring potential energy at equilibrium position
    KE = [0, 'J']  # KE: kinetic energy (KE = ½mv²)

    # related to the mass
    m = [0.04, 'kg']  # m: mass
    x = [0.20, 'm']  # A|x: amplitude|displacement
    v = [0, 'm s⁻¹']  # v: velocity

    print('-' * 30)
    print("A {} {} object is attached to a horizontal spring with a force constant of {} {}".format(m[0], m[1], k[0], k[1]))
    print("It is released from rest with an amplitude of {} {}.".format(x[0], x[1]))
    print("(a) What is the velocity of the object when it is halfway to the equilibrium position if the surface is frictionless? m/s")

    print('░ question a ░')
    print('spring potential energy: E = ½kx²')
    print('E = 0.5 * {} {} * {} {} ²'.format(k[0], k[1], x[0], x[1]))
    E[0] = 0.5 * k[0] * x[0] ** 2
    print('E = {:.2f} {}'.format(E[0], E[1]))

    print('spring potential energy at ½ equilibrium position: E = ½k(x/2)²')
    print('E₀ = 0.5 * {:.2f} {} * ({} {} / 2)²'.format(k[0], k[1], x[0], x[1]))
    E0[0] = 0.5 * k[0] * (x[0] / 2) ** 2
    print('E₀ = {:.2f} {}'.format(E0[0], E0[1]))

    print('spring potential energy lost <==> kinetic energy : KE = E - E₀')
    print('KE = {:.2f} {} - {:.2f} {}'.format(E[0], E[1], E0[0], E0[1]))
    KE[0] = E[0] - E0[0]
    print('KE = {:.2f} {}'.format(KE[0], KE[1]))

    print('kinetic energy: KE = ½mv²')
    print('rearrange to solve velocity: v = √(KE / ½m)')
    print('v = √({:.2f} {} / (0.5 * {} {}))'.format(KE[0], KE[1], m[0], m[1]))
    v[0] = math.sqrt(KE[0] / (0.5 * m[0]))
    print('v = {:.2f} {}'.format(v[0], v[1]))

def vertical_spring_mass():
    """
    brief:    find period of motion (oscillation) of a vertical spring-mass
    from:     WebAssign Homework 6.2
    category: oscillations
    types:    simple harmonic motion
    """

    # related to the masses
    m = [0.006, 'kg']  # m: initial mass
    m2 = [0.028, 'kg']  # m2: mass that comes after
    g = [9.81, 'm s⁻²']  # g: gravity

    # related to the oscillation
    k = [0, 'N m⁻¹']  # k: spring constant
    x = [0.037, 'm']  # x|A: displacement|amplitude
    T = [0, 's']  # T: Time PERIOD of oscillation in seconds (T = 2π√(m/k))

    print('-' * 30)
    print("A spring stretches {} {} when a {} {} object is hung from it.".format(x[0], x[1], m[0], m[1]))
    print("The object is replaced with a block of mass {} {} that oscillates in simple harmonic motion".format(m2[0], m2[1]))
    print("(a) calculate the period of motion (s)")

    print('░ question a ░')
    print('spring constant: k = mg/x')
    print('k = {} {} * {} {} / {} {}'.format(m[0], m[1], g[0], g[1], x[0], x[1]))
    k[0] = m[0] * g[0] / x[0]
    print('k = {:.2f} {}'.format(k[0], k[1]))

    print('simple harmonic motion - time period: T = 2π√(m2 / k)')
    print('T = 2π√({} {} / {:.2f} {})'.format(m2[0], m2[1], k[0], k[1]))
    T[0] = 2 * math.pi * math.sqrt(m2[0] / k[0])
    print('T = {:.2f} {}'.format(T[0], T[1]))

def wave_period_speed(Ac=0.09, hlc=0.20, fc=17.0):
    """
    brief:    find period and speed of a wave
    from:     WebAssign Homework 6.3
    category: wave motion
    types:    wave oscillation
    """

    # related to the wave
    v = ['wave speed', 0, 'v', 'm s⁻¹', '.2f', 'scalar']  # v: speed of a wave (v = fλ OR v = λ/T)
    f = ['frequency', fc, 'f', 'Hz', '.1f', 'scalar']     # f: frequency (also m s⁻¹)
    hl = ['wavelength', hlc, 'λ', 'm', '.2f','vector']    # λ: wavelength

    A = ['amplitude', Ac, 'A', 'm', '.2f', 'scalar']      # A: amplitude
    T = ['period', 0, 'T', 's', '.3f', 'scalar']          # T: Time PERIOD of oscillation in seconds, must be at least 3 dp for webassign (T = 2π√(m/k))

    print('-' * 30)
    print("A wave travelling in the positive x-direction has a {} ({}) of {:{}} {}".format(f[0], f[2], f[1], f[4], f[3]))
    print("An {} ({}) of {:{}} {} and {} ({}) of {:{}} {}".format(A[0], A[2], A[1], A[4], A[3], hl[0], hl[2], hl[1], hl[4], hl[3]))
    print("Find the following")
    print("(c) the period s")
    print("(d) the speed of the wave m/s")

    print('░ question c ░')
    print('wave period: T = 1/f')
    print_maths_evaluate('/', T, 1, f)

    print('░ question d ░')
    print('speed of a wave: v = fλ')
    print_maths_evaluate('*', v, f, A)

# webassign 7
def electrons_hitting_tv(Ic=55.0):
    """
    brief:    Measure the amount of electrons in a current of a TV
    from:     WebAssign Homework 7.1
    category: charge
    types:
    """

    I = ['ampere', Ic, 'I', 'µA', '.1f', 'scalar'] # I: ampere (Amperes are used to express flow rate of electric charge 1A = 1C/s) The unit symbol is dynamic!
    Q = ['coulomb', '0', 'Q', 'C', '.2e', 'scalar'] # Q: coulomb (C = Amps/second C = A s⁻¹)
    t = ['time', 0, 't', 's', '.2f', 'scalar']
    Qe = ['electrons per coulomb', 0.00000000000000000016021766208, 'Qe', 'electrons', '.2e', 'scalar'] # Q: coulomb (C = Amps/second C = A s⁻¹)
    e = ['electrons', 0, 'e', 'electrons', '.2e', 'scalar']

    print('-' * 30)
    print('In a particular television picture tube, the measured beam current is {:{}} {}.'.format(I[1], I[4], I[3]))
    print('(a) How many electrons strike the screen every second?')
    
    print('░ question a ░')
    print_amps_and_coulomb_equivalent(Q, I, Q)
    # time is 1 second
    t[1] = 1
    # current times time Q = I*t
    print_maths_evaluate('*', Q, I, t)
    print('solve how many electrons are in charge Q')
    print_maths_evaluate('/', e, Q, Qe)

def current_light_bulb(Rc=300, Vc=160):
    """
    brief:    Find the current in a light bulb given resistance and voltage
    from:     WebAssign Homework 7.2
    category: charge
    types:    ohms law
    """

    R = ['ohms', Rc, 'R', 'Ω', '.0f', 'scalar'] # R: ohms
    V = ['voltage', Vc, 'V', 'V', '.0f', 'scalar'] # V: voltage
    I = ['ampere', 0, 'I', 'A', '.2f', 'scalar'] # I: ampere (Amperes are used to express flow rate of electric charge 1A = 1C/s) The unit symbol is dynamic!

    print('-' * 30)
    print('A light bulb has a resistance of {:{}} {} when operating at a voltage of {:{}} {}.'.format(R[1], R[4], R[3], V[1], V[4], V[3]))
    print('(a) What is the current in the bulb?. mA')

    print('░ question a ░')
    print_ohms_law(I, V, I, R)
    print('convert A to mA * 1000')
    I[1] = I[1] * 1000
    I[3] = 'mA'
    print('{} = {:{}} {}'.format(I[2], I[1], I[4], I[3]))

"""
A length of metal wire has a radius of 5.10  10-3 m and a resistance of 0.100 .
When the potential difference across the wire is 15.0 V, the electron drift speed is found to be 3.17 ✕ 10-4 m/s. On the basis of these data, calculate the density of free electrons in the wire.


print_area_of_circle(A, r)


A 6.0  resistor, an 7.0  resistor, and a 15  resistor are connected in series with a 30 V battery.
"""


        





def water_bottle_experiment(rc=4.6, Vc=1500):
    """
    water bottle experiment
    take a bottle size, eg 1.5L and radius eg 3cm
    take a series of x targets want to hi, eg 5cm, 12cm, 18cm, 25cm

    1) equation 1
    take 2 hole sizes, 2mm and 3mm and calculate where to position the holes to hit the targets

    2) equation 2
    using a base of 10cm, calculate the area of a hole and velocity required to hit furthest target
    then take this hole size and use it to calculate the heights of lower targets

    A =

    u = 2gh
    u = Q/A

    """

    g = ['gravity', 9.81, 'a', 'm s⁻²', '.2f', 'scalar']

    rB = ['radius Bottle', rc, 'r', 'cm', '.3f', 'scalar']
    VB = ['volume Bottle', Vc, 'V', 'mL³', '.2f', 'scalar']
    bB = ['base Bottle', 0, 'h', 'cm²', '.2f', 'scalar']
    hB = ['height Bottle', 0, 'h', 'cm', '.6f', 'scalar']



    # calculate the height of the bottle given the volume and radius
    # V = Bh
    # B = πr²
    # V = πr²h
    # h = V/πr²

    # B = πr²
    bB[1] = math.pi * rB[1]**2
    print('base of bottle: {:{}} {}'.format(bB[1], bB[4], bB[3]))
    # h = V/πr²
    print_maths_evaluate('/', hB, VB, bB)

    # display how many millilitres (cm³) are in 1cm height of bottle
    Vcm = ['volume per cm/h', 0, 'Vcm', 'mL³', '.6f', 'scalar']
    print_maths_evaluate('/', Vcm, VB, hB)

    # calculate 25 x horizontal using 2mm
    # A = πr2
    # targets = [25, 18, 12, 5]
    # holeradius = [2, 3]

    rH = ['radius Hole', 0.2, 'r', 'cm', '.3f', 'scalar'] # 2 mm
    aH = ['radius Area', 0, 'r', 'cm²', '.3f', 'scalar']
    x1 = ['x1 horizontal distance', 25, 'x1', 'cm', '.2f', 'scalar']

    # A = πr²
    aH[1] = math.pi * rH[1]**2
    # print('convert mm to cm: x / 10')
    # print_maths_evaluate('/', aH, aH, 10)
    print('area of hole: {:{}} {}'.format(aH[1], aH[4], aH[3]))

    # print('convert mL to L: x / 1000')
    # print_maths_evaluate('/', V, V, 1000)


    # v = Q/As : flow rate = flow rate / surface area

    # volumetric flowrate
    # volume = area * length
    # volume flow = area * velocity

    # v = √(2gh)
    # Q = A * V

    # solve velocity full bottle: v² = v₀² + 2aΔx
    v = ['velocity', 0, 'v', 'cm s⁻¹', '.2f', 'vector']
    # print('convert cm to m: x / 100')
    # print_maths_evaluate('/', hB, hB, 100)
    print_mechanics_motion4(v, v, 0, g, hB)

    # # solve velocity 1cm: v² = v₀² + 2aΔx
    # hB[1]=1
    # print_mechanics_motion4(v, v, 0, g, hB)

    # Q = Av
    Q = ['flow rate', 0, 'Q', 'cm³ s⁻¹', '.2f', 'vector']
    print_maths_evaluate('*', Q, aH, v)


main()





"""
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


theta = theta0 + wt + .5angular acceleration * t^2
theta = .5at^2, since angular speed is zero initially and angular displacement is zero.
root(2theta/a) = t
t = root(2*.5/9.94x10^-4) = 31.7 s
"""
