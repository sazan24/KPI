import os, ctypes, win32api, psutil, pathlib
import winreg, hashlib
import tkinter as tk
from tkinter import messagebox


def install_program():
    # Get user and system information
    username = os.environ["USERNAME"]  # `t-1000` (echo %USERNAME%)
    computername = os.environ["COMPUTERNAME"]  # `DESKTOP-DRI0PBB` (echo %COMPUTERNAME%)
    windows_path = os.environ["WINDIR"]  # `C:\Windows` (echo %WINDIR%)
    system_path = os.environ["SYSTEMROOT"]  # `C:\Windows` (echo %SYSTEMROOT%)

    # Get information about peripheral equipment
    user32 = ctypes.windll.user32
    keyboard_type = user32.GetKeyboardType(0)  # `7`: USB keyboard
    keyboard_subtype = user32.GetKeyboardType(1)  # `0`: NONE (Subtype of the keyboard is not defined)
    screen_height = user32.GetSystemMetrics(1)  # `864`: The height of the primary display monitor in pixels

    # Get some information about the corresponding disk
    install_dir = install_dir_entry.get()
    memory_size = psutil._common.bytes2human(psutil.disk_usage(install_dir).total)  # `!` (476.3G or 931.5G)
    program_drive = os.path.splitdrive(install_dir)[0]  # `!` (C: or D:)

    # Write 'crypto_improved_authorization.py' file to the specified directory
    src_path = os.path.join(os.getcwd(), "crypto_improved_authorization.py")
    dst_path = os.path.join(install_dir, "crypto_improved_authorization.py")
    os.makedirs(install_dir, exist_ok=True)
    os.system(f'copy "{src_path}" "{dst_path}"')

    # Create a hash of user and system information
    data = f"{username}-{computername}-{windows_path}-{system_path}-" \
           f"{keyboard_type}-{keyboard_subtype}-{screen_height}-" \
           f"{memory_size}-{program_drive}"
    data_hash = hashlib.sha256(data.encode()).hexdigest()

    # Get user signature from input
    signature = signature_entry.get()

    # Write the hash and signature to the registry
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software")
    app_key = winreg.CreateKey(key, "Sakhnii")
    winreg.SetValueEx(app_key, "Signature", 0, winreg.REG_SZ, f"{signature}-{data_hash}")


def informing():
    messagebox.showinfo("Information",
                        "Програма-інсталятор, що забезпечує захист додатків від несанкціонованого використання і копіювання.\n\n"
                        "Зібрана про комп'ютер інформація включає в себе наступне (Варіант №11) ▼▼▼\n"
                        "– ім'я користувача;\n"
                        "– ім'я комп'ютера;\n"
                        "– шлях до папки з ОС Windows;\n"
                        "– шлях до папки з системними файлами ОС Windows;\n"
                        "– тип і підтип клавіатури;\n"
                        "– висота екрану;\n"
                        "– об’єм пам’яті;\n"
                        "– мітка тому, на якому встановлена програма.\n\n"
                        "=====================================\n"
                        "Інформація про автора програми: ФБ-01 Сахній Назар.\n"
                        "=====================================")
    return None


# Create a tkinter window
root = tk.Tk()
root.title("Program Installation")
root.geometry("520x155")

# Create a menu bar wuth help command
menu_bar = tk.Menu(root)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Довідка", menu=help_menu)
help_menu.add_command(label="Про програму", command=informing)
root.config(menu=menu_bar)

# Create a status bar
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
status_bar.config(text="Інсталятор очікує на ввід відповідної папки для установки й особистого ключа користувача...")

# Create a label and entry widget for the installation directory
install_dir_label = tk.Label(root, text="Папка для установки захищеної програми:", background="black", foreground="white")
install_dir_label.place(x=10, y=10)
install_dir = tk.StringVar()
install_dir_entry = tk.Entry(root, width=40)
install_dir_entry.place(x=265, y=10)

# Create a label and entry widget for the user signature
signature_label = tk.Label(root, text="Особистий ключ користувача програми:", background="black", foreground="white")
signature_label.place(x=10, y=45)
signature = tk.StringVar()
signature_entry = tk.Entry(root, width=40)
signature_entry.place(x=265, y=45)

# Create the "Інсталювати" button
install_button = tk.Button(root, text="Інсталювати", width=54, height=2, bg="yellow", fg="black", command=install_program)
install_button.place(x=10, y=80)

button = tk.Button(root, text="Довідка\nпро програму", width=12, height=2, bg="grey", fg="black", command=informing)
button.place(x=415, y=80)

# Start the main event loop
root.mainloop()
