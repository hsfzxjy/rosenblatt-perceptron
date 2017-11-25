#!/usr/bin/env python3

import sys
import argparse
from random import random
from functools import reduce
import os.path as path

import numpy as np

if __name__ == '__main__':
    param_file_name = path.join(path.dirname(__file__), 'param')

    if not path.isfile(param_file_name):
        print('No parameter specified.')
        sys.exit(1)

    with open(param_file_name, 'r') as f:
        param = np.array([float(x) for x in f.read().strip().split()])

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=10000, dest='number')
    parser.add_argument('-f', action='store_true', default=False, dest='flag')
    parser.add_argument('-nl', action='store_true', default=False, dest='non_linear')

    dim = param.shape[0]
    options = parser.parse_args()

    func = {
        True: lambda data: reduce(
            lambda x, y: x * y,
            [(x - y) for x, y in zip(param, data)]
        ),
        False: lambda x: x.dot(param)
    }[options.non_linear]

    for _ in range(options.number):
        data = np.array([random() * 100 * (-1 if random() > .5 else 1) for __ in range(dim)])
        print(*list(data))

        if options.flag:
            flag = 1 if func(data) > 0 else -1
            print(flag)
