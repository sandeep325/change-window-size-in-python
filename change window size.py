from tkinter import *

top=Tk()
top.title("RESIZE WINDOW")
top.geometry("900x400")


def size():
    width_value=width.get()
    height_value = height.get()
    top.geometry(f"{width_value}x{height_value}")


Label(top,text="RESIZE THE WINDOW ACCORDING TO YOUR ENTER NO. BELOW",bg="gray",fg="yellow",font="comicsansms 12 bold")\
    .grid(row=1,column="4")

Label(top,text="Enter the size for the width",font="comicsansms ",pady=5).grid(row=2,column=1,pady=4)
Label(top,text="Enter the size for the height",font="comicsansms ").grid(row=3,column=1,pady=4)


width=StringVar()
height=StringVar()


width_entry= Entry(top,textvariable=width).grid(row=2,column=2)
height_entry= Entry(top,textvariable=height).grid(row=3,column=2)


Button(text="SET SIZE",command= size, pady=6,padx=8,bg="red",fg="white").grid(row=5,column=2,pady=8)



top.mainloop()