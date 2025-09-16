name=input("enter your name")
rollno=int(input("enter your roll no"))
m1=int(input("enter your mark 1"))
m2=int(input("enter your mark 2"))
m3=int(input("enter your mark 3"))
total=m1+m2+m3
print(total)
avg=total/3
print(avg)
if m1>40 and m2>40 and m3>40:
    result=("pass")
    print(result)
else:
    result=("fail")
    print(result)
if result=="pass":
    if avg>90:
        print("Grade A")
    elif avg>80:
        print("Grade B")
    elif avg>70:
        print("Grade C")
    elif avg>60:
        print("Grade D")
    else:
        print("Grade E")