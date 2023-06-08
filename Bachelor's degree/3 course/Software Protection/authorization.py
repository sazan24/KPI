import os, json, re
import tkinter as tk
from tkinter import ttk, messagebox


def load_database():
    with open(filepath, "r") as fp:
        return json.load(fp)


def dump_database():
    with open(filepath, "w") as fp:
        json.dump(user_db, fp)
    return None


def create_window(root, size=None):
    for widget in root.winfo_children():
        widget.destroy()
    if size is not None:
        root.geometry(size)
    return None


def passwording(login, child, password, repeated, previous=None, action="create"):
    if action == "change": previous = previous.get()
    password = password.get()
    repeated = repeated.get()

    if (user_db[login][0] == previous or user_db[login][0] == "" or action == "create"):
        if password == repeated:
            result = check_password(login, password)
            if result[0] & result[1] & result[2]:
                user_db[login][0] = password
                dump_database()
                messagebox.showinfo("Success", f"Успішно змінено пароль для користувача [ {login} ]")
                child.destroy()
            else:
                if not result[0]:
                    result[0] = "Латинські букви"
                else:
                    result[0] = ""
                if not result[1]:
                    result[1] = "Символи кирилиці"
                else:
                    result[1] = ""
                if not result[2]:
                    result[2] = "Знаки арифметичних операцій (+-*/%)"
                else:
                    result[2] = ""
                error = f"Пароль повинен містити хоча б один символ із наступних категорій: " \
                        f"\n• {result[0]}\n• {result[1]}\n• {result[2]}"
                messagebox.showerror("Error", error)
        else:
            messagebox.showerror("Error", "Уведені паролі мають співпадати")
    else:
        messagebox.showerror("Error", "Неправильний попередній пароль")
    return None


def limitation(login, action, type, wordlist):
    login = login.get()
    if (login in user_db.keys()):
        if action == "block":
            user_db[login][2] = type
        else:
            user_db[login][3] = type
        dump_database()
        if type:
            messagebox.showinfo("Success", f"[ {login} ] був {wordlist[2]}")
        else:
            messagebox.showinfo("Success", f"[ {login} ] був {wordlist[3]}")
    else:
        messagebox.showerror("Error", "Даного користувача не знайдено")


def registration(login):
    login = login.get()
    password = ""
    if (login not in user_db.keys()):
        user_db[login] = [password, 0, False, False]
        dump_database()
        messagebox.showinfo("Success", f"Ім'я [ {login} ] було успішно додано")
    else:
        messagebox.showerror("Error", "Такий користувач уже існує")


def informing():
    messagebox.showinfo("Information",
                        "Програма розмежування повноважень користувачів на основі парольної автентифікацї.\n\n"
                        "Варіант №11. Наявність латинських букв, символів кирилиці і знаків арифметичних операцій.\n\n"
                        "=====================================\n"
                        "Інформація про автора програми: ФБ-01 Сахній Назар.\n"
                        "=====================================")
    return None


