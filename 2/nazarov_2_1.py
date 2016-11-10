import numpy as np

def func_1(x):
    if x > 0:
        return x
    else:
        return 0.01 * x

func_1_vec = np.vectorize(func_1)
print func_1_vec(np.linspace(-4, 4, 10))

def func_2(x, sgm=1):
    # Y ~ N(0, sgm) --  Gaussian distribution
    y = np.random.normal(0, sgm)
    return max(0., x + y)

func_2_vec = np.vectorize(func_2)
print func_2_vec(np.linspace(-1, 1, 10), 1.41)