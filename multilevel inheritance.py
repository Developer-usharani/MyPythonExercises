class Car:
    def __init__(self):
        self.x=10
        print("Car object")
class BMW(Car):
    def __init__(self):
        self.x=20
        print("BMW object")
class BMW_3_series(BMW):
    pass
class BMW_7_series(BMW):
    def __init__(self):
        self.x=30
        print("BMW_7_series object")
class Benz(Car):
    def __init__(self):
        print("Benz object")
        self.x=40
        super().__init__()
class Test(Benz,BMW_7_series,BMW_3_series):
    def __init__(self):
        self.x=50
        super().__init__()
        print("Test object")

        
t = Test()
print(t.x)
