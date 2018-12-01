from ctypes import c_double, c_float, c_int, c_bool, c_int64

import numpy as np

types_map = {'float': c_float,
             'double': c_double,
             'int': c_int,
             'bool': c_bool,
             'int64': c_int64}


def get_type_from_array(arr: np.ndarray):
    dtype = str(arr.dtype)
    if dtype not in types_map:
        raise ValueError('{} is not a registered type.'.format(dtype))
    return types_map[dtype]
