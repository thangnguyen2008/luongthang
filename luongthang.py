a = input("nhập tên nhân viên:")
b = float(input("nhập mức lương tháng"))
c = int(input("nhập số ngày đi làm thực tế"))
d = int(input("nhập số sản phẩm bán được"))
if d < 10:
    k = 0
else:
    if d >= 10 and d<30:
        k = float(1000000)
    else:
        if d >= 30 and d < 50:
            k = float(2000000)
        else:
            k = float(3000000)
e = d/26*c + k
e = int(e)
print("lương tháng của ",a," là ",e,"VND")
