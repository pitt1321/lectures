#
# Physics 1321 Week 6
# University of Pittsburgh
#

import numpy as np


N = 100

xs = np.linspace(0, 10, N)
ys = 7.0*xs - 31.0
ys += np.random.normal(0.0, 1.0, N)

np.savetxt('linear.csv', np.column_stack([xs, ys]),
           delimiter=',', fmt='%g')


xs = np.linspace(0, 10, N)
ys = 2.0*xs**2 - 9.0*xs + 35.0
ys += np.random.normal(0.0, 5.0, N)

np.savetxt('nonlinear.csv', np.column_stack([xs, ys]),
           delimiter=',', fmt='%g')
