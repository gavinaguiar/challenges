'''
Overlapping rectangles
Given points (bottom left and top right) of two rectangles
determine if the rectangles overlap
Input: Rect1, Rect2
Output: True/False
'''
class Rect:
    def __init__(self,bottom_x,bottom_y,top_x,top_y):
        self.bottom_x=bottom_x
        self.bottom_y=bottom_y
        self.top_x=top_x
        self.top_y=top_y


def overlap(rect1,rect2):
    ydist = distance(rect1.bottom_y,rect2.bottom_y,rect1.top_y,rect2.top_y)
    if ydist <=0:
        return False
    xdist = distance(rect1.bottom_x,rect2.bottom_x,rect1.top_x,rect2.top_x)
    if xdist <= 0:
        return False
    return True

def distance(r1b_xy,r2b_xy,r1t_xy,r2t_xy):
    return (min(r2t_xy,r1t_xy) - max(r1b_xy,r2b_xy))
    

rect1 = Rect(2,1,5,5)
rect2 = Rect(3,2,5,7)

print overlap(rect1,rect2)
