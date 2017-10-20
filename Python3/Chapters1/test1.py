#if 语法
a=1
if a>0:
	print("haha")
else:
	print("bbbb")

#打印结果输出小数点后一位
t1 = int(72)
t2 = int(85)
t3 = t1 / t2
print("%.1f" % (t1 / t2))

#计算体重的BMI
higt=1.72
height=77.5
bmi=height / (higt * higt)
print(bmi)

if bmi < 18.5:
	print("过轻")
elif (bmi >= 18.5 and bmi < 25):
	print("正常")
elif bmi >= 25 and bmi < 28:
	print("过重")
else:
	print("no")
