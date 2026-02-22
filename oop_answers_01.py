class Point():
    def __init__(self, x, y):
        """
        x = horizontal axis
        y = vertical axis
        """
        self.x = x
        self.y = y
    
    def move_left(self, value) -> None:
        self.x -= value
    
    def move_right(self, value) -> None:
        self.x += value
    
    def move_up(self, value) -> None:
        self.y += value
    
    def move_down(self, value) -> None:
        self.y -= value
    
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

p1 = Point(x=5.4, y=8.1)
print(p1)

p1.move_right(2.5)
p1.move_up(3)

print(p1)