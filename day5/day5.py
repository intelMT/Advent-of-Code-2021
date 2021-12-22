example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

from typing import NamedTuple,  Iterable
from collections import Counter 

class Point(NamedTuple):
    x : int
    y : int

class Line:
    def __init__(self, begin: Point, end:Point):
        self.origin = begin
        self.end = end

    def is_horizontal(self):
        return self.origin.y == self.end.y

    def is_vertical(self):
        return self.origin.x == self.end.x

    def points_on_the_line(self)->Iterable[Point]:
        x_lo = min(self.origin.x, self.end.x)
        y_lo = min(self.origin.y, self.end.y)
        x_hi = max(self.origin.x, self.end.x)
        y_hi = max(self.origin.y, self.end.y)

        if self.is_horizontal():
            y = self.origin.y
            for x in range(x_lo, x_hi+1):
                yield Point(x, y)
        elif self.is_vertical():
            x = self.origin.x
            for y in range(y_lo, y_hi+1):
                yield Point(x, y)
        else: # Diagonal
            dy = self.end.y - self.origin.y
            dx = self.end.x - self.origin.x
            x = x_lo
            if dy*dx > 0: # x, y increase or decrease together, their product is positive: a*b == -a*-b 
                for y in range(y_lo, y_hi+1):
                    yield Point(x, y)
                    x +=1
            else: # as x increases, y decreases
                for y in range(y_hi, y_lo-1, -1):
                    yield Point(x, y)
                    x +=1

def parser(data : str) -> Iterable[Line]:
    lines = [line for line in data.split('\n')]
    list_lines = list()              

    for line in lines:
        points = [int(point) for points in line.split(" -> ")
                        for point in points.split(",")]
        list_lines.append(Line(begin=Point(x=points[0], y=points[1]), 
                                end=Point(x=points[2], y=points[3])))
    return list_lines


def count_overlaps(data : str, inc_diag=False)-> int:
    list_lines = parser(data)
    # Count all occurences of the data points
    counts = Counter(point for line in list_lines
                        if any([line.is_horizontal(), line.is_vertical(), inc_diag])
                        for point in line.points_on_the_line())

    overlap_count = sum(count>1 for count in counts.values())
    return overlap_count
        
assert count_overlaps(example) == 5
assert count_overlaps(example, inc_diag=True) == 12

if __name__ == '__main__':
    with open('d5.txt') as f:
        content = f.read()
    
    print(count_overlaps(content))
    print(count_overlaps(content, inc_diag=True))
