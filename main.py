from user import User
import csv
from typing import Optional

class LIBRARY(User):
    def __init__(self):
        super().__init__()

    def home(self, run: bool):
        while run:
            print('1.Admin \n2.User \n3.Exit')
            match self.get():
                case 1:
                    admin = self.admin()
                    run = True if admin == 1 else False
                case 2:
                    user = self.user()
                    run = True if user == 1 else False
                case 3:
                    run = False
                case _:
                    print('Invalid')

    def admin(self) -> Optional[int]:
        try:
            admin_id = input(f"{'Admin Id':<10}:")
            admin_pwd = int(input(f"{'Password':<10}:"))
            if admin_id == 'Librarian' and admin_pwd == 1111:
                while True:
                    print('1.Add book \n2.User detail \n3.Back')
                    match self.get():
                        case 1:
                            book = self.add_book()
                            match book:
                                case 1: print('Book already exists')
                                case 2: print('Book added successfully')
                                case _: print('Book adding failed')
                        case 2:
                            self.user_detail()
                        case 3:
                            return 1
                        case _:
                            print('Invalid')
            else:
                print('Invalid Admin Id or Password')
                return 0
        except ValueError:
            return 0

    def add_book(self) -> Optional[int]:
        try:
            count = 100
            title = input(f"{'Book Name':<13}:")
            author = input(f"{'Author Name':<13}:")
            category = input(f"{'Category':<13}:")
            status = 'available'
            self.new = True
            updated: list[list[str]] = []

            with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\Books_data.csv', 'r', newline='') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row) != 0:
                        count += 1
                    if len(row) > 1 and title.strip().lower() == row[1].strip().lower():
                        self.new = False
                    # fill missing columns to prevent IndexError
                    if len(row) < 5:
                        row += [''] * (5 - len(row))
                    updated.append([row[0], row[1], row[2], row[3], row[4]])

            if self.new:
                try:
                    with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\Books_data.csv', 'a+', newline='') as data:
                        writer = csv.writer(data)
                        writer.writerow([count, title, author, category, status])
                        return 2
                except (FileNotFoundError, PermissionError):
                    return 3
            else:
                return 1
        except (FileNotFoundError, PermissionError):
            return 3

    def user_detail(self) -> Optional[int]:
        try:
            user = 1
            uid = input(f"{'Enter User Id':<15}:")
            with open('C:\\Users\\KAMAL TAMIL\\Downloads\\Python\\Library\\User_Details.csv', 'r', newline='') as data:
                reader = csv.reader(data)
                for row in reader:
                    if len(row) != 0 and uid == row[0]:
                        print(f"{'User Id':<13}: {row[0]}\n{'User Name':<13}: {row[1]}\n{'Book status':<13}: {row[-1]}")
                        return 1
                    else:
                        user = 0
            return user
        except (ValueError, FileNotFoundError, PermissionError):
            return 0


if __name__ == '__main__':
    app: LIBRARY = LIBRARY()
    app.home(run=True)
