#!/usr/bin/env python3

import sys
import os.path as path
from functools import partial
import numpy as np

if __name__ == '__main__':

    resolve = partial(path.join, path.dirname(__file__))
    trained_fn = resolve('trained')

    if not path.isfile(trained_fn):
        print('No trained data specified. Aborted.', file=sys.stderr)
        sys.exit(1)

    with open(trained_fn, 'r') as f:
        w = np.array([float(x) for x in f.read().strip().split()])

    total = correct = 0

    while True:
        line1 = sys.stdin.readline()

        if not line1:
            break

        data = np.array([float(x) for x in line1.strip().split()])
        flag = int(sys.stdin.readline().strip())

        total += 1

        predict = 1 if w.dot(data) > 0 else -1

        if predict == flag:
            correct += 1

    print('Correctness:')
    print(f'{correct}/{total} = {correct / total * 100}%')
