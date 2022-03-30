from re import A

class triangle:
    def __init__(self, a, b, c, d) -> None:
        self.side_base = a
        self.side_b = b
        self.side_c = c
        self.side_height = d

    def perimeter(self):
        tri_per = self.side_base + self.side_b + self.side_c
        return tri_per

    def area(self):
        tri_area = (self.side_base/2) * self.side_height
        return tri_area

triangle_1 = triangle(8, 6, 7, 9)
sum = triangle_1.perimeter()
sum2 = triangle_1.area()
print(sum)
print(sum2)