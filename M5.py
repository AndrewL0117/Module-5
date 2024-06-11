# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:52:22 2024

@author: xboxl
"""
class Rectangle:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

def create_rectangle(x1, y1, x2, y2):
        return Rectangle(x1, y1, x2, y2)
    
def string_rectangle(rect):
        return f"Rectangle(({rect.x1}, {rect.y1}), ({rect.x2}, {rect.y2})"
    
def shift_rectangle(rect, dx, dy):
        rect.x1 += dx
        rect.y1 += dy
        rect.x2 += dx
        rect.y2 += dy
        
def offset_rectangle(rect, dx, dy):
    new_x1 = rect.x1 + dx
    new_y1 = rect.y1 + dy
    new_x2 = rect.x2 + dx
    new_y2 = rect.y2 + dy
    return Rectangle(new_x1, new_y1, new_x2, new_y2)
        
r1 = create_rectangle(10, 20, 30, 40)
print(string_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(string_rectangle(r1))

r2 = offset_rectangle(r1, 100, 100)
print(string_rectangle(r1)) # should be same as previous
print(string_rectangle(r2))