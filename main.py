from tkinter import *

window = Tk()
window.title("Distance Convertor")
window.minsize(height=150, width=400)
window.config(padx=100, pady=20)


def clicked():
    miles = input.get()
    mile = int(miles)
    km = round(mile * 1.6)
    label4.config(text=km)


label1 = Label(text=" ")
label1.grid(row=0, column=0)

input = Entry()
input.grid(row=0, column=2)

label2 = Label(text="Miles")
label2.grid(row=0, column=3)
label2.config(padx=60, pady=20)

label3 = Label(text="is equal to")
label3.grid(row=1, column=0)
label3.config(padx=30)

label4 = Label(text="0")
label4.grid(row=1, column=2)

label5 = Label(text="Km")
label5.grid(row=1, column=3)

button = Button(text="Calculate", command=clicked)
button.grid(row=2, column=2)

window.mainloop()
