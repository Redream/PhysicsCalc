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
    "F = ['force', Fc, 'F', 'N', '.2f', 'scalar'] | " \
    "g = ['gravity', 9.81, 'a', 'm s⁻²', '.2f', 'scalar'] | " \
    "hl = ['wavelength', hlc, 'λ', 'm', '.2f', 'vector'] | " \
    "KE = ['kinetic energy', KEc, 'KE', 'J', '.1f', 'scalar'] # KE: kinetic energy (KE = ½mv²) | " \
    "m = ['mass', mc, 'mc', 'kg', '.2f', 'scalar'] | " \
    "m1 = ['mass1', m1c, 'm1', 'kg', '.2f', 'scalar'] | " \
    "m2 = ['mass2', m2c, 'm2', 'kg', '.2f', 'scalar'] | " \
    "t = ['time', tc, 't', 's', '.2f', 'scalar'] | " \
    "T = ['tension force', Tc, 'T', 'N', '.1f', 'scalar'] # T: tension | " \
    "T = ['period', Tc, 'T', 's', '.3f', 'scalar'] | "
    "v = ['wave speed', vc, 'v', 'm s⁻¹', '.2f', 'scalar'] | " \
    "v = ['velocity', vc, 'v', 'm s⁻¹', '.2f', 'scalar'] | " \
    "v0 = ['initial velocity', v0c, 'v₀', 'm s⁻¹', '.2f', 'vector'] | " \
    "vf = ['final velocity', vfc, 'vf', 'm s⁻¹', '.2f', 'vector'] | " \
    "W = ['work', Wc, 'W','J', '.2f', 'scalar']  # W: work (W = Fd) | " \
    "x = ['change in distance', xc, 'Δx', 'm', '.2f', 'scalar'] | " \
    "x = ['distance', xc, 'x', 'm', '.2f', 'scalar'] | "

    variables = (longstring.split('|'))

    for i in required:
        for j in variables:
            k = j.split('=')
            k[0] = k[0].strip()
            if i == k[0]:
                k[1] = k[1].strip()
                print('{} = {}'.format(k[0], k[1]))

#get_resources('m1', 'm2', 'T', 'a', 'g', 't', 'x', 'v0')
get_resources('m','v','KE','x','F', 'T', 'f')
