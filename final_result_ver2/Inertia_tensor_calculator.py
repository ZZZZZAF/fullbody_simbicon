w = 0.032975  # x
d = 0.032975  # y
h = 0.1319  # z

mass = 0.45

import numpy as np

I = np.array([[(1/12) * mass * (h ** 2 + d ** 2), 0, 0],
              [0, (1/12) * mass * (w ** 2 + h ** 2), 0],
              [0, 0, (1/12) * mass * (w ** 2 + d ** 2)]])

print(I)