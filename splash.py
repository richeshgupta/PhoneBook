from Tkinter import *
root = Tk()
root.wm_title('Richesh Gupta')
root.geometry('600x450')
Label(root,text='Project Title : PhoneBook',font='Arial 20').grid(row=0,column=1)
Label(root,text='Project of Python and database',font='Arial 10').grid(row=1,column=1)
Label(root,text='Developed By: Richesh Gupta(181b165)',font='Arial 8',bg='white').grid(row=2,column=1)
Label(root,text='----------------------------',font='Arial 20').grid(row=3,column=1)
Label(root,text='Make mouse movement over this screen to close',font='Arial 20',fg='red').grid(row=4,column=1)
def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()
