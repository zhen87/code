#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = qlz
# date = 2021/5/29
# file = list.py


import os

list = [x for x in range(2, 5)]
print(list)

list1 = [x for x in range(50) if x % 2 == 0]
print(list1)

list2 = [m + n for m in '1234' for n in 'ASDFFG']
print(list2)

list3 = [y for y in os.listdir('..')]
print(list3)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


d = odd()
while True:
    print(next(d))
