#import tkinter as tk
#import tkinter.messagebox as msg
#top=tk.Tk()
#def helloCallback():
    #msg.showinfo("Hello Python", "Assalamu'alaikum")
#w=tk.Button(top, text="Hello", command=helloCallback)
#w.pack()
#top.mainloop()



#import tkinter as tk
#from tkinter import messagebox

#top = tk.Tk()
#CheckVar1 = tk.IntVar()
#CheckVar2 = tk.IntVar()
#C1 = tk.Checkbutton(top, text = "Music", variable = CheckVar1,
#onvalue = 1, offvalue = 0, height=5, width = 20)
#C2 = tk.Checkbutton(top, text = "Video", variable = CheckVar2,
#onvalue = 1, offvalue = 0, height=5, width = 20)
#C1.pack()
#C2.pack()
#top.mainloop()    


import tkinter as tk
import tkinter.messagebox as msg
top=tk.Tk()
CheckVar1 = tk.StringVar()
C=tk.Checkbutton(top, text = "Gender", variable = CheckVar1,
                 onvalue = "Tampan", offvalue = "Cantik", height=5)
C.pack()
L1=tk.Label(top, text="Nama: ");L1.pack()
E1=tk.Entry(top, bd=5);E1.pack()
def helloCallback():
    msg.showinfo("Belajar GUI", "Assalamu'alaikum "
                 +E1.get()+"! kamu "+CheckVar1.get()+" sekali hari ini!")   
w1=tk.Button(top, text="Klik saya!", command=helloCallback)  
w1.pack()
top.mainloop()                                    

