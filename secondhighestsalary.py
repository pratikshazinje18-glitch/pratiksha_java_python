a = int(input("enter salary 1:"))
b = int(input("enter salary 2:"))
c = int(input("enter salary 3:"))
d = int(input("enter salary 4:"))
e = int(input("enter salary 5:"))

highest = a
if b >= highest:
    highest=b
if c >= highest:
    highest=c
if d >= highest:
    highest=d
if e >= highest:
    highest=e

highest = a       
if b> second and b!=highest:
    second =b
if c> second and c!=highest:
    second =c
if d> second and d!=highest:
    second =d
if e> second and e!=highest:
    second =e

print("highest salary=" ,highest)
print("second highest salary=" ,second)

    

