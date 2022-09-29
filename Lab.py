from ast import keyword
from turtle import distance

#โรงแรม
from_0 =       [{"name":"หาดนางทอง", "key":1, "distant":4.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":2.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":32.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":10.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":11.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":14.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":3.00}]
#หาดนางทอง
from_1 =       [{"name":"โรงแรม", "key":0, "distant":4.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":27.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":37.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":47.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":33.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":14.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":38.00}]
#ประภาคารเขาหลัก
from_2 =       [{"name":"โรงแรม", "key":0, "distant":2.00}, 
                {"name":"หาดนางทอง", "key":1, "distant":27.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":3.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":25.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":10.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":4.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":9.00}]
#หาดเขาหลัก
from_3 =       [{"name":"โรงแรม", "key":0, "distant":32.00}, 
                {"name":"หาดนางทอง", "key":1, "distant":37.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":3.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":13.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":1.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":7.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":16.00}]
#น้ำตกโตนช่องฟ้า
from_4 =       [{"name":"โรงแรม", "key":0, "distant":10.00}, 
                {"name":"หาดนางทอง", "key":1, "distant":47.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":25.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":13.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":9.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":5.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":1.00}]
#ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา
from_5 =       [{"name":"โรงแรม", "key":0, "distant":11.00}, 
                {"name":"หาดนางทอง", "key":1, "distant":33.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":10.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":1.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":9.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":21.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":7.00}]
#หาดคึกคัก
from_6 =       [{"name":"โรงแรม", "key":0, "distant":16.00}, 
                {"name":"หาดนางทอง", "key":1, "distant":14.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":4.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":7.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":5.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":21.00}, 
                {"name":"หาดปากวีป", "key":7, "distant":9.00}]
#หาดปากวีป
from_7 =       [{"name":"โรงแรม", "key":0, "distant":3.00}, 
                {"name":"หาดนางทอง", "key":1, "distant":38.00}, 
                {"name":"ประภาคารเขาหลัก", "key":2, "distant":9.00}, 
                {"name":"หาดเขาหลัก", "key":3, "distant":16.00}, 
                {"name":"น้ำตกโตนช่องฟ้า", "key":4, "distant":1.00}, 
                {"name":"ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา", "key":5, "distant":7.00}, 
                {"name":"หาดคึกคัก", "key":6, "distant":8.00}]

def intro(lists):
    print("Traveling Planner")
    print("********************")
    print("ขณะนี้คุณอยู่ที่เขาหลัก จังหวัดพังงา พบสถานที่ท่องเที่ยวดังนี้")
    for placelist in lists:
        print(placelist["key"], placelist["name"])

intro(from_0)


numselect = int(input("จำนวนสถานที่ท่องเที่ยวที่คุณต้องการจะไป : "))

Cplacelist =[]
i = 0
while i < numselect:
    A = int(input("กรุณาเลือกสถานที่เที่ยวที่คุณต้องการจะไป : "))
    if A == 1:
        print("หาดนางทอง")
        i += 1
    elif A == 2:
        print("ประภาคารเขาหลัก")
        i += 1
    elif A == 3:
        print("หาดเขาหลัก")
        i += 1
    elif A == 4:
        print("น้ำตกโตนช่องฟ้า")
        i += 1
    elif A == 5:    
        print("ศูนย์อนุรักษ์พันธุ์เต่าทะเล ฐานทัพเรือพังงา")
        i += 1
    elif A == 6:
        print("หาดคึกคัก")
        i += 1
    elif A == 7:
        print("หาดปากวีป")
        i += 1
    else:
        print("กรุณาเลือกใหม่อีกครั้งค่ะ")
    Cplacelist.append(A)

distant_list = []
for placelist in from_0:
    for splace in Cplacelist:
        if splace == placelist["key"]:
            distant_list.append(placelist["distant"])

sorted_distant_list = sorted(distant_list)

for placelist in from_0:
    if sorted_distant_list[0] == placelist["distant"]:
        print("สถานที่ที่ 1 :", placelist["name"])
        if placelist["key"] == 1:
            current_list = from_1
        elif placelist["key"] == 2:
            current_list = from_2
        elif placelist["key"] == 3:
            current_list = from_3
        elif placelist["key"] == 4:
            current_list = from_4
        elif placelist["key"] == 5:
            current_list = from_5
        elif placelist["key"] == 6:
            current_list = from_6
        else:
            current_list = from_7
        if sorted_distant_list[0] == placelist["distant"]:
            Cplacelist.remove(placelist["key"])

i = 2
while i <= numselect:

    distant_list.clear()
    sorted_distant_list.clear()

    for placelist in current_list:
        for splace in Cplacelist:
            if splace == placelist["key"]:
                distant_list.append(placelist["distant"])
        
    sorted_distant_list = sorted(distant_list)

    for placelist in current_list:
        if sorted_distant_list[0] == placelist["distant"]:
            print("สถานที่ที่ ", i, ": ", placelist["name"])
            if placelist["key"] == 1:
                current_list = from_1
            elif placelist["key"] == 2:
                current_list = from_2
            elif placelist["key"] == 3:
                current_list = from_3
            elif placelist["key"] == 4:
                current_list = from_4
            elif placelist["key"] == 5:
                current_list = from_5
            elif placelist["key"] == 6:
                current_list = from_6
            else:
                current_list = from_7
            if i < numselect:
                if sorted_distant_list[0] == placelist["distant"]:
                    Cplacelist.remove(placelist["key"])
            else:
                break
    i += 1