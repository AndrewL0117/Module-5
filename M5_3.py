# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:25:55 2024

@author: xboxl
"""

class Rectangle:
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height

def str_rectangle(rect):
    return f"Rectangle(({rect.x1}, {rect.y1}), ({rect.width}, {rect.height})"

def create_rectangle(x1, y1, width, height):
    return Rectangle(x1, y1, width, height)


def shift_rectangle(rect, dx, dy):
    rect.x1 += dx
    rect.y1 += dy

def offset_rectangle(rect, dx, dy):
    x1 = rect.x1 + dx
    y1 = rect.y1 + dy
    return Rectangle(x1, y1, rect.width, rect.height)

r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1)) # should be same as previous
print(str_rectangle(r2))