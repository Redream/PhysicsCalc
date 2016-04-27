
def get_resources(*required):
    """
    This is to help building functions in the main calculator faster
    returns lists of resources needed, in the order requested
    """
    print('-'*30)
    longstring = \
    "a = ['acceleration', ac, 'a', 'm s⁻²', '.2f', 'scalar'] | " \
    "A = ['amplitude', Ac, 'Ac', 'm', '.2f', 'scalar'] # A: amplitude | " \
    "Em = ['combined mass', Emc, '∑m', 'kg', '.2f', 'scalar'] | " \
    "f = ['frequency', fc, 'f', 'Hz', '.1f', 'scalar'] f: frequency (also m s⁻¹) | " \
    "F = ['force', Fc, 'F', 'N', '.2f', 'vector'] | " \
    "g = ['gravity', 9.81, 'a', 'm s⁻²', '.2f', 'scalar'] | " \
    "hl = ['wavelength', hlc, 'λ', 'm', '.2f', 'vector'] | " \
    "J = ['impulse', Jc, 'J', 'N s⁻¹', '.2f', 'vector'] | " \
    "KE = ['kinetic energy', KEc, 'KE', 'J', '.1f', 'scalar'] # KE: kinetic energy (KE = ½mv²) | " \
    "m = ['mass', mc, 'mc', 'kg', '.2f', 'scalar'] | " \
    "m1 = ['mass1', m1c, 'm1', 'kg', '.2f', 'scalar'] | " \
    "m2 = ['mass2', m2c, 'm2', 'kg', '.2f', 'scalar'] | " \
    "O = ['angle', Oc, 'θ', '°', '.0f', 'scalar'] | " \
    "p = ['momentum', pc, 'p', 'kg m/s', '.2f', 'vector'] | " \
    "t = ['time', tc, 't', 's', '.2f', 'scalar'] | " \
    "T = ['tension force', Tc, 'T', 'N', '.1f', 'scalar'] # T: tension | " \
    "T = ['period', Tc, 'T', 's', '.3f', 'scalar'] | " \
    "v = ['wave speed', vc, 'v', 'm s⁻¹', '.2f', 'scalar'] | " \
    "v = ['velocity', vc, 'v', 'm s⁻¹', '.2f', 'vector'] | " \
    "v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.2f', 'vector'] | " \
    "vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.2f', 'vector'] | " \
    "W = ['work', Wc, 'W','J', '.2f', 'scalar']  # W: work (W = Fd) | " \
    "x = ['change in distance', xc, 'Δx', 'm', '.2f', 'scalar'] | " \
    "x = ['distance', xc, 'x', 'm', '.2f', 'scalar'] | " \
    "xF = ['x component force', 0, 'x', 'N', '.2f', 'vector'] | " \
    "yF = ['y component force', 0, 'y', 'N', '.2f', 'vector'] | "

    # build a list with variables to use
    function_string = 'def newfunction('
    input_list = []
    question_list = []

    variables = (longstring.split('|'))
    for i in required:
        for j in variables:
            k = j.split('=')
            k[0] = k[0].strip()
            if i == k[0]:
                question_list.append(i)
                l = k[1].split(',')
                text= l[0]
                SIunit = l[3]
                input_list.append(k[0] + ' = input("' + text[3:-1] + ' (' + SIunit[2:-1] + '): ")')
                variable = l[1]
                function_string += variable[1:] + '=0, '

    # build choice menu
    print('if question == 3:')
    for i in input_list:
        print('    {}'.format(i))
    # build if not choice
    if_string = '    if not ('
    if_string += ' and '.join(question_list)
    if_string += '): newfunction()'
    # build else choice
    else_string = '    else: newfunction('
    for i in range(0, len(question_list)):
        question_list[i] = question_list[i] + 'c=float(' + question_list[i] + '), '
    else_string += ''.join(question_list)
    else_string = else_string[0:-2] + ')'

    # print choices
    print(if_string)
    print(else_string)
    print('')

    function_string = function_string[0:-2] + '):'
    print(function_string)
    print('    """')
    print("    brief:")
    print("    from:     WebAssign Homework ")
    print("    category:")
    print("    types:")
    print('    """')
    print('')

    variables = (longstring.split('|'))
    for i in required:
        for j in variables:
            k = j.split('=')
            k[0] = k[0].strip()
            if i == k[0]:
                k[1] = k[1].strip()
                print('    {} = {}'.format(k[0], k[1]))

    print("")
    print("    print('-' * 30)")
    print("    print('A {:{}} {} thing of {:{}} {}.'.format(m[1], m[4], m[3], v[1], v[4], v[3]))")
    print("    print('A {:{}} {} object with speed {:{}} {} hits at {:{}} {}.'.format(m[1], m[4], m[3], v[1], v[4], v[3], v0[1], v0[4], v0[3]))")
    print("    print('Before {:{}} {}.'.format(t[1], t[4], t[3]))")
    print("    print('(a) Find its kinetic energy. J')")
    print("    print('░ question a ░')")
    print("    print('░ question b ░')")

get_resources('m1', 'm2', 'T', 'a', 'g', 't', 'x', 'v0')
get_resources('m','v','KE','x','F', 'T', 'f')
get_resources('m', 'x', 'g', 'F', 'v')
get_resources('m1', 'm2', 'g', 'v0', 'v', 'x', 'a')
get_resources('J', 'm', 'v', 'v0')
get_resources('m','v','O','p','t','F','xF','yF')

get_resources('m1', 'm2', 'v0', 'vf', 'v', 'p')