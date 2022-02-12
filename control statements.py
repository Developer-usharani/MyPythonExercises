# for i in range(15,25):
#     if i < 18:
#         print("your not eligible for vote")
#     elif i >= 20:
#         print("your eligible for vote ")
#     else:
#         print("false")




def f(a,b,c):
    sum = (a+b+c)
    if sum > 270:
        print("a+ grade")
    elif sum >240:
        print("a grade")
    elif sum <240:
        print("b grade")
    elif sum >180:
        print("c grade")
    elif sum <180:
        pass
    else:
        print("fail")
f(30,59,60)