import math

x = int(input("กรอก x : "))  #กำหนดตัวแปร output x

y =(((2 - x) + (3/7 * (x**2))) - ((5/11) *( x**3))) + math.log10(x) # กำหนดสูตร โดยต้องจัดลำดับความสำคัญของการทำงานของสัญลักษณ์ทางคณิตศาสตร์

print(f" คำตอบของ  2 - x + 3/7 * x**2 - 5/11 * x**3 + log10(x) เท่ากับ {y} ") #แสดงคำตอบ

