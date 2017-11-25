#!/usr/bin/env python3

import argparse
from random import random

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, dest='number', required=True)
    options = parser.parse_args()

    print(*[random() * 100 * (-1 if random() > .5 else 1) for __ in range(options.number)])
