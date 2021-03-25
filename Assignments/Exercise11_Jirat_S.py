'''
   *      1 -> * = 1
  ***     2 -> * = 3
 *****    3 -> * = 5
*******   4 -> * = 7
'''
number = int(input("Enter the number : "))
for x in range(number): # จำนวนแถว
    text1 = ""
    text2 = ""
    text3 = ""
    for y in range(number-(x+1)): # จำนวนช่องว่าง
        text1 = text1 + " "
    for z in range((2*x)+1): # จำนวน *
        text2 = text2 + "*"
    text3 = text1 + text2
    print(text3)