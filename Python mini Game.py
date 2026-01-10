import sys
from tkinter import Tk,simpledialog,messagebox

def rec(width,length):
    loresult = width * length
    return loresult

root = Tk()
root.withdraw()
while True :
    openBox = simpledialog.askstring('Rectangle calculate','Are you ready? y/n :')
    if openBox == 'y':
        while True:
            input_width = simpledialog.askinteger('Width Input','Enter width : ')
            input_length = simpledialog.askinteger('Length Input','Enter length : ')
            if input_width == None or input_length == None :
                messagebox.showinfo('Hmmm..','Are you tryna cancel? i will bring you to where you can end program')
                break
            elif input_width == 6 and input_length == 7:
                messagebox.showinfo(' 6 7 ?', ' 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! ...')
                root.destroy()
                sys.exit()
            else:
                result = rec(input_width,input_length)
                messagebox.showinfo('Answer','The area of Rectangle is ' + str(result))
                choice = simpledialog.askstring('Having fun?','Do you wanna keep going? y/n : ')
                while choice != 'y' and choice != 'n':
                    messagebox.showinfo('Excuse me?','what is that even mean? try again')
                    choice = simpledialog.askstring('Having fun?','So do you wanna keep going? y/n : ')

                if choice == 'n':
                    messagebox.showinfo('Bye!','Thank you for today , see you next time')
                    root.destroy()
                    sys.exit()
                
    elif openBox == 'n':
        messagebox.showinfo('=_=','Bye')
        root.destroy()
        sys.exit()

    else :
        messagebox.showinfo('Huh!?','There are 2 options , follow what it said')
        
    

