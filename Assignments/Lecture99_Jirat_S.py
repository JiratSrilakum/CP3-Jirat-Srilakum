from tkinter import *
import math

def leftClickbutton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(result)
    if result < 18.5:
        labelResult.configure(text = "น้ำหนักน้อย/ผอม")
    elif result < 23:
        labelResult.configure(text="ปกติ(สุขภาพดี)")
    elif result < 25:
        labelResult.configure(text="ท้วม/โรคอ้วนระดับ 1")
    elif result < 30:
        labelResult.configure(text="อ้วน/โรคอ้วนระดับ 2")
    else:
        labelResult.configure(text="อ้วนมาก/โรคอ้วนระดับ 3")

mainWindow = Tk()
labelHeight = Label(mainWindow,text = "ส่วนสูง(cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text = "น้ำหนัก(kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickbutton)
calculateButton.grid(row=2,column=0)
labelResult = Label(mainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
mainWindow.mainloop()