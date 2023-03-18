from tkinter import *
import random

# Computer Science FB01, Lab 8.1, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 8.1")
print("Сахній Назар ФБ-01")

window = Tk()
window.title("Lab 8.1")
window.geometry('175x110')

label = Label(window, text="0", fg="black", bg="yellow", width=10, height=5)
label.grid(row=1, column=0)


def increase_or_decrease():
    counter = int(str(label['text']))
    counter += random.randint(-100, 100)
    label.config(text=str(counter))


def clear_window():
    label.config(text="0")


def close_window():
    window.destroy()


inc_dec = Button(window, bg="blue", text="Inc/Dec", command=increase_or_decrease)
inc_dec.grid(row=0, column=0, sticky="nsew")

clear = Button(window, bg="white", text="Clear", command=clear_window)
clear.grid(row=0, column=1, sticky="nsew")

goodbye = Button(window, bg="red", fg="black", text="Goodbye", command=close_window)
goodbye.grid(row=0, column=2, sticky="nsew")

window.mainloop()
