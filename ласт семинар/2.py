import unittest
import numpy as np
def mnk(y_t, y_p):
    return np.mean((y_t - y_p) ** 2)

###

class testMNK(unittest.TestCase):
    def test_mnk(self):
        y_t = np.array([1, 2, 3, 4, 5])
        y_p = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
        t_mnk = mnk(y_t, y_p)
        self.assertAlmostEqual(t_mnk, 0.25, places=5)
if __name__ == "__main__":
    unittest.main()