#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = qlz
# date = 2021/5/28
# file = 2.py


def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    else:
        (min,max) = (L[0],L[0])
        for i in L:
            if max < i:
                max = i
            if min > i:
                min = i
        return (min,max)


findMinAndMax([2, 1])
findMinAndMax([0,0])
findMinAndMax([1,4,2,7,9])
