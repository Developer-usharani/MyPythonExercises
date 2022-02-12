# class A:
#     def f():
#         a=876
#         b=5424
#         print(a+b)
#     f()
#     def __init__(self):
#         self.x= 10
#         self.y=20
# class B(A):
#     def __init__(self):
#         print("b object")
#         super().__init__()
# b = B()
# a = A()
# print(a.x)
# print(a.y)


# class A:
#     def f():
#         x=10
#         y=20
#         print(x,y)
#     f()



# class Test:
#     def __init__(self):
#         self.x= 10
#         self.y=20
#         self.z=30
# t = Test()
# print(t.x)
# print(t.y)
# print(t.z)



# class Car:
#     def __init__(self):
#         self.x=10
#         print("car object")
# class BMW(Car):
#     def __init__(self):
#         self.x_=20
#         self._y=5
#         print("BMW object")
#         super().__init__()
# b = BMW()



class A:
    x=10
    print(x)
    def a():
        return "a constructor"
    def b():
        return 10/2
class B(A):
    pass
b=B()
