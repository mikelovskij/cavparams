import numpy as np


def cavity_parameter_estimator(l, rc1, rc2, lam=1064 * 10 ** (-9)):
    """
    Uses the parameters of a FP cavity (and of the laser) to estimate the
    parameters of its matched gaussian beam, using Perreca's formulas.

    Args:
        l: length of the cavity
        rc1: curvature radius of first mirror
        rc2: curvature radius of second mirror
        lam: laser wavelength

    Returns:
        g1, g2 are the cavity stability parameters
        z1, z2 the positions of the two mirrors with respect of the matched
        gaussian beam waist
        w0 is the waist size of the gaussian beam
    """
    g1 = 1 - l / rc1
    g2 = 1 - l / rc2

    z1 = -(l * g2 * (1 - g1)) / (g1 + g2 - 2 * g1 * g2)
    z2 = (l * g1 * (1 - g2)) / (g1 + g2 - 2 * g1 * g2)
    if z2 != (z1 + l):
        raise ValueError(
            "Math is wrong, I knew it! \n l = {}, z1 = {}, z2 = {}".format(l,
                                                                           z1,
                                                                           z2))
    else:
        print("Math is right once again, boring.")

    w0 = np.sqrt(lam * l / np.pi * np.sqrt(
        (g1 * g2 * (1 - g1 * g2)) / (g1 + g2 - 2 * g1 * g2) ** 2))
    return g1, g2, z1, z2, w0


def cavity_parameter_estimator_2(l, rc1, rc2, lam=1064 * 10 ** (-9)):
    """
    Uses the parameters of a FP cavity (and of the laser) to estimate the
    parameters of its matched gaussian beam.

    Args:
        l: length of the cavity
        rc1: curvature radius of first mirror
        rc2: curvature radius of second mirror
        lam: laser wavelength

    Returns:
        g1, g2 are the cavity stability parameters
        z1, z2 the positions of the two mirrors with respect of the matched
        gaussian beam waist
        w0 is the waist size of the gaussian beam
    """
    g1 = 1 - l / rc1
    g2 = 1 - l / rc2

    z1 = -l * (rc2 + l) / (rc2 + rc1 + 2 * l)
    z2 = z1 + l
    if z2 != (z1 + l):
        raise ValueError(
            "Math is wrong, I knew it! \n l = {}, z1 = {}, z2 = {}".format(l,
                                                                           z1,
                                                                           z2))
    else:
        print("Math is right once again, boring.")
    z0 = np.sqrt(- l * (rc1 + l) * (rc2 + l) * (rc1 + rc2 + l) / (rc2 + rc1 + 2 * l)**2)
    w0 = np.sqrt(lam * z0 / np.pi)
    return g1, g2, z1, z2, w0


def cavity_parameter_estimator_3(l, rc1, rc2, lam=1064 * 10 ** (-9)):
    """
    Uses the parameters of a FP cavity (and of the laser) to estimate the
    parameters of its matched gaussian beam. metodo mathematicho

    Args:
        l: length of the cavity
        rc1: curvature radius of first mirror
        rc2: curvature radius of second mirror
        lam: laser wavelength

    Returns:
        g1, g2 are the cavity stability parameters
        z1, z2 the positions of the two mirrors with respect of the matched
        gaussian beam waist
        w0 is the waist size of the gaussian beam
    """
    g1 = 1 - l / rc1
    g2 = 1 - l / rc2

    z1 = -l * (rc2 - l) / (rc2 + rc1 - 2 * l)
    z2 = z1 + l
    if z2 != (z1 + l):
        raise ValueError(
            "Math is wrong, I knew it! \n l = {}, z1 = {}, z2 = {}".format(l,
                                                                           z1,
                                                                           z2))
    else:
        print("Math is right once again, boring.")
    z0 = np.sqrt(l * (rc1 - l) * (rc2 - l) * (rc1 + rc2 - l) / (rc2 + rc1 - 2 * l)**2)
    w0 = np.sqrt(lam * z0 / np.pi)
    return g1, g2, z1, z2, w0
