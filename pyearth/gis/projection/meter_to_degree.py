import numpy as np
def meter_to_degree(dResolution_meter, dLatitude_mean):
    """[summary]

    Args:
        dResolution_meter ([type]): [description]
        dLatitude_mean ([type]): [description]

    Returns:
        [type]: [description]
    """
    dLatitude_mean = abs(dLatitude_mean)

    dRadius = 6378137.0
    dRadius2 = dRadius * np.cos( dLatitude_mean / 180.0 * np.pi)

    ##dResolution_meter = dResolution_degree / 360.0 * 2*np.pi * dRadius2

    dResolution_degree= dResolution_meter/(2*np.pi * dRadius2) * 360.0

    return dResolution_degree