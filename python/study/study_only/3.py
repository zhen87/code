#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = qlz
# date = 2021/6/7
# file = 3.py


def func():
    username = "快不快"
    def func2():
        nonlocal username
        username = "慢"
        print(username)
    func2()
    print("我是func的username,",username)
func()

