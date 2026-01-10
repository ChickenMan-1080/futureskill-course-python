# Python mini Game

[Script](https://github.com/ChickenMan-1080/futureskill-course-python/blob/main/Python%20mini%20Game.py) นี้คืองานส่งของ Course เรียน **Future Skill Upskill Python programming**
ที่มีการปรับปรุงต่อหลังจากส่งไปแล้วเพื่อความเข้าแล้วให้เห็นถึงปัญหาที่อาจเกิด
โดยที่โจทย์ของ class ก่อนมีการปรับปรุง คือ **"ให้ผู้เรียนเขียนโปรแกรมคำนวณหาพื้นที่สี่เหลี่ยมผืนผ้าโดยใช้ Library tkinter"**  

## สารบัญ

 - [เครื่องมือที่ใช้](#%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%83%E0%B8%8A%E0%B9%89)
 - [ภาพรวมการทำงาน](#%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B3%E0%B8%87%E0%B8%B2%E0%B8%99)
 - [ปัญหาที่เจอและวิธีแก้ไข](#%E0%B8%9B%E0%B8%B1%E0%B8%8D%E0%B8%AB%E0%B8%B2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%88%E0%B8%AD%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B9%81%E0%B8%81%E0%B9%89%E0%B9%84%E0%B8%82)
 - [สิ่งที่ได้เรียนรู้ใน Project](#%E0%B8%AA%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%84%E0%B8%94%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%99%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%83%E0%B8%99-project)
## เครื่องมือที่ใช้

 - **Language :** python 3.13.9
 - **Libraries :**  sys , tkinter ( Tk , simpledialog , messagebox )
 - **Text Editor :** Visual Studio Code
 - **AI Assistant :** Gemini 3
 - **Markdown Editor :** StackEdit.io 

## ภาพรวมการทำงาน

 1. เมื่อรัน script จะมีหน้า GUI ถามความพร้อมของผู้ใช้ ซึ่งมีให้ตอบ 2
    แบบคือ **y** หรือ **n** หากตอบ **"y"** ระบบทำงานต่อไป หากตอบ **"n"**
    จะจบการทำงานโปรแกรม ในกรณีที่พิมพ์นอกเหนือจากนั้นจะมีหน้าต่าง GUI
    ขึ้นมาเตือนแล้ววนกลับไปถามคำถามแรกใหม่
 2. เมื่อตอบ **y**
    ระบบจะถามความกว้างและความยาวของสี่เหลี่ยมผืนผ้าให้ผู้ใช้ใส่
    **input**

 3. ในกรณีที่ผู้ใช้ใส่ **ความกว้าง == 6** และ **ความยาว == 7**  ระบบจะขึ้นหน้าต่างพร้อมข้อความ **67** ทั่วหน้าต่าง GUI (ใส่มาเพื่อให้มีลูกเล่น) แล้วจบการทำงาน แต่หาก เป็นตัวเลขนอกเหนือจากนั้นระบบจะแสดงผลคูณของ ความกว้าง และ ความยาว แล้วถามจะถามผู้ใช้ว่าอยากเล่นต่อไหม โดยให้ตอบ y หรือ n
 4. หากตอบนอกเหนือจาก **y** และ **n** จะวน Loop ถามซ้ำไปเรื่อยๆ และเมื่อตอบ **"y"** ระบบจะออกจาก Loop แล้วกลับไปเล่นใหม่ แต่หากตอบ **"n"** ก็จะจบการทำงานโปรแกรม
  
## ปัญหาที่เจอและวิธีแก้ไข
ปัญหาเหล่านี้คือปัญหาที่เจอทั้งตอนก่อนส่งงาน Future Skill และ หลังส่งที่นำมาปรับปรุงเพิ่มเติม


 -   **ปัญหาการจับเงื่อนไขไม่ถูกต้อง**

เมื่อผู้ใช้ พิมพ์ **y** ระบบจะไปขั้นตอนต่อไปตามปกติ หรือ **n** จะจบการทำงานของโปรแกรม   แต่ **ปัญหาที่เกิดคือ**เมื่อผู้ใช้พิมพ์ตัวอื่นที่ไม่ใช่ **y** หรือ **n** หรือกด cancelที่ให้ค่าเป็น NoneType ระบบจบการทำงานทันทีเนื่องจาก คำสั่ง else: ที่เป็น true เสมอ หากไม่ใช่ **y**  ซึ่งไม่เป็นไปตาม logic ที่ผมอยากให้เป็น 

    openBox = simpledialog.askstring('Rectangle calculate','Are you ready? y/n :')
    if openBox == 'y':
     .
     .
     .
    else:
        messagebox.showinfo('=_=','Bye')
        root.destroy()
        sys.exit()

 **วิธีที่แก้** คือ เพิ่ม while True ไว้บรรทัดบน openBox แล้วเพิ่ม Condition
หากเป็น ตัวอักษรอื่นที่ไม่ใช่ n และ เป็น NoneType ให้ขึ้นหน้าต่าง GUI เตือนหลังจากนั้นโปรแกรมจะวน Loop ซ้ำ เพื่อบังคับให้ผู้ใช้ตอบแค่ **y** หรือ **n**

    while  True :
    
        openBox = simpledialog.askstring('Rectangle calculate','Are you ready? y/n :')
        if openBox ==  'y':
         .
         .
         .
        elif openBox ==  'n':
            messagebox.showinfo('=_=','Bye')
            root.destroy()
            sys.exit()
    
        else :
            messagebox.showinfo('Huh!?','There are 2 options , follow what it said')

##

 - **การประกาศ ตัวแปร ซ้ำ**

**script** ตัวเก่ามีการประกาศตัวแปรซ้ำโดยไม่จำเป็นจึงมีการลบออกเพื่อให้ง่ายต่อการทำความเข้าใจมากขึ้น

**Before :**

    openBox =  ''
    openBox = simpledialog.askstring('Rectangle calculate','Are you ready? y/n :')
    .
    .
    input_width =  ''
    input_length =  ''
    input_width = simpledialog.askinteger('Width Input','Enter width : ')
    input_length = simpledialog.askinteger('Length Input','Enter length : ')
    .
    .
    choice =  ''
    choice = simpledialog.askstring('Having fun?','Do you wanna keep going? y/n : ')

**After :**

    openBox = simpledialog.askstring('Rectangle calculate','Are you ready? y/n :')
    .
    .
    input_width = simpledialog.askinteger('Width Input','Enter width : ')
    input_length = simpledialog.askinteger('Length Input','Enter length : ')
    .
    .
    choice = simpledialog.askstring('Having fun?','Do you wanna keep going? y/n : ')


 
##
 - **ปัญหาที่ TypeError เมื่อค่าที่ใส่เป็น NoneType** 

เมื่อมีการกด cancel ที่

    input_width = simpledialog.askinteger('Width Input','Enter width : ')
    input_length = simpledialog.askinteger('Length Input','Enter length : ')

ระบบจะใส่ค่า Data Type เป็น None ซึ่งทำให้เกิด Error ที่มีการคำนวณจาก Function **rec** 

    def rec(width,length):
        loresult = width * length
        return loresult

**วิธีแก้ปัญหาคือ** เพิ่ม Condition ไปว่าหาก width หรือ length เป็น None ให้ผู้ใช้ออกจาก Loop แล้ววนเข้าลูปใหม่ เพื่อให้ผู้ใช้ตัดสินใจว่าจะเลิกเล่นไหม

    if input_width is  None  or input_length is  None :
        messagebox.showinfo('Hmmm..','Are you tryna cancel? i will bring you to where you can end program')
        break
##

 - **ปัญหา Error ที่การแสดงผลการคูณ** 

หลังจากที่มีการคำนวณ แล้วเอา result มารับ ค่า Function **rec** ที่ **return** ออกมา
เมื่อ แสดง คำตอบที่ หน้าต่าง GUI จะเกิด TypeError เนื่องจาก massagebox จะแสดงแค่ข้อมูล Data Type ที่เป็น **string** เท่านั้น ดังนั้นจึงมีการเปลี่ยน Data Type ของ result ให้อยู่ในรูปของ string โดยใช้ 'str(result)' 

    else:
        result =  rec(input_width,input_length)
        messagebox.showinfo('Answer','The area of Rectangle is '  +  str(result))
##

 - **ปัญหาการจับเงื่อนไขไม่ถูกต้อง (ช่วงตัดสินใจจะเล่นต่อหรือหยุด)**

ใน **script** เก่ามีการถามให้ ตอบ **y** หรือ **n** ซึ่งเมื่อตอบ **n** จะจบการทำงานทันที
แต่ใน กรณีที่จะเล่นต่อ จะสามารถตอบแบบใดก่อนได้ ซึ่งไม่เป็นไปตาม logic ที่อยากให้เป็น

    choice = simpledialog.askstring('Having fun?','Do you wanna keep going? y/n : ')
    if choice ==  'n':
        messagebox.showinfo('Bye!','Thank you for today,see you next time')
        root.destroy()
        sys.exit()

**วิธีแก้ปัญหาคือ** ใช้ **while loop** ที่มี **condition** มาแก้ปัญหา 
(เหตุผลที่ไม่ใช้ **while True** เนื่องจากอยากลองฝึกเขียน **condition** เอง)
โดยที่ไม่ว่าผู้ใช้จะพิมพ์อะไรนอกเหนือจาก **y** และ **n** จะไม่สามารถเล่นต่อหรือจบการทำงานได้จนกว่าจะพิมพ์ **y** หรือ **n** ในการเลือก และแม้ว่าจะกด **cancel** ก็จะไม่สามารถจบการทำงานโปรแกรมได้เช่นกัน

    choice = simpledialog.askstring('Having fun?','Do you wanna keep going? y/n : ')
    while choice !=  'y'  and choice !=  'n':
        messagebox.showinfo('Excuse me?','what is that even mean? try again')
        choice = simpledialog.askstring('Having fun?','So do you wanna keep going? y/n : ')
        
        if choice ==  'n':
            messagebox.showinfo('Bye!','Thank you for today , see you next time')
            root.destroy()
            sys.exit()

## สิ่งที่ได้เรียนรู้ใน Project

 - **การใช้งาน Libraries  module** 
 
การจัดการ **Library** ที่เกี่ยวข้อง ดึง **Module** ของ **library tkinter** มาใช้ โดยไม่ต้อง import มาทั้งหมด วิธีการเรียก **API** เพื่อทำงาน และเข้าใจข้อจำกัดของ **Module** เช่น **messagebox** ที่รับค่าและแสดงผลได้เฉพาะ **string**
 ##
 - **โครงสร้าง Logic และลำดับการทำงาน**    
 
 ได้ทำความเข้าใจ logic การทำงานของ python และได้เรียนรู้การเขียนลักษณะการเขียน **syntax** **Python** เข้าใจภาพรวมคร่าวๆลักษณะภาษาของ Python ที่ทำงานแบบ
 **OOP(Object-Oriented Programming)** ที่มองเป็นเหมือนวัตถุเป็นจุดศูนย์รวมข้อมูลที่ลดความซับซ้อนของโค้ด และ สามารถนำมาใช้งานซ้ำได้ เช่น **Function rec** ที่ parameter รับค่า **Numeric** เพื่อคำนวณสูตรหาพื้นที่สี่เหลี่ยมผืนผ้า

   
       ''' def rec(width,length):
               loresult = width * length
               return loresult '''

และการเรียกใช้ Function ที่สามารถนำมาใช้ต่อได้โดยการใช้ตัวแปรมารับค่า return ของ Function เปิดเอาคำตอบนั้นไปแสดงผลบนหน้า GUI 

    '''
        result =  rec(input_width,input_length)
        messagebox.showinfo('Answer','The area of Rectangle is '  +  str(result))'''
        

##
