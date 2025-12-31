# class A:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         print(x,y)
# obj = A(10,20)
# li = A(35, 40)

# class B:
#     def __init__(self):
#         self.x = 40
#         self.y = 50
#         print("Init Completed")
# a = B()
# print(a.x + a.y)

# class Ticket:
#     def __init__(self,n,a,des):
#         self.name = n
#         self.age = a
#         self.destination = des
# t1 = Ticket("charitha", 25, "Hyderabad")
# print(t1.name)
# print(t1.age)
# print(t1.destination)

# class Student:
#     def __init__(self,name,rollNo,sec):
#         self.name = name
#         self.rollNo = rollNo
#         self.section = sec
# S1 = Student("Charitha", "5H8", "Python-04")
# print(S1.name, S1.rollNo, S1.section)

#print next prime to the given number
# 1,2,3,4,'5',6,"7",8,9,10,11,12,13,14,15

# import math
# n = int(input())
# c = 0
# while n>=0:
#     n += 1
#     fc = 0
#
#     if n < 2:
#         continue
#     for i in range(2,int(math.sqrt(n))+1):
#         if n % i == 0:
#             fc += 1
#     if fc == 0:
#         print(n)
#         break

#print previous prime number of given number

# import math
# n = int(input())
# while n>0:
#     n-=1
#     fc = 0
#     if n<2:
#         print("No prime numbers previously")
#         continue
#     for i in range(2,int(math.sqrt(n))+1):
#         if n % i==0:
#             fc += 1
#     if fc == 0:
#         print(n)
#         break

#print nth prime number of given number
# import math
# p = int(input())
# n = int(input())
# c = 0
# while c < n:
#     if p<2:
#         p+=1
#         continue
#     fc = 0
#
#     for i in range(2,int(math.sqrt(p))+1):
#         if p % i == 0:
#             fc+=1
#     if fc == 0:
#         c += 1
#         if c == n:
#             print(p)
#             break
#     p+=1

#nearest prime number of given number
import math
def is_Prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
p = n -1
q = n+1
while True:
    if is_Prime(p):
        break
    p -=1
while True:
    if is_Prime(q):
        break
    q +=1
if abs(n-p) > abs(n-q):
    print(q)
elif abs(n-p) < abs(n-q):
    print(p)
elif abs(n-p) == abs(n-q):
    print(p,q)
