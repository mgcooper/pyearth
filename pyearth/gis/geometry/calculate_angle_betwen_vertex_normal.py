

import numpy as np
from pyearth.gis.location.convert_longitude_latitude_to_sphere_3d import convert_longitude_latitude_to_sphere_3d

def calculate_angle_betwen_vertex_normal(dLongitude1_in, dLatitude1_in, 
                                dLongitude2_in, dLatitude2_in, 
                                dLongitude3_in, dLatitude3_in, 
                                iFlag_radian = None):
    if iFlag_radian is None:
        dLongitude1_radian_in, dLatitude1_radian_in = np.radians(np.array((dLongitude1_in, dLatitude1_in) ))
        dLongitude2_radian_in, dLatitude2_radian_in = np.radians(np.array((dLongitude2_in, dLatitude2_in) )) #this is the middle one
        dLongitude3_radian_in, dLatitude3_radian_in = np.radians(np.array((dLongitude3_in, dLatitude3_in) ))
        pass
    else:         
        dLongitude1_radian_in, dLatitude1_radian_in = dLongitude1_in , dLatitude1_in  
        dLongitude2_radian_in, dLatitude2_radian_in = dLongitude2_in , dLatitude2_in #this is the middle one
        dLongitude3_radian_in, dLatitude3_radian_in = dLongitude3_in , dLatitude3_in
        pass
    # The points in 3D space
    a3 = convert_longitude_latitude_to_sphere_3d(dLongitude1_radian_in, dLatitude1_radian_in)
    b3 = convert_longitude_latitude_to_sphere_3d(dLongitude2_radian_in, dLatitude2_radian_in)
    c3 = convert_longitude_latitude_to_sphere_3d(dLongitude3_radian_in, dLatitude3_radian_in)
    a3vec = a3 - b3
    c3vec = c3 - b3 
    dot = np.dot(a3vec, c3vec)
    g = np.cross(a3vec, c3vec)
    det = np.dot(b3, g)
    angle = np.arctan2(det, dot)
    f = np.degrees(angle) 
    if f < 0:
        f = 360 + f
    
    return f