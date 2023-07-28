import json
import os
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.geometry('600x300+600+200')
root.resizable(False, False)

root.iconbitmap(default=r"C:\Users\LENOVO\PycharmProjects\pythonProject3\New folder\open-book.ico")

image = Image.open("qa.png")
image = image.resize((20, 20))
photo = ImageTk.PhotoImage(image)

image3 = Image.open("Search.png")
image3 = image3.resize((40, 40))
photo3 = ImageTk.PhotoImage(image3)

image2 = Image.open("Profile.png")
image2 = image2.resize((70, 70))
photo2 = ImageTk.PhotoImage(image2)

image1 = Image.open("imd.png")
image1 = image1.resize((400, 350))
photo1 = ImageTk.PhotoImage(image1)

var = IntVar()
var2 = IntVar()
var3 = IntVar()


class Person:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password

    def set_login(self, item):
        self.__login = item

    def set_password(self, item):
        self.__password = item


class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_name(self, item):
        self.__name = item

    def set_price(self, item):
        self.__price = item


class Products:
    def __init__(self, snack, price1):
        self.__snack = snack
        self.__price1 = price1

    def get_snack(self):
        return self.__snack

    def get_price1(self):
        return self.__price1

    def set_snack(self, item):
        self.__snack = item

    def set_price(self, item):
        self.__price1 = item


def save_product_data(products):
    product_list = []
    for product in products:
        data = {
            "snack": product.get_snack(),
            "price1": product.get_price1(),
        }
        product_list.append(data)
    with open("product_data.json", "w") as f:
        json.dump(product_list, f)


