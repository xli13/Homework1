#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:45:44 2018

@author: liximing
"""
def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return n


for i in range(1,11):
  print(fibonacci(i))

