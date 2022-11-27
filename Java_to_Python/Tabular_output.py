
print("%-10s%-10s%-10s%s" % ("N", "N^2", "N^3", "N^4"))
# print(f"{'N':<10}{'N^2':<10}{'N^3':<10}N^4")
for i in range(1, 6):
    num1 = i*i
    num2 = num1*i
    num3 = num2*i
    print("%-10d%-10d%-10d%d" % (i, num1, num2, num3))