class Command:
    def __init__(self, login):
        self.login = login

    def change_password(self, root):
        child = tk.Toplevel(root)
        child.grab_set()
        child.title("Change Password")

        previous = tk.StringVar()
        tk.Label(child, text="Уведіть відповідні дані").pack()
        previous_label = tk.Label(child, fg="blue", text="Попередній пароль ↓")
        previous_label.pack(pady=5)
        previous_entry = tk.Entry(child, width=15, textvariable=previous, show="*")
        previous_entry.pack()
        previous_entry.focus()

        password = tk.StringVar()
        password_label = tk.Label(child, fg="blue", text="Новий пароль ↓")
        password_label.pack(pady=5)
        password_entry = tk.Entry(child, width=15, textvariable=password, show="*")
        password_entry.pack()

        repeated = tk.StringVar()
        repeated_label = tk.Label(child, fg="blue", text="Повторне введення ↓")
        repeated_label.pack(pady=5)
        repeated_entry = tk.Entry(child, width=15, textvariable=repeated, show="*")
        repeated_entry.pack()

        button = tk.Button(child, bg="yellow", fg="black", text="Змінити пароль", width=25,
                           command=lambda: passwording(self.login, child, password, repeated, previous, action="change"))
        button.pack(pady=5)

        button = tk.Button(child, bg="grey", fg="black", text="Назад до меню", width=15,
                           command=lambda: child.destroy())
        button.pack(pady=5)
        return None

    def view_user_list(self, root):
        child = tk.Toplevel(root)
        child.grab_set()
        child.title("View User List")
        tk.Label(child, text=f"Інформація про зареєстрованих користувачів").pack()

        style = ttk.Style(child)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background=[("!active", "black"), ("active", "white")], foreground="blue")
        style.configure("Treeview", fieldbackground="white", background="black", foreground="yellow", gridcolor="grey")

        table = ttk.Treeview(child)
        table["columns"] = ("Login", "Password", "Blocked", "Restricted")

        table.column("#0", width=0, stretch="no")
        table.heading("#0", text="")

        table.column("Login", anchor="center", width=160)
        table.heading("Login", text="Login ▼▼▼", anchor="center")

        table.column("Password", anchor="center", width=160)
        table.heading("Password", text="Password ▼▼▼", anchor="center")

        table.column("Blocked", anchor="center", width=80)
        table.heading("Blocked", text="Blocked?", anchor="center")

        table.column("Restricted", anchor="center", width=80)
        table.heading("Restricted", text="Restricted?", anchor="center")

        i = 0
        for login in user_db.keys():
            table.insert(parent="", index="end", iid=i, text="",
                         values=(login, user_db[login][0], user_db[login][2], user_db[login][3]))
            i += 1
        table.pack()

        login_button = tk.Button(child, bg="grey", fg="black", text="Назад до меню", width=15,
                                 command=lambda: child.destroy())
        login_button.pack(pady=10)
        return None

    def block_or_restrict(self, root, action):
        block = ["Заблокувати", "Розблокувати", "заблкований", "розблокований", "Block/Unblock"]
        restrict = ["Обмежити", "Розмежити", "обмежений", "розмежений", "Restrict/Unrestrict"]
        if action == "block":
            wordlist = block
        else:
            wordlist = restrict

        child = tk.Toplevel(root)
        child.grab_set()
        child.title(f"{wordlist[4]} Menu")
        tk.Label(child, text=f"{wordlist[0]}/{wordlist[1]}\nнаступного користувача").pack()

        login = tk.StringVar()
        login_entry = tk.Entry(child, width=15, textvariable=login)
        login_entry.pack()
        login_entry.focus()

        button = tk.Button(child, bg="black", fg="yellow", text=wordlist[0], width=25,
                           command=lambda: limitation(login, action, True, wordlist))
        button.pack(pady=5)

        button = tk.Button(child, bg="yellow", fg="black", text=wordlist[1], width=25,
                           command=lambda: limitation(login, action, False, wordlist))
        button.pack(pady=5)

        button = tk.Button(child, bg="grey", fg="black", text="Назад до меню", width=15,
                           command=lambda: child.destroy())
        button.pack(pady=5)
        return None

    def add_user(self, root):
        child = tk.Toplevel(root)
        child.grab_set()
        child.title("Add User")
        tk.Label(child, text=f"Щоби додати нового користувача,\nвведіть відповідне унікальне ім'я").pack()

        login = tk.StringVar()
        login_entry = tk.Entry(child, width=15, textvariable=login)
        login_entry.pack()
        login_entry.focus()

        button = tk.Button(child, bg="yellow", fg="black", text="Створити нового користувача", width=25,
                           command=lambda: registration(login))
        button.pack(pady=5)

        button = tk.Button(child, bg="grey", fg="black", text="Назад до меню", width=15,
                           command=lambda: child.destroy())
        button.pack(pady=5)
        return None


def check_password(login, password):
    result = [True, True, True]
    if user_db[login][3]:
        if re.search("[a-zA-Z]", password) is None:
            result[0] = False
        if re.search("[а-яА-Я]", password) is None:
            result[1] = False
        if re.search("[+\-*/%]", password) is None:
            result[2] = False
    return result


