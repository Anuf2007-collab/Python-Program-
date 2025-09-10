a=[]
print(a)
n=int(input("enter no of elements"))
i=0
for i in range(0,n):
    b=int(input("enter the number"))
    a.append(b)
    i=i+1
print(a)
print(a[0])
print(a[-1])
print(a[2])
print(a[-3:])
print(a.index(3))
print(a.index(4))
print(a.index(5))
c=[6,7,8]
a.extend(c)
print(a)
print(len(a))
