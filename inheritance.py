class Animal:

    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale,exhale")

class Fish(Animal):
    def __init__(Self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doin this underwtaer only.")
    def swim(self):
        print("movin in water")

nemo=Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)