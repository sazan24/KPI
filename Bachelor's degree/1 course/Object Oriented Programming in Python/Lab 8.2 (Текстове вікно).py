from tkinter import *
# Computer Science FB01, Lab 8.2, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 8.2")
print("Сахній Назар ФБ-01")

window = Tk()
window.title("Lab 8.2")
window.geometry('375x375')

input_field = Text(window, fg="black", bg="white", width=40, height=15)
label_ATCG = Label(window, bg="white", fg="black", text="Num As=0, Num Ts=0, Num Cs=0, Num Gs=0")


def clear_field():
    input_field.delete(1.0, END)
    label_ATCG.config(text="Num As=0, Num Ts=0, Num Cs=0, Num Gs=0")


def count_letters():
    num_a = str(input_field.get("1.0", END).count('A'))
    num_t = str(input_field.get("1.0", END).count('T'))
    num_c = str(input_field.get("1.0", END).count('C'))
    num_g = str(input_field.get("1.0", END).count('G'))
    label_ATCG.config(text="Num As=" + num_a + ", Num Ts=" + num_t + ", Num Cs=" + num_c + ", Num Gs=" + num_g)


def close_window():
    window.destroy()


clear = Button(window, width=20, text="Clear", bg="orange", command=clear_field)
count = Button(window, width=20, text="Count", bg="green", command=count_letters)
goodbye = Button(window, width=20, text="Goodbye", bg="red", fg="black", command=close_window)

input_field.pack()
label_ATCG.pack()
clear.pack()
count.pack()
goodbye.pack()
window.mainloop()
