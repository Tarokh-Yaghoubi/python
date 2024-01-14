
class Ratio:
    s = 1
    m = 1

    def assign(self, ss, mm):
        self.s = ss
        self.m = mm

    def invert(self):
        self.s = self.m
        self.m = self.s
    
    def convert(self):
        d = self.s / self.m
        return d

    def __str__(self):
        string = f"The ratio is {str(self.s)} / {str(self.m)}\n"
        return string



r1 = Ratio()


