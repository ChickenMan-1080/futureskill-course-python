import sys
from tkinter import Tk,simpledialog,messagebox

def rec(width,length):
    loresult = width * length
    return loresult

root = Tk()
root.withdraw()
openBox = ''
openBox = simpledialog.askstring('Rectangle calculate','Are you ready? y/n :')
if openBox == 'y':
    while True:
        input_width = ''
        input_length = ''
        input_width = simpledialog.askinteger('Width Input','Enter width : ')
        input_length = simpledialog.askinteger('Length Input','Ener length : ')
        if input_width == 6 and input_length == 7:
            messagebox.showinfo(' 6 7 ?', ' 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! 67! ...')
            root.destroy()
            sys.exit()
        else:
            result = rec(input_width,input_length)
            messagebox.showinfo('Answer','The area of Rectangle is ' + str(result))
            choice = ''
            choice = simpledialog.askstring('Having fun?','Do you wanna keep going? y/n : ')
            if choice == 'n':
                messagebox.showinfo('Bye!','Thank you for today,see you next time')
                root.destroy()
                sys.exit()
else:
    messagebox.showinfo('=_=','Bye')
    root.destroy()
    sys.exit()
        
