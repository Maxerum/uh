import math

import random
import numpy as np
import pylab
from functools import reduce

# from lehmer import lehmer

def lehmer(n):
    return list(map(lambda x: random.random(), range(0, n)))



# Равномерное распределение
def uniform(a, b, n):
    numbers = lehmer(n)
    array = []
    for num in numbers:
        array.append(a + (b - a) * num)
    return array

# Гауссовское распределение
def normal(mean, std, n=6):
    return list(map(lambda x: mean + std * math.sqrt(12 / n) * (sum(lehmer(n)) - n / 2), range(0, 1000000)))



# Экспоненциальное распределение
def exponential(scale, size):
    numbers = lehmer(size)
    array = []
    for num in numbers:
        array.append(((-1) / scale) * (math.log(1 - num)))
    return array


# Гамма-распределение
def gamma(nu, l, n):
    return list(map(lambda x: -1 / l * math.log(reduce(lambda y, z: y * z, lehmer(nu))),
                    range(0, 1000000)))



# Треугольое распределение
def triangular(a, b, size):
    numbers = lehmer(size)
    array = []
    for i in np.arange(0, len(numbers) - 1):
        array.append(a + (b - a) * min(numbers[i], numbers[i + 1]))
        i += 2
    return array



# Распределение Симпсона
def simpson(left, right, size):
    numbers = lehmer(size * 2)
    a = left / 2
    b = right / 2
    x = []
    i = 0
    while i < len(numbers):
        y = a + (b - a) * numbers[i]
        z = a + (b - a) * numbers[i + 1]
        x.append(y + z)
        i += 2
    return x


size = 1000000

def main():
    low = -2.7
    high = 3.55
    uniformd = uniform(low, high, size)
    uniform_m = np.mean(uniformd)
    uniform_v = np.var(uniformd)
    uniform_s = np.std(uniformd)
    weights = np.ones_like(uniformd) / float(len(uniformd))

    pylab.hist(uniformd, bins=np.linspace(min(uniformd), max(uniformd), 21),
               weights=weights, histtype='bar', color='blue', rwidth=0.9)
    pylab.title("Равномерное распределение")
    print("Равномерное распределение:")
    print("Мат. ожидание: ", uniform_m)
    print("Дисперсия: ", uniform_v)
    print("СКО: ", uniform_s)
    pylab.show()

    mean = -14.56
    std = 1.258
    n = 10
    normald = normal(mean, std, n)
    normal_m = np.mean(normald)
    normal_v = np.var(normald)
    normal_s = np.std(normald)
    weights = np.ones_like(normald) / float(len(normald))
    pylab.hist(normald, bins=np.linspace(min(normald), max(normald), 21),
             weights=weights, histtype='bar', color='blue', rwidth=0.9)
    pylab.title("Гауссовское распределение")
    print("Гауссовское распределение:")
    print("Мат. ожидание: ", normal_m)
    print("Дисперсия: ", normal_v)
    print("СКО: ", normal_s)
    pylab.show()

    scale = 5.687;
    exp = exponential(scale, size)
    exp_m = np.mean(exp)
    exp_v = np.var(exp)
    exp_s = np.std(exp)
    weights = np.ones_like(exp) / float(len(exp))
    pylab.hist(exp, bins=np.linspace(min(exp), max(exp), 21),
               weights=weights, histtype='bar', color='blue', rwidth=0.9)
    pylab.title("Экспоненциальное распределение:")
    print("Экспоненциальное распределение:")
    print("Мат. ожидание: ", exp_m)
    print("Дисперсия: ", exp_v)
    print("СКО: ", exp_s)
    pylab.show()

    shape = 10
    l = 5
    gammad = gamma(shape, l, size)
    gamma_m = np.mean(gammad)
    gamma_v = np.var(gammad)
    gamma_s = np.std(gammad)
    weights = np.ones_like(gammad) / float(len(gammad))
    pylab.hist(gammad, bins=np.linspace(min(gammad), max(gammad), 21),
               weights=weights, histtype='bar', color='blue', rwidth=0.9)
    pylab.title("Гамма-распределение")
    print("Гамма-распределение:")
    print("Мат. ожидание: ", gamma_m)
    print("Дисперсия: ", gamma_v)
    print("СКО: ", gamma_s)
    pylab.show()

    left = -4
    right = 27
    tle = triangular(left, right, size)
    tle_m = np.mean(tle)
    tle_v = np.var(tle)
    tle_s = np.std(tle)
    weights = np.ones_like(tle) / float(len(tle))
    pylab.hist(tle, bins=np.linspace(min(tle), max(tle), 21),
               weights=weights, histtype='bar', color='blue', rwidth=0.9)
    pylab.title("Треугольное распределение")
    print("Треугольное распределение:")
    print("Мат. ожидание: ", tle_m)
    print("Дисперсия: ", tle_v)
    print("СКО: ", tle_s)
    pylab.show()

    left = 2.5
    right = 14.3
    simpsond = simpson(left, right, size)
    simpson_m = np.mean(simpsond)
    simpson_v = np.var(simpsond)
    simpson_s = np.std(simpsond)
    weights = np.ones_like(simpsond) / float(len(simpsond))
    pylab.hist(simpsond, bins=np.linspace(min(simpsond), max(simpsond), 21),
               weights=weights, histtype='bar', color='blue', rwidth=0.9)
    pylab.title("Распределение Симпсона")
    print("Распределение Симпсона:")
    print("Мат. ожидание: ", simpson_m)
    print("Дисперсия: ", simpson_v)
    print("СКО: ", simpson_s)
    pylab.show()

if __name__ == '__main__':
    main()