import math

r , theta = [float(e) for e in input("เติมค่า  x , y : ").split() ] #กำหนดตัวแปร r และ theta

x = r*math.cos(theta) #กำหนดการหาค่า x
y = r*math.sin(theta) #กำหนดการหาค่า y

print(f"x= {x} y={y}") #แสดงผลข้อมูล x และ y
