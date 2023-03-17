import os


class HardwareSystem:  # Реалізація функціоналу підсистеми Апаратного Забезпечення
    def __init__(self):
        self.current_action = 'waiting any action with Hardware SubSystem'

    def input(self):
        self.current_action = 'input these data in system'

    def storage(self):
        self.current_action = 'storage our data in HDD or SDD'

    def processing(self):
        self.current_action = 'processing all data'

    def output(self):
        self.current_action = 'output data'

    pass


class SoftwareSystem:  # Реалізація функціоналу підсистеми Програмного Забезпечення
    def __init__(self):
        self.current_action = 'waiting any action with Software SubSystem'

    def use_apps(self, application, filepath):
        self.current_action = 'use applications for your specific work'
        os.system(application + f" {filepath}")

    pass


class InfoResourceSystem:  # Реалізація функціоналу підсистеми Інформаційних ресурсів
    def __init__(self, path):
        self.current_action = 'waiting any action with Info-Resource SubSystem'

        self.path = path
        # self.files = os.listdir(self.path)
        self.software_system = SoftwareSystem()

    def create(self, filename):
        try:
            self.current_action = 'create any type of file'
            open(self.path + filename, 'xt')
        except FileExistsError:
            print("There is already a file with the same name in this location")

    def rename(self, filename):
        try:
            self.current_action = 'rename any file'
            os.rename(self.path + filename, self.path + input('New name of the file: '))
        except FileNotFoundError:
            print(f"You cannot rename file '{filename}' because it doesn't exist")

    def open(self, application, filepath):
        try:
            self.current_action = 'open this file with any application'
            self.software_system.use_apps(application, filepath)
        except FileNotFoundError:
            print("There is no such a file in this directory")

    def remove(self, filename):
        try:
            self.current_action = 'remove file from the directory'
            os.remove(self.path + filename)
        except FileNotFoundError:
            print("There is no such a file in this directory")

    pass


class Users:  # Система користувачів Комп`ютера
    """Class that describes Users."""

    def __init__(self, username, password, admin_permission=False):
        self.username = username
        self.password = password
        self.admin_permission = admin_permission

    pass


class Computer:  # Основна система Комп`ютер та реалізація її функцій
    """Class that describes Computer."""

    def __init__(self, users, computer_type, os_type, display_size, path):
        self.admin = [user for user in users if user.admin_permission]
        self.users = users
        self.computer_type = computer_type
        self.os_type = os_type
        self.display_size = display_size
        self.path = path

        self.current_user = None
        self.current_action = 'waiting any action with Computer System'

        self.is_active = False
        self.hardware_system = HardwareSystem()
        self.software_subsystem = SoftwareSystem()
        self.info_resource = InfoResourceSystem(self.path)

    def start(self):
        """Turn on computer."""
        self.is_active = True

    def stop(self):
        """Turn off computer."""
        if self.is_active:
            shutdown = input("Do you wish to shutdown your computer? (yes/no): ").lower()

            if shutdown == 'no':
                pass
            else:
                os.system("shutdown /s /t 1")
        else:
            print("You cannot stop the computer because it hasn't been started yet")

    def log_in(self, username, password):

        # def check_userdata(username_check, password_check):
        #     is_name = False
        #     name_index = -1
        #     for i in range(len(self.users)):
        #         if username_check == self.users[i].username:
        #             is_name = True
        #             name_index = i
        #
        #     is_password = False
        #     password_index = -1
        #     for j in range(len(self.users)):
        #         if password_check == self.users[j].password:
        #             is_password = True
        #             password_index = j
        #     is_user = False
        #     is_admin = False
        #     if is_name and is_password and (name_index == password_index):
        #         is_user = True
        #         if self.users[name_index].admin_permission:
        #         is_admin = True
        #     return is_user, is_admin

        def check_userdata(username_check, password_check) -> tuple[bool, bool]:
            for user in self.users:
                if user.username == username_check and user.password == password_check:
                    return True, user.admin_permission
            else:
                return False, False


        """Log in system."""
        temp = Users(username, password)
        if self.is_active:
            is_valid_user, is_admin_permission = check_userdata(username, password)
            if is_valid_user:
                print(f'You have logged in as {username}')
                self.current_action = 'You have successfully logged in system with correct username and password'
                self.current_user = temp.username
                if is_admin_permission:
                    print("Congratulation!!! Everything in your hands")
            else:
                print('Incorrect username or password')
        else:
            print("You cannot log in the computer because it hasn't been started yet")

    def change_user(self):
        """Change current user."""
        if self.is_active:
            self.current_action = 'change current user on another one'
            self.log_in(input('New username: '), input('New password: '))
        else:
            print("You cannot change current user because computer hasn't been started yet")

    def data_interaction(self, action):
        """The computer can input, storage, processing, output data."""
        assert action in ('input', 'storage', 'processing', 'output'), 'Wrong action!'

        if self.is_active:
            if action == 'input':
                self.hardware_system.input()
            elif action == 'storage':
                self.hardware_system.storage()
            elif action == 'processing':
                self.hardware_system.processing()
            elif action == 'output':
                self.hardware_system.output()
        else:
            print("You cannot interact with data because computer hasn't been started yet")

    def use_apps(self, application, filename):
        """Use any program."""
        if self.is_active:
            print(self.path + filename)
            self.software_subsystem.use_apps(application, self.path + filename)
        else:
            print("You cannot open any app for using because computer hasn't been started yet")

    def file_interaction(self, action):
        """The computer can create, open, save, view files."""
        assert action in ('create', 'rename', 'open', 'remove'), 'Wrong action!'

        if self.is_active:
            if action == 'create':
                self.info_resource.create(input('Filename: '))
            elif action == 'rename':
                self.info_resource.rename(input('Filename: '))
            elif action == 'open':
                self.info_resource.open(input('Open with application: '), f"{self.path}" + input('Filename: '))
            elif action == 'remove':
                self.info_resource.remove(input('Filename: '))
        else:
            print("You cannot interact with files because computer hasn't been started yet")

    pass
