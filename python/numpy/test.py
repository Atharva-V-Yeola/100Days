import numpy as np
import time

a = list(range(1000000))
b = list(range(1000000))

start = time.time()
c = [x + y for x, y in zip(a, b)]
end = time.time()
print("List Time:", end - start)

a_np = np.array(a)
b_np = np.array(b)

start = time.time()
c_np = a_np + b_np
end = time.time()
print("NumPy Time:", end - start)