def check_user(login, password, password_entry):
    login = login.get()
    password = password.get()
    if login in user_db.keys():
        if user_db[login][2]:
            messagebox.showerror("Error", "На жаль, цей користувач заблокований")
        elif user_db[login][0] == "":
            USER = Command(login)
            messagebox.showinfo("Success", f"Вітаємо новоствореного користувача [ {login} ]")

            child = tk.Toplevel(root)
            child.grab_set()
            child.title("First Login")
            tk.Label(child, fg="black", text=f"Завершіть реєстрацію користувача [ {login} ]").pack()
            tk.Label(child, fg="black", text=f"Будь ласка, створіть пароль").pack()

            password = tk.StringVar()
            password_label = tk.Label(child, fg="blue", text="Придумайте пароль ↓")
            password_label.pack(pady=10)
            password_entry = tk.Entry(child, width=25, textvariable=password, show="*")
            password_entry.pack()

            repeated = tk.StringVar()
            repeated_label = tk.Label(child, fg="blue", text="Повторне введення ↓")
            repeated_label.pack(pady=10)

            repeated_entry = tk.Entry(child, width=25, textvariable=repeated, show="*")
            repeated_entry.pack()

            button = tk.Button(child, bg="yellow", fg="black", text="Зареєструватися", width=25,
                               command=lambda: passwording(login, child, password, repeated))
            button.pack(pady=5)

            button = tk.Button(child, bg="grey", fg="black", text="Завершити роботу", width=15,
                               command=lambda: sign_in(child))
            button.pack(pady=5)
        elif user_db[login][0] == password:
            if login == "ADMIN":
                USER = Command(login)
                create_window(root, "250x360")
                root.title("Admin Menu")
                tk.Label(root, bg="black", fg="white", text=f"Ви увійшли в систему під іменем [ {login} ]").pack()

                button = tk.Button(root, bg="yellow", fg="black", text="Зміна пароля адміністратора", width=30,
                                   command=lambda: USER.change_password(root))
                button.pack(pady=15)

                button = tk.Button(root, bg="yellow", fg="black", text="Перегляд списку користувачів", width=30,
                                   command=lambda: USER.view_user_list(root))
                button.pack(pady=15)

                button = tk.Button(root, bg="yellow", fg="black", text="Блокування певного користувача", width=30,
                                   command=lambda: USER.block_or_restrict(root, action="block"))
                button.pack(pady=15)

                button = tk.Button(root, bg="yellow", fg="black", text="Обмеження при зміні паролю", width=30,
                                   command=lambda: USER.block_or_restrict(root, action="restrict"))
                button.pack(pady=15)

                button = tk.Button(root, bg="yellow", fg="black", text="Додавання унікального імені", width=30,
                                   command=lambda: USER.add_user(root))
                button.pack(pady=15)

                button = tk.Button(root, bg="grey", fg="black", text="Завершити роботу", width=15,
                                   command=lambda: sign_in(root, exit=True))
                button.pack(pady=15)
            else:
                USER = Command(login)
                create_window(root, "250x120")
                root.title("User Menu")
                tk.Label(root, bg="black", fg="white", text=f"Ви увійшли в систему під іменем [ {login} ]").pack()

                button = tk.Button(root, bg="yellow", fg="black", text="Зміна особистого пароля", width=30,
                                   command=lambda: USER.change_password(root))
                button.pack(pady=10)

                button = tk.Button(root, bg="grey", fg="black", text="Завершити роботу", width=15,
                                   command=lambda: sign_in(root, exit=True))
                button.pack(pady=10)
            user_db[login][1] = 0
            dump_database()
        else:
            user_db[login][1] += 1
            dump_database()
            messagebox.showerror("Error", f"Неправильно введений пароль.\nЗалишилось {3 - user_db[login][1]} із 3 спроби")
            password_entry.delete(0, tk.END)
            if user_db[login][1] == 3:
                user_db[login][1] = 0
                dump_database()
                root.destroy()
    else:
        messagebox.showerror("Error", "Помилка при введенні імені користувача")
    return None


def sign_in(root, exit=False):
    create_window(root, "310x155") if exit else root.geometry("310x135")
    root.title("Sign In")

    menu_bar = tk.Menu(root)
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Довідка", menu=help_menu)
    help_menu.add_command(label="Про програму", command=lambda: informing())
    root.config(menu=menu_bar)

    status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    status_bar.config(text="Програма очікує на ввід своїх даних від користувача.....")

    login_label = tk.Label(root, text="Login >>> ", background="black", foreground="white")
    login_label.place(x=10, y=10)
    login = tk.StringVar()
    login_entry = tk.Entry(root, width=36, textvariable=login)
    login_entry.place(x=80, y=10)

    password_label = tk.Label(root, text="Password >", background="black", foreground="white")
    password_label.place(x=10, y=45)
    password = tk.StringVar()
    password_entry = tk.Entry(root, width=36, textvariable=password, show="*")
    password_entry.place(x=80, y=45)

    button = tk.Button(root, text="Зареєструватися", width=18, bg="yellow", fg="black",
                       command=lambda: check_user(login, password, password_entry))
    button.place(x=14, y=80)

    button = tk.Button(root, text="Довідка про програму", width=18, bg="grey", fg="black",
                       command=lambda: informing())
    button.place(x=165, y=80)
    return None


user_db = {"ADMIN": ["", 0, False, False]}
filepath = "./database.json"
if os.path.isfile(filepath):
    user_db = load_database()
else:
    dump_database()

root = tk.Tk()
root.configure(background="black")

sign_in(root)

root.mainloop()
