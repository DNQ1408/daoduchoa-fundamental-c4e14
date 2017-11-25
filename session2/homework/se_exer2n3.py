n = float(input("Nhap so:"))
fac = 1
if n % 1 != 0 or n < 0:
    n = int(input("Hay nhap so tu nhien"))
for i in range (1,n+1):
        fac = fac * i
print("Giai thua cua", n, "la", fac)