def load_product_data():
    if not os.path.exists("product_data.json"):
        return []
    with open("product_data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    product_list = []
    for item in data:
        product = Products(
            item["snack"],
            item["price1"],
        )
        product_list.append(product)
    return product_list


def add_product():
    snack = add_name1.get()
    price1 = add_price3.get()
    product = Products(snack, price1)

    existing_products = load_product_data()
    for products in existing_products:
        if products.get_snack() == snack:
            showinfo('GUI PYTHON', 'This product already exists')
            add_name1.delete(0, END)
            add_price3.delete(0, END)
            return
    else:
        existing_products.append(product)
        save_product_data(existing_products)
        add_name1.delete(0, END)
        add_price3.delete(0, END)
        showinfo('GUI PYTHON', 'Product added successfully')
        frame_add_snack.place_forget()
        root.geometry('650x600+210+50')
        frame_admin.place(relx=0, rely=0)


def save_book_data(books):
    book_list = []
    for book in books:
        data = {
            "name": book.get_name(),
            "price": book.get_price(),
        }
        book_list.append(data)
    with open("book_data.json", "w") as f:
        json.dump(book_list, f)


def load_book_data():
    if not os.path.exists("book_data.json"):
        return []
    with open("book_data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    book_list = []
    for item in data:
        book = Book(
            item["name"],
            item["price"],
        )
        book_list.append(book)
    return book_list


def add_book():
    name = add_name.get()
    price = add_price.get()
    book = Book(name, price)

    existing_books = load_book_data()
    for books in existing_books:
        if books.get_name() == name:
            showinfo('GUI PYTHON', 'This book already exists')
            return
    else:
        existing_books.append(book)
        save_book_data(existing_books)
        add_name.delete(0, END)
        add_price.delete(0, END)
        showinfo('GUI PYTHON', 'Book added successfully')
        frame_add_book.place_forget()
        root.geometry('650x600+210+50')
        frame_admin.place(relx=0, rely=0)


def save_user_data(users):
    user_list = []
    for info in users:
        data = {
            "login": info.get_login(),
            "password": info.get_password(),
        }
        user_list.append(data)
    with open("user_data.json", "w") as f:
        json.dump(user_list, f)


def SaveRegInfo():
    email1 = entry_mail.get()
    password1 = entry_pass1.get()

    existing_users = load_user_data()

    for user in existing_users:
        if user.get_login() == email1:
            showinfo('GUI PYTHON', 'This email already exists')
            return

    person = Person(email1, password1)

    existing_users.append(person)

    save_user_data(existing_users)
    showinfo('GUI PYTHON', 'You created new account')


def load_user_data():
    if not os.path.exists("user_data.json"):
        return []
    with open("user_data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    person_list = []
    for item in data:
        person = Person(
            item["login"],
            item["password"],
        )
        person_list.append(person)
    return person_list


def create(event=NONE):
    email = entry_mail.get()
    username = entry_name.get()
    password = entry_pass.get()
    password1 = entry_pass1.get()

    if '@gmail.com' not in email:
        showerror("GUI PYTHON", "Incorrect E-mail")
    elif len(password) < 8 or len(password1) < 8:
        showerror("GUI PYTHON", "Use at least 8 characters in the password")
    elif password != password1:
        showerror('GUI PYTHON', 'Passwords must be identical')
    else:

        entry_mail.delete(0, END)
        entry_pass.delete(0, END)
        entry_pass1.delete(0, END)

        switch_to_login()


def show_pass():
    if var.get() == 1:
        entry_pass['show'] = ''
    else:
        entry_pass['show'] = '*'


def show_pass1():
    if var2.get() == 1:
        entry_pass1['show'] = ''
    else:
        entry_pass1['show'] = '*'


def show_pass2():
    if var3.get() == 1:
        lg_pass_entry['show'] = ''
    else:
        lg_pass_entry['show'] = '*'


def exit():
    root.destroy()


def switch_to_registration():
    frame_menu.place_forget()
    root.geometry('500x600+210+50')
    frame_regis.place(relx=0, rely=0)


def switch_to_login1():
    frame_regis.place_forget()
    root.geometry('450x300+210+50')
    frame_login.place(relx=0, rely=0)


def switch_to_products_info():
    frame_admin.place_forget()
    root.geometry('400x500+210+50')
    frame_products.place(relx=0, rely=0)


def back_to_menu():
    frame_regis.place_forget()
    root.geometry('600x300+210+50')
    frame_menu.place(relx=0, rely=0)


def back_to_menu_from_admin_login():
    frame_admin_login.place_forget()
    root.geometry('600x300+210+50')
    frame_menu.place(relx=0, rely=0)


def back_to_reg():
    frame_login.place_forget()
    root.geometry('500x600+210+50')
    frame_regis.place(relx=0, rely=0)
    back_to_menu()


def switch_to_shop(event=None):
    persons = load_user_data()
    a = lg_name_entry.get()
    b = lg_pass_entry.get()
    for person in persons:
        if a == person.get_login() and b == person.get_password():
            showinfo("GUI PYTHON", "You have logged in successfully")
            frame_login.place_forget()
            root.geometry('1000x700+210+50')
            frame_user_acc.place(relx=0, rely=0)
            profile()
            lg_name_entry.delete(0, END)
            lg_pass_entry.delete(0, END)
            return
    else:
        showerror('GUI PYTHON', 'Invalid login or password')


def switch_to_admin(event=None):
    a = entr_ad_login.get()
    b = entr_ad_pass.get()
    if a == "admin" and b == "admin123":
        showinfo("GUI PYTHON", "you have entered to admin menu")
        frame_admin_login.place_forget()
        root.geometry('650x600+210+50')
        frame_admin.place(relx=0, rely=0)
    else:
        showerror('GUI PYTHON', 'Invalid login or password')


def switch_to_login():
    frame_menu.place_forget()
    root.geometry('450x300+210+50')
    frame_login.place(relx=0, rely=0)


def switch_to_settings():
    frame_admin.place_forget()
    root.geometry('300x400+210+50')
    frame_set.place(relx=0, rely=0)


var1 = IntVar()


def change_theme():
    color = var1.get()
    if color == 0:
        return True
    elif color == 1:
        add_price1['bg'] = 'white'
        lbl_add['bg'] = 'white'
        rad_but4['bg'] = 'white'
        rad_but3['bg'] = 'white'
        rad_but2['bg'] = 'white'
        rad_but4['fg'] = 'black'
        rad_but3['fg'] = 'black'
        rad_but2['fg'] = 'black'
        frame_add_snack['bg'] = 'white'
        frame_admin['bg'] = 'white'
        frame_set['bg'] = 'white'
        frame_users['bg'] = 'white'
        frame_add_book['bg'] = 'white'
        frame_books['bg'] = 'white'
        frame_option['bg'] = 'white'
        frame_users['bg'] = 'white'
        frame_products['bg'] = 'white'
        frame_product_price['bg'] = 'white'
        frame_book_price['bg'] = 'white'
        frame_password['bg'] = 'white'
        lbl_add1['bg'] = 'white'
        add_password1['bg'] = 'white'
        lbl_add4['bg'] = 'white'
        lbl_add3['bg'] = 'white'
        rad_but1['bg'] = 'white'
        rad_but['bg'] = 'white'
        bg_srift['bg'] = 'white'
        bg_name['bg'] = 'white'
        lbl_snack['bg'] = 'white'
        add_price2['bg'] = 'white'
    else:
        lbl_add['bg'] = 'black'
        add_price1['bg'] = 'black'
        lbl_snack['bg'] = 'black'
        rad_but3['bg'] = 'black'
        add_price2['bg'] = 'black'
        rad_but4['bg'] = 'black'
        rad_but2['bg'] = 'black'
        rad_but4['fg'] = 'white'
        rad_but3['fg'] = 'white'
        rad_but2['fg'] = 'white'
        frame_admin['bg'] = 'black'
        frame_set['bg'] = 'black'
        frame_users['bg'] = 'black'
        frame_add_snack['bg'] = 'black'
        frame_add_book['bg'] = 'black'
        frame_books['bg'] = 'black'
        frame_products['bg'] = 'black'
        frame_option['bg'] = 'black'
        lbl_add3['bg'] = 'black'
        add_password1['bg'] = 'black'
        frame_product_price['bg'] = 'black'
        lbl_add4['bg'] = 'black'
        frame_book_price['bg'] = 'black'
        frame_password['bg'] = 'black'
        lbl_add1['bg'] = 'black'
        frame_users['bg'] = 'black'
        rad_but1['bg'] = 'black'
        rad_but['bg'] = 'black'
        bg_srift['bg'] = 'black'
        bg_name['bg'] = 'black'


def change_font():
    style = com_box.get()
    numbers = com_box1.get()
    color1 = entr_color.get()
    lbl_menu.config(font=(style, numbers), fg=color1)
    lbl_option.config(font=(style, numbers), fg=color1)
    lbl_sign.config(font=(style, numbers), fg=color1)
    lbl_mail.config(font=(style, numbers), fg=color1)
    lbl_pass.config(font=(style, numbers), fg=color1)
    lbl_pass1.config(font=(style, numbers), fg=color1)
    lbl_name.config(font=(style, numbers), fg=color1)
    lg_login.config(font=(style, numbers), fg=color1)
    lg_name.config(font=(style, numbers), fg=color1)
    lg_pass_label.config(font=(style, numbers), fg=color1)


def switch_to_admin_login():
    frame_menu.place_forget()
    root.geometry('300x250+210+50')
    frame_admin_login.place(relx=0, rely=0)


def back_to_shop_from_set():
    frame_set.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def back_to_menu_from_admin():
    frame_admin.place_forget()
    root.geometry('600x300+210+50')
    frame_menu.place(relx=0, rely=0)


def switch_options():
    frame_admin.place_forget()
    root.geometry('300x200+210+50')
    frame_option.place(relx=0, rely=0)


def switch_to_users():
    frame_admin.place_forget()
    root.geometry('400x500+210+50')
    frame_users.place(relx=0, rely=0)


def options():
    option = var1.get()
    if option == 1:
        frame_option.place_forget()
        root.geometry('500x600+210+50')
        frame_regis.place(relx=0, rely=0)
        btn_create['state'] = DISABLED
    elif option == 2:
        frame_option.place_forget()
        root.geometry('400x300+210+50')
        frame_add_book.place(relx=0, rely=0)
    else:
        frame_option.place_forget()
        root.geometry('400x300+210+50')
        frame_add_snack.place(relx=0, rely=0)


def switch_to_wallet():
    frame_user_acc.place_forget()
    root.geometry('300x250')
    frame_wallet.place(relx=0, rely=0)


def back_to_admin():
    frame_users.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def switch_to_book():
    frame_admin.place_forget()
    root.geometry('400x500+210+50')
    frame_books.place(relx=0, rely=0)


def back_to_admin_from_book():
    frame_books.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def back_to_admin_from_products():
    frame_products.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def edit():
    frame_users.place_forget()
    root.geometry('400x450+210+50')
    frame_password.place(relx=0, rely=0)


def edit_price():
    frame_products.place_forget()
    root.geometry('400x450+210+50')
    frame_product_price.place(relx=0, rely=0)


def edit_book_price():
    frame_books.place_forget()
    root.geometry('400x450+210+50')
    frame_book_price.place(relx=0, rely=0)


def confirm_book_price():
    selected_login3 = lst_box_books2.get(lst_box_books2.curselection())
    add_new_price1 = add_book_price.get()

    with open("book_data.json", "r") as f:
        data = json.load(f)
        for user in data:
            if user['name'] == selected_login3:
                user['price'] = add_new_price1

    with open("book_data.json", "w") as f:
        json.dump(data, f)
    showinfo('Success', 'Price updated successfully!')
    frame_book_price.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def confirm_price():
    selected_login2 = lst_box_users2.get(lst_box_users2.curselection())
    add_new_price = add_price7.get()

    with open("product_data.json", "r") as f:
        data = json.load(f)
        for user in data:
            if user['snack'] == selected_login2:
                user['price1'] = add_new_price

    with open("product_data.json", "w") as f:
        json.dump(data, f)

    showinfo('Success', 'Price updated successfully!')
    frame_product_price.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def add_to_card1():
    global products_to_buy
    selected_index = lst_box_books.curselection()
    if selected_index:
        selected_book = lst_box_books.get(selected_index)
        products_to_buy.append(selected_book)
        lst_box_books.delete(selected_index)
        com_box2['values'] = products_to_buy


def add_to_card2():
    global products_to_buy
    selected_index1 = lst_box_products.curselection()
    if selected_index1:
        selected_product = lst_box_products.get(selected_index1)
        products_to_buy.append(selected_product)
        lst_box_products.delete(selected_index1)
        com_box2['values'] = products_to_buy


def back_to_admin_from_option():
    frame_option.place_forget()
    root.geometry('650x600+210+50')
    frame_admin.place(relx=0, rely=0)


def select():
    a = com_box2.get()
    b = int(spin_box.get())
    money = entr_amount.get()
    with open("product_data.json", "r") as f:
        data = json.load(f)
    with open("book_data.json", "r") as f:
        data1 = json.load(f)
        for item in data:
            if a == item['snack']:
                price = item['price1']
                total = b * float(price)
                result = askyesno(title='GUI Python', message=f'продукт {b}*{a} = {total} AZN\n Желаете купить?')
                if float(money) >= float(total):
                    if result:
                        money = int(money) - int(total)
                        entr_amount.delete(0, END)
                        entr_amount.insert(0, money)
                        entr_wallet_info['text'] = f'Wallet balance : {money} AZN'
                        showinfo('GUI Python', f'У ВАС ОСТАЛОСЬ = {money} AZN на счету')

                    else:
                        showinfo("GUI Python", "Операция отменена")
                else:
                    showerror("GUI Python", "У вас недостаточно денег")
        for item1 in data1:
            if a == item1['name']:
                price1 = item1['price']
                result = askyesno(title='GUI Python', message=f'книга {a} = {price1} AZN\n Желаете купить?')
                if float(money) >= float(price1):
                    if result:
                        money = float(money) - float(price1)
                        entr_amount.delete(0, END)
                        entr_amount.insert(0, money)
                        entr_wallet_info['text'] = f'Wallet balance : {money} AZN'
                        showinfo('GUI Python', f'У ВАС ОСТАЛОСЬ = {money} AZN на счету')
                    else:
                        showinfo("GUI Python", "Операция отменена")
                else:
                    showerror("GUI Python", "У вас недостаточно денег")


def confirm():
    selected_login = lst_box_users1.get(lst_box_users1.curselection())
    new_password = add_password2.get()
    new_password2 = add_password.get()
    if new_password2 == new_password:
        with open("user_data.json", "r") as f:
            data = json.load(f)
            for user in data:
                if user['login'] == selected_login:
                    user['password'] = new_password

        with open("user_data.json", "w") as f:
            json.dump(data, f)

        showinfo('GUI Python', 'Password updated successfully!')
        frame_password.place_forget()
        root.geometry('650x600+210+50')
        frame_admin.place(relx=0, rely=0)
    else:
        showerror('GUI Python', 'Passwords must be identical!')


def add_to_list_box():
    with open("user_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            lst_box.insert(END, item["login"])


def is_valid_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def confirm_wallet(event=None):
    money = entr_amount.get()
    if is_valid_number(money):
        entr_wallet_info['text'] = f'Wallet balance : {money} AZN'
        showinfo('GUI Python', 'You updated your wallet balance')
        frame_wallet.place_forget()
        root.geometry('1000x700+210+50')
        frame_user_acc.place(relx=0, rely=0)
    else:
        showerror('GUI Python', 'Please enter a valid number')


def search(event=None):
    simvols = entr_search.get()
    found = False

    with open("product_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            if simvols in item['snack']:
                result = item['snack']
                showinfo('GUI Python', f'Product: {result} is in list')
                found = True
                break
    with open("book_data.json", "r") as f:
        data1 = json.load(f)
        for item1 in data1:
            if simvols == item1['name']:
                result = item['name']
                showinfo('GUI Python', f'Product: {result} is in list')
                found = True
                break
    if not found:
        showerror('GUI Python', 'There is no such a product')


def profile():
    a = lg_name_entry.get()
    with open("user_data.json", "r") as f:
        data = json.load(f)
    for users in data:
        if a == users['login']:
            password = users['password']
            profile_name['text'] = f'E-mail: {a}'
            profile_password['text'] = f'Password: {password}'
            break


def delete_from_lst_box():
    select = lst_box.curselection()
    lst_box.delete(select)
    with open("user_data.json", "r") as f:
        data = json.load(f)
        del data[0]
    with open("user_data.json", "w") as f:
        json.dump(data, f)


def product_in_list():
    with open("product_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            product_info = item['snack']
            lst_box_products.insert(END, product_info)


def add_to_list_books():
    with open("book_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            book_info = f"{item['name']} = {item['price']} AZN"
            lst_box1.insert(END, book_info)


def product_list():
    with open("product_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            lst_box_users2.insert(END, item['snack'])


def edit_profile():
    frame_user_acc.place_forget()
    root.geometry('500x600+210+50')
    frame_password.place(relx=0, rely=0)


def book_list():
    with open("book_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            lst_box_books2.insert(END, item['name'])


def users_in_list():
    with open("user_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            lst_box_users1.insert(END, item['login'])


def books_in_list():
    with open("book_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            book_info = item['name']
            lst_box_books.insert(END, book_info)


def view_products():
    with open("product_data.json", "r") as f:
        data = json.load(f)
        for item in data:
            product_info1 = f"{item['snack']} = {item['price1']} AZN"
            lst_box4.insert(END, product_info1)


def back_to_menu_from_user():
    frame_user_acc.place_forget()
    root.geometry('600x300+210+50')
    frame_menu.place(relx=0, rely=0)


def delete_form_lst_products():
    select3 = lst_box4.curselection()
    lst_box4.delete(select3)
    with open("product_data.json", "r") as f:
        data = json.load(f)
        del data[0]
    with open("product_data.json", "w") as f:
        json.dump(data, f)


def delete_from_list_books():
    select1 = lst_box1.curselection()
    lst_box1.delete(select1)
    with open("book_data.json", "r") as f:
        data = json.load(f)
        del data[0]
    with open("book_data.json", "w") as f:
        json.dump(data, f)


def insert_default_text():
    lg_name_entry.insert(END, 'E-mail')
    lg_name_entry.config(fg='white')


def insert_default_text2():
    lg_pass_entry.insert(END, 'Password')
    lg_pass_entry.config(fg='white')


def on_email_entry_click1(event):
    if lg_pass_entry.get() == 'Password':
        lg_pass_entry.delete(0, END)
        lg_pass_entry.config(fg='white')


def on_email_entry_focus_out1(event):
    if lg_pass_entry.get() == '':
        insert_default_text2()


def on_email_entry_click(event):
    if lg_name_entry.get() == 'E-mail':
        lg_name_entry.delete(0, END)
        lg_name_entry.config(fg='white')


def on_email_entry_focus_out(event):
    if lg_name_entry.get() == '':
        insert_default_text()


# First Menu
frame_menu = Frame(width=600, height=300, bg="orange")
lbl_menu = Label(frame_menu, text="Welcome to Book Shop", font='Calibri 25', bg="orange")
lbl_option = Label(frame_menu, text='Please choose an option:', font='Calibri 18', bg="orange")
btn_question = Button(frame_menu, text="Already have an account?", width=30, font='Abadi 10', command=switch_to_login,
                      height=3, bg="grey", fg='white')
btn1 = Button(frame_menu, text="New user", width=30, font='Abadi 11', command=switch_to_registration, height=3,
              bg="grey", fg='white')
btn_ext = Button(frame_menu, text="Exit", command=exit, font='Abadi 15', background='red')
btn_admin = Button(frame_menu, text='Admin menu', bg="grey", fg='white', font='Abadi 10', command=switch_to_admin_login)






frame_menu.place(relx=0, rely=0)
lbl_menu.place(relx=0.26, rely=0.1)
lbl_option.place(relx=0.3, rely=0.3)
btn_question.place(relx=0.25, rely=0.70, anchor='s')
btn1.place(relx=0.74, rely=0.70, anchor='s')
btn_ext.place(relx=0.91, rely=0.81)
btn_admin.place(relx=0.4, rely=0.74)

########################################################################################################################
# Registration Window
frame_regis = Frame(width=500, height=600, bg="#707B7C")

lbl_sign = Label(frame_regis, text='Create your account', font='Impact  21', fg="white", bg='#707B7C')
lbl_mail = Label(frame_regis, text='E-mail', font="Calibri 13", bg='#707B7C', fg="white")
lbl_pass = Label(frame_regis, text='Password', font="Calibri 13", bg='#707B7C', fg="white")
lbl_pass1 = Label(frame_regis, text='Confirm Password', font="Calibri 13", bg='#707B7C', fg="white")
lbl_name = Label(frame_regis, text='Username', font="Calibri 13", bg='#707B7C', fg="white")

entry_mail = Entry(frame_regis, width=37, font="Calibri 16", bg="#424b4c", fg="white")
entry_name = Entry(frame_regis, width=37, font="Calibri 16", bg="#424b4c", fg="white")
entry_pass = Entry(frame_regis, width=37, font="Calibri 16", show='*', bg="#424b4c", fg="white")
entry_pass1 = Entry(frame_regis, width=37, font="Calibri 16", show='*', bg="#424b4c", fg="white")
entry_pass1.bind("<Return>", create)

check_btn = Checkbutton(frame_regis, text='Show Password', image=photo, variable=var, command=show_pass, bg="#424b4c")
check_btn1 = Checkbutton(frame_regis, text='Show Password', image=photo, variable=var2, command=show_pass1,
                         bg="#424b4c")
btn_create = Button(frame_regis, text="Create", width=35, font='Impact 13', height=2, command=create, bg="#5580d1",
                    fg='white')
btn_ext = Button(frame_regis, text="Exit", command=exit, font='Abadi 15', background='#5580d1', bd=10)
btn_save = Button(frame_regis, text="Save", width=14, font='Abadi 10', bd=7, height=2, bg="#424b4c", fg='white',
                  command=SaveRegInfo)
btn_back = Button(frame_regis, text="Back <==", width=10, font='Calibri 10', bd=7, height=2, bg="red", fg='white',
                  command=back_to_menu)



lbl_sign.place(relx=0.25, rely=0.08, anchor=W)
lbl_mail.place(relx=0.05, rely=0.19)
lbl_pass.place(relx=0.05, rely=0.47)
lbl_pass1.place(relx=0.05, rely=0.61)
lbl_name.place(relx=0.05, rely=0.33)


entry_mail.place(relx=0.05, rely=0.24)
entry_name.place(relx=0.05, rely=0.38)
entry_pass.place(relx=0.05, rely=0.52)
entry_pass1.place(relx=0.05, rely=0.66)


check_btn.place(relx=0.77, rely=0.52)
check_btn1.place(relx=0.77, rely=0.66)
btn_create.place(relx=0.46, rely=0.86, anchor='s')
btn_ext.place(relx=0.83, rely=0.89)
btn_save.place(relx=0.50, rely=0.98, anchor='s')
btn_back.place(relx=0.13, rely=0.98, anchor='s')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Login Window
frame_login = Frame(width=450, height=300, bg="green")
lg_login = Label(frame_login, text='Login', font="Impact 28", fg='white', bg="green")
lg_name = Label(frame_login, text='E-mail', font="Calibri 19", bg="green", fg="white")
lg_pass_label = Label(frame_login, text='Password', font="Calibri 19", bg="green", fg="white")

lg_login.place(relx=0.45, rely=0.03)
lg_name.place(relx=0.05, rely=0.30)
lg_pass_label.place(relx=0.05, rely=0.48)

lg_name_entry = Entry(frame_login, width=20, font="Calibri 16", bg="#424b4c", fg='white')
lg_pass_entry = Entry(frame_login, width=20, show='*', font="Calibri 16", bg="#424b4c", fg='white')
lg_pass_entry.bind('<Return>', switch_to_shop)
insert_default_text()
insert_default_text2()
lg_name_entry.bind('<FocusIn>', on_email_entry_click)
lg_name_entry.bind('<FocusOut>', on_email_entry_focus_out)

lg_pass_entry.bind('<FocusIn>', on_email_entry_click1)
lg_pass_entry.bind('<FocusOut>', on_email_entry_focus_out1)

btn_log = Button(frame_login, text='Sign In', command=switch_to_shop, font='Abadi 15', width=10, bg="#5580d1",
                 fg="white")
btn_ext = Button(frame_login, text="Exit", command=exit, font='Abadi 15', bg="#2a2829", fg='#5580d1')
btn_back = Button(frame_login, text="Back <==", width=10, font='Calibri 10', height=2, bg="#2a2829", fg='#5580d1',
                  command=back_to_reg)
check_btn2 = Checkbutton(frame_login, variable=var3, command=show_pass2, bg="green")


lg_name_entry.place(relx=0.30, rely=0.32)
lg_pass_entry.place(relx=0.30, rely=0.48)

check_btn2.place(relx=0.86, rely=0.48)
btn_log.place(relx=0.39, rely=0.67)
btn_ext.place(relx=0.86, rely=0.84)
btn_back.place(relx=0.13, rely=0.98, anchor='s')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Admin Login
frame_admin_login = Frame(width=300, height=250, bg='#17C5D5')

lbl_ad_login = Label(frame_admin_login, text="Login", font='Arial 15', bg='#17C5D5')
lbl_ad_password = Label(frame_admin_login, text="Password", font='Arial 15', bg='#17C5D5')
entr_ad_login = Entry(frame_admin_login, width=16, font='Calibri 15', bd=7)
entr_ad_pass = Entry(frame_admin_login, width=16, font='Calibri 15', bd=7)
entr_ad_pass.bind('<Return>', switch_to_admin)
btn_admin_entry = Button(frame_admin_login, text='Enter', command=switch_to_admin)
btn_back2 = Button(frame_admin_login, text="Back <==", width=10, font='Calibri 10', bg="#2a2829", fg='#5580d1',
                   command=back_to_menu_from_admin_login)

lbl_ad_login.place(relx=0.4, rely=0.09)
lbl_ad_password.place(relx=0.37, rely=0.45)
entr_ad_login.place(relx=0.22, rely=0.25)
entr_ad_pass.place(relx=0.22, rely=0.6)
btn_admin_entry.place(relx=0.46, rely=0.81)
btn_back2.place(relx=0.7, rely=0.86)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Admin Window
frame_admin = Frame(width=650, height=600, bg="#CA7171")

admin_image_label = Label(frame_admin, image=photo1, bd=0, bg="#CA7171")
admin_image_label.image = photo1
btn_sett = Button(frame_admin, text='Settings', width=10, height=3, font='Abadi 15', bg='yellow',
                  command=switch_to_settings)
btn_add = Button(frame_admin, text='Add', width=10, height=3, font='Abadi 15', bg='yellow', command=switch_options)
btn_info = Button(frame_admin, text='Users', width=10, height=3, font='Abadi 15', bg='yellow', command=switch_to_users)
btn_info1 = Button(frame_admin, text='Books', width=10, height=3, font='Abadi 15', bg='yellow', command=switch_to_book)
btn_back1 = Button(frame_admin, text="Back <==", width=10, font='Calibri 10', bd=7, height=2, bg="red", fg='white',
                   command=back_to_menu_from_admin)
product_info = Button(frame_admin, text='Products', width=10, height=3, font='Abadi 15', bg='yellow',
                      command=switch_to_products_info)


product_info.place(relx=0.42, rely=0.02)
btn_back1.place(relx=0.83, rely=0.9)
btn_info1.place(relx=0.8, rely=0.02)
btn_info.place(relx=0.61, rely=0.02)
btn_add.place(relx=0.23, rely=0.02)
btn_sett.place(relx=0.04, rely=0.02)
admin_image_label.place(relx=0.2, rely=0.2)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Settings
frame_set = Frame(width=300, height=400)

styles = ['Abadi', 'Impact', 'Calibri', 'Verdana', 'Courier', 'Times NEW Roman']
spisok = [i for i in range(1, 26)]

bg_name = Label(frame_set, text='Choose background color', foreground='#76009F', font='Abadi 15', )
bg_srift = Label(frame_set, text='Choose text style', foreground='#76009F', font='Abadi 15', )
rad_but = Radiobutton(frame_set, text='White', variable=var1, value=1, command=change_theme, font='Abadi 10',
                      fg='#76009F')
rad_but1 = Radiobutton(frame_set, text='Black', variable=var1, value=2, command=change_theme, font='Abadi 10',
                       fg='#76009F')
btn_back2 = Button(frame_set, text="Back <==", width=10, font='Calibri 10', bd=7, height=2, bg="red", fg='white',
                   command=back_to_shop_from_set)
btn3 = Button(frame_set, text="Press", width=10, font='Calibri 10', bd=7, height=2, bg="red", fg='white',
              command=change_font)
com_box = ttk.Combobox(frame_set, values=styles)
com_box1 = ttk.Combobox(frame_set, values=spisok)
entr_color = Entry(frame_set, width=15, font='Abadi 10')



entr_color.place(relx=0.05, rely=0.65)
bg_name.place(relx=0.05, rely=0.12)
bg_srift.place(relx=0.05, rely=0.34)
rad_but.place(relx=0.05, rely=0.2)
rad_but1.place(relx=0.05, rely=0.25)
btn_back2.place(relx=0.05, rely=0.81)
btn3.place(relx=0.72, rely=0.81)
com_box.place(relx=0.05, rely=0.40)
com_box1.place(relx=0.5, rely=0.40)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Choose option
frame_option = Frame(width=300, height=200)

rad_but2 = Radiobutton(frame_option, text='Add User', width=10, font='Arial 12', variable=var1, value=1, )
rad_but3 = Radiobutton(frame_option, text='Add Book', width=10, variable=var1, font='Arial 12', value=2, )
rad_but4 = Radiobutton(frame_option, text='Add Snack', width=10, variable=var1, value=3, font='Arial 12', )
btn_option = Button(frame_option, text='Select', command=options)
btn_back5 = Button(frame_option, text='Back <==', font='Abadi 12', command=back_to_admin_from_option)


btn_back5.place(relx=0.7, rely=0.8)
btn_option.place(relx=0.4, rely=0.3)
rad_but2.place(relx=0.1, rely=0.2)
rad_but3.place(relx=0.1, rely=0.4)
rad_but4.place(relx=0.1, rely=0.6)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Users
frame_users = Frame(width=400, height=500, bg="green")


lst_box = Listbox(frame_users, width=25, font='Calibri 15')
btn_add2 = Button(frame_users, text='View', command=add_to_list_box)
btn_add3 = Button(frame_users, text='Delete', command=delete_from_lst_box)
btn_back3 = Button(frame_users, text='Back', bg='red', width=15, command=back_to_admin)
btn_back4 = Button(frame_users, text='Edit', command=edit)


btn_back4.place(relx=0.45, rely=0.7)
btn_back3.place(relx=0.7, rely=0.85)
btn_add3.place(relx=0.7, rely=0.7)
btn_add2.place(relx=0.17, rely=0.7)
lst_box.place(relx=0.17, rely=0.15)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Books
frame_books = Frame(width=400, height=500, bg="green")


lst_box1 = Listbox(frame_books, width=25, font='Calibri 15')
btn_add2 = Button(frame_books, text='View', command=add_to_list_books)
btn_book = Button(frame_books, text='Edit', command=edit_book_price)
btn_add3 = Button(frame_books, text='Delete', command=delete_from_list_books)
btn_back3 = Button(frame_books, text='Back', bg='red', width=15, command=back_to_admin_from_book)


btn_book.place(relx=0.45, rely=0.7)
lst_box1.place(relx=0.17, rely=0.15)
btn_add2.place(relx=0.17, rely=0.7)
btn_add3.place(relx=0.7, rely=0.7)
btn_back3.place(relx=0.7, rely=0.85)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Add book
frame_add_book = Frame(root, width=400, height=300)


lbl_add = Label(frame_add_book, text='Add new book', font='Calibri 20', fg='red')
add_name = Entry(frame_add_book, width=25, bd=7, font='Calibri 13')
add_price1 = Label(frame_add_book, text='Add price', font='Calibri 13', fg='red')
add_price = Entry(frame_add_book, width=25, bd=7, font='Calibri 13')
add_btn = Button(frame_add_book, text='Add', command=add_book)


lbl_add.place(relx=0.24, rely=0.08)
add_name.place(relx=0.21, rely=0.25)
add_price1.place(relx=0.21, rely=0.37)
add_price.place(relx=0.21, rely=0.50)
add_btn.place(relx=0.34, rely=0.71)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# FRame add snack
frame_add_snack = Frame(root, width=400, height=300)

lbl_snack = Label(frame_add_snack, text='Add new snack', font='Calibri 20', fg='red')
add_name1 = Entry(frame_add_snack, width=25, bd=7, font='Calibri 13')
add_price2 = Label(frame_add_snack, text='Add price', font='Calibri 13', fg='red')
add_price3 = Entry(frame_add_snack, width=25, bd=7, font='Calibri 13')
add_btn1 = Button(frame_add_snack, text='Add', command=add_product)

lbl_snack.place(relx=0.36, rely=0.08)
add_name1.place(relx=0.21, rely=0.25)
add_price2.place(relx=0.21, rely=0.35)
add_price3.place(relx=0.21, rely=0.50)
add_btn1.place(relx=0.34, rely=0.71)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# New price

frame_product_price = Frame(root, width=400, height=450)

lbl_add3 = Label(frame_product_price, text='New Price', font='Calibri 20', fg='red')
add_price7 = Entry(frame_product_price, width=25, bd=7, font='Calibri 13')
add_price8 = Button(frame_product_price, text=' Confirm', command=confirm_price)
lst_box_users2 = Listbox(frame_product_price, width=25, font='Calibri 15')
product_list()


lst_box_users2.place(relx=0.18, rely=0.43)
lbl_add3.place(relx=0.36, rely=0.05)
add_price7.place(relx=0.21, rely=0.23)
add_price8.place(relx=0.37, rely=0.33)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
frame_book_price = Frame(root, width=400, height=450)


lbl_add4 = Label(frame_book_price, text='New Price', font='Calibri 20', fg='red')
add_book_price = Entry(frame_book_price, width=25, bd=7, font='Calibri 13')
add_book_price1 = Button(frame_book_price, text=' Confirm', command=confirm_book_price)
lst_box_books2 = Listbox(frame_book_price, width=25, font='Calibri 15')
book_list()


lst_box_books2.place(relx=0.18, rely=0.43)
lbl_add4.place(relx=0.36, rely=0.05)
add_book_price.place(relx=0.21, rely=0.23)
add_book_price1.place(relx=0.37, rely=0.33)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# New password

frame_password = Frame(root, width=400, height=450)

lbl_add1 = Label(frame_password, text='New Password', font='Calibri 20', fg='red')

add_password = Entry(frame_password, width=25, bd=7, font='Calibri 13')
add_password1 = Label(frame_password, text='Confirm Password', font='Calibri 13', fg='red')
add_password2 = Entry(frame_password, width=25, bd=7, font='Calibri 13')
add_password3 = Button(frame_password, text=' Confirm', command=confirm)
lst_box_users1 = Listbox(frame_password, width=25, font='Calibri 15')
users_in_list()



lst_box_users1.place(relx=0.18, rely=0.43)
lbl_add1.place(relx=0.36, rely=0.05)
add_password.place(relx=0.21, rely=0.17)
add_password1.place(relx=0.21, rely=0.23)
add_password2.place(relx=0.21, rely=0.3)
add_password3.place(relx=0.37, rely=0.37)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# User account
frame_user_acc = Frame(width=1000, height=700, bg="#6E0800")


products_to_buy = []
lbl_books = Label(frame_user_acc, text='Books List', bg="#6E0800", font='Verdana 15', fg='#F830B2')
lbl_coffee = Label(frame_user_acc, text='Coffee List', bg="#6E0800", font='Verdana 15', fg='#F830B2')
lbl_quantity = Label(frame_user_acc, text='Quantity:', bg="#6E0800", font='Verdana 15', fg='#F830B2')
entr_search = Entry(frame_user_acc, width=20, font='Verdana 15', bd=10)
entr_search.bind('<Return>', search)
btn_search = Button(frame_user_acc, image=photo3, bg="#6E0800", command=search)
lst_box_books = Listbox(frame_user_acc, width=30, font='Abadi 15')
books_in_list()
lst_box_products = Listbox(frame_user_acc, width=30, font='Abadi 15')
product_in_list()
add_btn = Button(frame_user_acc, width=20, height=2, text='Add to card', bg='pink', command=add_to_card1)
wallet_btn = Button(frame_user_acc, text='Wallet', width=17, height=2, command=switch_to_wallet,bg='#670087')
entr_wallet_info = Label(frame_user_acc, text='', font='Abadi 14', bg="#6E0800", fg='yellow')
add_btn3 = Button(frame_user_acc, width=20, height=2, text='Add to card', bg='pink', command=add_to_card2)
com_box2 = ttk.Combobox(frame_user_acc, values=products_to_buy)
com_box2.insert(END, 'Products')
select = Button(frame_user_acc, text='Select', command=select)
spin_box = Spinbox(frame_user_acc, from_=1, to=10, width=7, font='Abadi 10')
admin_image_label1 = Label(frame_user_acc, image=photo2, bg="#6E0800")
admin_image_label1.image = photo2
profile_name = Label(frame_user_acc, text='', bg="#6E0800", fg='White', font='Calibri 14')
profile_password = Label(frame_user_acc, text='', bg="#6E0800", fg='White', font='Calibri 14')
edit_profile = Button(frame_user_acc, text='Edit', width=10, bg='purple', command=edit_profile)
btn_back5 = Button(frame_user_acc, text='Back <==', bg='blue', font='Abadi 10', width=14, height=2,
                   command=back_to_menu_from_user)




lbl_books.place(relx=0.02, rely=0.36)
lbl_coffee.place(relx=0.63, rely=0.36)
lbl_quantity.place(relx=0.8, rely=0.36)
entr_search.place(relx=0.4, rely=0.02)
btn_search.place(relx=0.69, rely=0.02)
lst_box_books.place(relx=0.02, rely=0.4)
lst_box_products.place(relx=0.63, rely=0.4)
add_btn.place(relx=0.02, rely=0.75)
wallet_btn.place(relx=0.77, rely=0.1)
entr_wallet_info.place(relx=0.76, rely=0.04)
add_btn3.place(relx=0.81, rely=0.75)
com_box2.place(relx=0.43, rely=0.5)
select.place(relx=0.43, rely=0.6)
spin_box.place(relx=0.9, rely=0.37)
admin_image_label1.place(relx=0.02, rely=0.02)
profile_name.place(relx=0.12, rely=0.04)
profile_password.place(relx=0.12, rely=0.09)
edit_profile.place(relx=0.02, rely=0.12)
btn_back5.place(relx=0.86, rely=0.9)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Frame products
frame_products = Frame(width=400, height=500, bg="green")
lst_box4 = Listbox(frame_products, width=25, font='Calibri 15')
btn_add2 = Button(frame_products, text='View', command=view_products)
btn_add6 = Button(frame_products, text='Edit', command=edit_price)
btn_add4 = Button(frame_products, text='Delete', command=delete_form_lst_products)
btn_back5 = Button(frame_products, text='Back', bg='red', width=15, command=back_to_admin_from_products)

btn_add6.place(relx=0.45, rely=0.7)
lst_box4.place(relx=0.17, rely=0.15)
btn_add2.place(relx=0.17, rely=0.7)
btn_add4.place(relx=0.7, rely=0.7)
btn_back5.place(relx=0.7, rely=0.85)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Wallet
frame_wallet = Frame(width=300, height=250, bg='#424949')

amount = Label(frame_wallet, text='Enter your wallet value', font='Abadi 15', bg='#424949', fg='yellow')
entr_amount = Entry(frame_wallet, width=20, font='Arial 15', bg='#273746')
entr_amount.bind('<Return>', confirm_wallet)
confirm_btn = Button(frame_wallet, text='Confirm', command=confirm_wallet)

amount.place(relx=0.13, rely=0.2)
entr_amount.place(relx=0.2, rely=0.5)
confirm_btn.place(relx=0.4, rely=0.7)

root.mainloop()
