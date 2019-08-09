"""
Module handling infiltration calculation.
References:
Beven (1984)
Morel-Seytoux and Khanji (1974)
"""

import math

class expinf:
    """
    Initialize and store static variables
    """
    const = 0
    ponding = 0
    cumf = 0
    cumf2 = 0
    tp = 0
    maxiter = 50


def green_ampt(t, R, CD, xk0, scaling_factor, dt, expinf):
    """
    t: Time increment (input)
    R: Precp in m/h (input)
    xk0: saturated_hydraulic_con/24/1000 (m/hr) (input).
    CD: Capillary drive, from Beven via Morel-Seytoux (input)
    scaling_factor: scaling_parameter in m (scaling_parameter/1000) (input)
    dt: Calculation time step in relation to reporting timestep, in this case hr/day (input)
    expinf: object storing the values of static variables (input)
    f1: Infiltration at the beginning of the time step (m)
    f2: Infiltration at the end of the timestep (m)
    r2: Infiltration rate (m/dt)
    tp: Estimated time to ponding
    cumf = Cumulative infiltration at the start of a time step (m)
    cumf2 = Cumulative infiltration at the end of a time step, aka big F (m)
    f = df in Beven.  Little f in the papers. (m)
    """

    def calc_cnst(cumf2, CD, szf):
        """
        Private function to calculate C
        """

        fact = 1
        const = 0
        fc = cumf2 + CD
        for i in range(1, 11):
            fact = fact * i
            add = (fc * szf) ** i / (i * fact)
            const = const + add
        const = math.log(fc) - (math.log(fc) + const) / math.exp(CD / szf)
        return const
    f1 = 0
    if expinf.ponding == 0:
        if expinf.cumf > 0:
            f1 = expinf.cumf
            r2 = -xk0 / scaling_factor * (CD + f1) / (1 - math.exp(f1 / scaling_factor))
            if R > r2:
                # Ponding starts
                expinf.cumf2 = expinf.cumf
                expinf.tp = t - dt
                expinf.ponding = 1
                expinf.const = calc_cnst(expinf.cumf2, CD, scaling_factor)

        f2 = expinf.cumf + R * dt
        r2 = -xk0 / scaling_factor * (CD + f2) / (1 - math.exp(f2 / scaling_factor))

        if f2 == 0 or R < r2:
            # No ponding, everything infiltrates
            f = R
            expinf.cumf = expinf.cumf + f * dt
            expinf.ponding = 0
            return f

        # set up the estimated time to ponding
        expinf.cumf2 = expinf.cumf + r2 * dt
        for i in range(1, expinf.maxiter):
            r2 = -xk0 / scaling_factor * (CD + expinf.cumf2) / (1 - math.exp(expinf.cumf2 / scaling_factor))
            if r2 > R:
                f1 = expinf.cumf2
                expinf.cumf2 = (expinf.cumf2 + f2) / 2
                diff = expinf.cumf2 - f1
            else:
                f2 = expinf.cumf2
                expinf.cumf2 = (expinf.cumf2 + f1) / 2
                diff = expinf.cumf2 - f2
        expinf.tp = t - dt + (expinf.cumf2 - expinf.cumf) / R
        if expinf.tp > t:
            f = R
            expinf.cumf = expinf.cumf + f * dt
            expinf.ponding = 0
            return f

    if expinf.const == 0:
        # At this point ponding is occurring, therefore C needs to exist and ponding flag is triggered.
        expinf.const = calc_cnst(expinf.cumf2, CD, scaling_factor)
        expinf.cumf2 = expinf.cumf2 + R * (t - expinf.tp) / 2
        expinf.ponding = 1

    # Ponding infiltration via Newton-Raphson.
    for i in range(1, expinf.maxiter):
        fc = expinf.cumf2 + CD
        sum1 = 0
        fact = 1
        for j in range(1, 11):
            fact = fact * j
            add = (scaling_factor / fc) ** j / (j * fact)
            sum1 = sum1 + add
        f1 = -(math.log(fc) - (math.log(fc) + sum1) / math.exp(CD / scaling_factor) - expinf.const
               ) / (xk0 / scaling_factor) - (t - expinf.tp)
        f2 = (math.exp(expinf.cumf2 / scaling_factor) - 1) / (fc * xk0 / scaling_factor)
        diff = - f1 / f2
        expinf.cumf2 = expinf.cumf2 + diff

    if expinf.cumf2 - expinf.cumf < R * dt:
        f = (expinf.cumf2 - expinf.cumf) / dt
        expinf.cumf = expinf.cumf2
        expinf.cumf2 = expinf.cumf2 + f * dt
        return f
    else:
        f = R
        expinf.cumf = expinf.cumf + f * dt
        expinf.ponding = 0
        return f

def static_reset(expinf, infil_array, i):

    """Resets variables in there is in precipitation
    expinf: Class containing static variables
    infil_array: Daily infiltration array
    i: time step index
    """

    expinf.cumf = 0
    expinf.cumf2 = 0
    expinf.ponding = 0
    expinf.tp = 0
    expinf.const = 0
    infil_array[i] = 0
