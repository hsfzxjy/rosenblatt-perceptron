#!/usr/bin/env python3

import sys
import os.path as path
import numpy as np


class Trainer:

    def __init__(self):
        fn = path.join(path.dirname(__file__), 'param')

        if not path.isfile(fn):
            print('No parameter specified. Aborted.', file=sys.stderr)
            sys.exit(1)

        with open(fn, 'r') as f:
            self.dim = len(f.read().strip().split())

        self.w = np.array([0] * self.dim)
        self.ita = .5

    def train(self):
        while True:
            line1 = sys.stdin.readline()

            if not line1:
                break

            data = np.array([float(x) for x in line1.strip().split()])
            flag = int(sys.stdin.readline().strip())

            self.adjust(data, flag)

        print(*list(self.w))

    def adjust(self, data, flag):

        d = 1 if self.w.dot(data) > 0 else -1

        self.w = self.w + self.ita * (flag - d) * data


if __name__ == '__main__':
    Trainer().train()
