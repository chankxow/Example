v1,v2,v3 = [float(e) for e in  input("พิมจำนวน v1 v2 v3 โดยเว้นวรรคแต่ละตัว : ").split()]   #กำหนดตัวแปร v 
u1,u2,u3 = [float(e) for e in input("พิมจำนวน u1 u2 u3 โดยเว้นวรรคแต่ละตัว :").split()]     #กำหนดตัวแปร u

dot_product = v1*u1 + v2*u2 + v3*u3 #กำหนดสูตรการหาค่า

print(f"ค่า dot product ที่ได้: {dot_product}") #output ข้อความ