a = input("nhập tên nhân viên: ")
b = float(input("nhập mức lương tháng: "))
while b < 0:
    print("Lỗi")
    b = float(input("Nhập lại: "))
    if b >= 0:
        break
c = int(input("nhập số ngày đi làm thực tế: "))
while c < 0:
    print("Lỗi")
    c = float(input("Nhập lại: "))
    if c >= 0:
        break
d = int(input("nhập số sản phẩm bán được: "))
while d < 0:
    print("Lỗi")
    d = float(input("Nhập lại: "))
    if d >= 0:
        break
if d < 10:
    e = 0
else:
    if d >= 10 and d<30:
        e = float(1000000)
    else:
        if d >= 30 and d < 50:
            e = float(2000000)
        else:
            e = float(3000000)
f = (b/26)*c + e
f = int(f)
t = 0
r = 0
w = 0
q = f%1000
if f <= 999999:
    w = f//1000
if f >= 1000000 and f<= 999999999:
    r = f//1000000
    w = (f-r*1000000)//1000
if f >= 1000000000 and f <= 999999999999:
    t = f//1000000000
    r = (f-t*1000000000)//1000000
    w = (f-t*1000000000-r*1000000)//1000
if q <= 9:
    q = str(q)
    q = "00"+q
else:
    if q >= 10 and q <= 99:
        q = str(q)
        q = "0"+q
if w <= 9:
    w = str(w)
    w = "00"+w
else:
    if w >= 10 and w <= 99:
        w = str(w)
        w = "0"+w
if r <= 9:
    r = str(r)
    r = "00"+r
else:
    if r >= 10 and r <= 99:
        r = str(r)
        r = "0"+r
if t <= 9:
    t = str(t)
    t = "00"+t
else:
    if t >= 10 and t <= 99:
        t = str(t)
        t = "0"+t
print("lương tháng của",a,"là",t,r,w,q,"VND")
