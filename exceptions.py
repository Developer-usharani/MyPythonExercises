# def divid(x,y):
#     try:
#         result = x//y
#         print("yeah your answer is:",result)
#     except:
#         print("sorry your dividing zero")
# divid(3,2)


# def r(a,b):
#     try:
#         result = a//b
#         print("dividing",result)
#     except:
#         print("answer is corrrect")
# r(7867,0)




# def f(a,b):
#     try:
#         c = ((a+b)/(a-b))
#     except:
#         print("a/b result is 0")
#     else:
#         print(c)
# f(4,5)



try:
    k = 5//0
except:
    print("con't divide")
finally:
    print("always executed")