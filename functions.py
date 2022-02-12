# def splitting(string):
#         for each in string:
#             if(each==','):
#                 pass
#             else:
#                 print(each,end='*')
# s = "usha,rani,python"
# splitting(s)


# def num(x):
#     for i in range(10):
#         print(i)
# num(10)



# def sample(a,b,c):
#     a,b=b,a
#     n=a+b+c;
#     return n/3
# sample(20,40,50)



# def fact(x):
#     if (x == 0):
#         return 1;
#     return x * fact(x-1)
# print(fact(5))   



# def fun(x,y,z):
#     x,y = y,x
#     print("x=",x)
#     print("y=",y)
#     print("average of the given 3 numbers :",(x+y+z)/3)
# fun(7,2,6)



# def square_num(num):
#     return num**2
# print(square_num(67))
# print(square_num(22))



# to print a reverse of string
# def f():
#     s = "python"
#     a = reversed(s)
#     for i in a:
#         print(i)
# f()


def h():
    sample = "1,2,5,65,89,56"
    b = reversed(sample)
    for i in b:
        print(i,end=" ")
h()