# import some required libraries
import csv
from typing import Optional

class User:
    def __init__(self):
        self.flag = int()
        self.new = True

    # Get input from user
    def get(self):
        try:
            option = int(input(f"{'Choice':<8}:"))
            return option
        except ValueError:
            return False

    # User status
    def user(self) -> Optional[int]:
        try:
            run = True
            while run:
                print('1.Signup \n2.Login \n3.Back')
                match User.get(self):
                    case 1:
                        signup = self.signup()
                        match signup:
                            case 1: print('User id already exist')
                            case 2: print('Signup successfully')
                            case 3: print('Something went wrong1')
                            case 4: print('Something went wrong2')
                            case _: print('Something went wrong3')
                    case 2:
                        uid = input(f"{'User id':<10}:")
                        pwd = int(input(f"{'Password':<10}:"))
                        login = self.login(pwd=pwd, id=uid)
                        match login:
                            case 1: print('Invalid Id')
                            case 2: print('Invalid Password')
                            case 3:
                                bookname = input(f"{'Book Name':<10}:")
                                entry = self.book(bookname=bookname)
                                match entry:
                                    case 1: print('The book is not available')
                                    case 2: print('The book does not exist')
                                    case 3: self.user_update(uid); print('Book entry successful')
                                    case _: print('Book entry failed')
                            case _: print('Something went wrong')
                    case 3: return 1
                    case _: run = True
        except ValueError:
            return 0

    # Signup for new user
    def signup(self) -> Optional[int]:
        try:
            user_name = str(input(f"{'User name':<10}:"))
            mobile = int(input(f"{'Mobile':<10}:"))
            if self.duplicate(mobile): return 1
            stored = self.store(user_name=user_name, mobile=mobile)
            if stored == 1: return 2
            elif stored == 2: return 3
            else: return 4
        except ValueError:
            return 0

    # Store the user data
    def store(self, user_name: str, mobile: int) -> Optional[int]:
        try:
            count = 0
            book_status = "None"
            with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv", 'r') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row) != 0: count += 1
                user_id = user_name + str(count)
                user_data = [user_id, user_name, mobile, book_status]
            try:
                with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv", 'a+') as data:
                    writer = csv.writer(data)
                    writer.writerow(user_data)
                    print(f"{'Your Id is':<15} {user_id}")
                return 1
            except (ValueError, FileNotFoundError, PermissionError):
                return 2
        except (ValueError, FileNotFoundError, PermissionError):
            return 0

    # Login for authenticate user
    def login(self, pwd: int, id: str) -> Optional[int]:
        try:
            with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv", 'r', newline='') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row) < 3: continue
                    if id == row[0]:
                        if str(pwd) == row[2]: return 3
                        else: return 2
                    else: self.flag = 1
                return self.flag
        except (ValueError, FileNotFoundError, PermissionError):
            return 0

    # Check duplicate user
    def duplicate(self, is_dup: int) -> Optional[int]:
        try:
            with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv", 'r') as data:
                reader = csv.reader(data)
                for row in reader:
                    if str(is_dup) in row: return 1
            return 0
        except (FileNotFoundError, PermissionError):
            return 0

    # Check book availability and issue
    def book(self, bookname: str) -> Optional[int]:
        try:
            issued = False
            updated: list[list[str]] = []
            with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\Books_data.csv", 'r', newline='') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row) < 2: continue
                    if bookname.strip().lower() == row[1].strip().lower():
                        if row[-1].strip().lower() == 'available':
                            row[-1] = 'issued'
                            issued = True
                        else:
                            return 1
                    # Safe append to prevent IndexError
                    if len(row) < 5:
                        row += ['']*(5 - len(row))
                    updated.append([row[0], row[1], row[2], row[3], row[4]])
            if issued:
                try:
                    with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\Books_data.csv", 'w', newline='') as data:
                        writer = csv.writer(data)
                        writer.writerows(updated)
                        return 3
                except (FileNotFoundError, PermissionError):
                    return 0
            else:
                return 2
        except (FileNotFoundError, PermissionError):
            return 0

    # Update user's book status
    def user_update(self, uid: str) -> Optional[int]:
        try:
            updated: list[list[str]] = []
            with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv", 'r') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row) < 2: continue
                    if uid == row[0]:
                        row[-1] = 'have book'
                    updated.append([row[0], row[1], row[2], row[3]])
            try:
                with open("C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv", 'w', newline='') as data:
                    writer = csv.writer(data)
                    writer.writerows(updated)
            except (FileNotFoundError, PermissionError):
                return 0
        except (FileNotFoundError, PermissionError):
            return 0
