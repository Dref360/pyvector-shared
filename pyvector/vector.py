import multiprocessing as mp
from multiprocessing.sharedctypes import Array

import numpy as np

from pyvector.utils import get_type_from_array


class Vector:
    def __init__(self, data: np.ndarray):
        """
        Shareable Vector-like structure.
        Args:
            data: Initial data hold by the vector.
        """
        self.length = data.size
        self._capacity = data.size
        self._ntype = data.dtype
        self.type = get_type_from_array(data)
        self.array = Array(self.type, data, lock=False)
        self.lock = mp.Lock()

    def assign(self, data: np.ndarray):
        """
        Modify the structure to hold `data` instead.
        Args:
            data: Numpy array with the same dtype.

        Returns:

        """
        if self.type is not get_type_from_array(data):
            raise ValueError('We do not support dynamic typing')
        with self.lock:
            if data.size > self._capacity:
                self.array = Array(self.type, data, lock=False)
                self._capacity = data.size
            else:
                self.array[:data.size] = data
            self.length = data.size

    def get(self):
        """
        Get the vector as a numpy array.
        Returns:
            A numpy array.
        """
        with self.lock:
            arr = np.frombuffer(self.array, self._ntype, count=self.length)
        return arr
