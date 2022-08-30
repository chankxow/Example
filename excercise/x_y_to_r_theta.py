import math

x , y = [float(e) for e in input("กำหนดค่า x , y : ").split()]#กำหนดค่า x y


r = math.sqrt((x*x)+(y*y)) #สูตรการหา r เรเดียน
theta = math.atan2(x,y)     #สูตรการหาทีต้า
print(f" r= {r} theta = {theta}") #แสดงผลการหา