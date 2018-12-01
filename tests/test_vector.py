import multiprocessing as mp
import time

import numpy as np
from pyvector import Vector


def test_arange_single_process():
    x = np.arange(10, dtype=np.int)
    vec = Vector(x)
    np.testing.assert_allclose(x, vec.get())

    y = np.arange(8, dtype=np.int)
    vec.assign(y)
    np.testing.assert_allclose(y, vec.get())

    z = np.arange(15, dtype=np.int)
    vec.assign(z)
    np.testing.assert_allclose(z, vec.get())


def test_arange_two_processes():
    def runnable(vec: Vector, event: mp.Event, value: int):
        while not event.is_set():
            pass
        vec.assign(np.ones([10], dtype=vec._ntype) * value)

    x = np.arange(10, dtype=np.int)
    vec = Vector(x)

    e1 = mp.Event()
    pc = mp.Process(target=runnable, args=(vec, e1, 5))
    pc.start()
    time.sleep(1)

    np.testing.assert_allclose(x, vec.get())
    e1.set()
    time.sleep(1)
    np.testing.assert_almost_equal(np.ones([10], dtype=vec._ntype) * 5, vec.get())
