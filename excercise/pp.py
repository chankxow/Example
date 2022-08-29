import math


x1,y1 = [int(e) for e in input("x1, y1 : ").split()] # รับค่า x1 y1
x2,y2 = [int(e) for e in input("x1, y2 : ").split()]# รับค่า x2 y2



p1 = (x1-x2)**2 #กำหนดสูตร x1-x2 ยกกำลัง2
p2 = (y1-y2)**2 #กำหนดสูตร y1-y2 ยกกำลัง2

pp = math.sqrt(p1+p2) #สูตรการหาค่าระยะห่างระหว่างจุดสองจุด

print(f" ระยะห่างระหว่างจุด คือ {pp:.2f} ") #output ระยะห่างระหว่างจุดสองจุด


