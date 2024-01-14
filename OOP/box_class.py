
class Box:

    def __init__(self, h, w, d):
        self.height = h
        self.width = w
        self.depth = d

    def __del__(self):
        print("The box is removed")

    def volume(self):
        return (self.height * self.width, self.depth)

    def __str__(self):
        string = f"The box height is {self.height}\nWidth={self.width}\nDepth is : {self.depth}, Volume is {self.volume()}"
        return string 


b1 = Box(10, 4, 6)
print(b1.height, "\n", b1.width, "\n", b1.depth)
print(str(b1))
