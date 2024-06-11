# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:56:21 2024

@author: xboxl
"""

class Rectangle:
    def __init__(self, x1, y1, width, height):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.x2 = x1 + width
        self.y2 = y1 + height

def create_rectangle(x1, y1, width, height):
    print(f"Creating rectangle with bottom-left corner at ({x1}, {y1}) and width {width}, height {height}")
    x2 = x1 + width
    y2 = y1 + height
    print(f"Current rectangle coordinates are ({x1}, {y1}) and ({x2}, {y2})")
    return Rectangle(x1, y1, width, height)


def shift_rectangle(rect, dx, dy):
    print(f"Shifting rectangle by ({dx}, {dy})")
    rect.x1 += dx
    rect.y1 += dy
    rect.x2 += dx
    rect.y2 += dy
    print(f"Shifted rectangle coordinates are ({rect.x1}, {rect.y1}) and ({rect.x2}, {rect.y2})")

def offset_rectangle(rect, dx, dy):
    print(f"Creating offset rectangle by ({dx}, {dy})")
    x1 = rect.x1 + dx
    y1 = rect.y1 + dy
    x2 = rect.x2 + dx
    y2 = rect.y2 + dy
    print(f"Offset rectangle coordinates are ({x1}, {y1}) and ({x2}, {y2})")
    return Rectangle(x1, y1, rect.width, rect.height)

r1 = create_rectangle(10, 20, 30, 40)

shift_rectangle(r1, -10, -20)

r2 = offset_rectangle(r1, 100, 100)