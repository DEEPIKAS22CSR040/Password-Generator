import random
from tkinter import Label, Entry, Tk, Button

def generate_password():
    n_alpha = int(alpha_field.get())
    n_sym = int(sym_field.get())
    n_num = int(num_field.get())
    p = ""

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

    pass_lst = []
    for i in range(1, n_alpha + 1):
        c = random.choice(alphabets)
        pass_lst.append(c)

    for i in range(1, n_sym + 1):
        c = random.choice(symbols)
        pass_lst.append(c)

    for i in range(1, n_num + 1):
        c = str(random.choice(numbers)) 
        pass_lst.append(c)

    random.shuffle(pass_lst)

    for i in pass_lst:
        p += i

    pass_field.delete(0, 'end') 
    pass_field.insert(0, p)


window = Tk()
window.title("Password Generator")
window.config(bg="cadetblue")
window.geometry("700x450")

title_label = Label(window, text="Welcome To Password Generator!", font=("Arial", 20), fg="red", padx=50, pady=30)
title_label.place(relx=0.5, rely=0.1, anchor='center') 

alpha_label = Label(window, text="How many alphabets would you like to have?", font=("calibri bold",15), highlightbackground="blue", highlightcolor="blue",fg="royal blue4", relief="ridge")
alpha_field = Entry(window, width=20, font=15, bd=5, highlightbackground="blue", highlightcolor="blue")
num_label = Label(window, text="How many numbers would you like to have?", font=("calibri bold",15), highlightbackground="red", highlightcolor="red",fg="royal blue4", relief="ridge")
num_field = Entry(window, width=20, bd=5, highlightbackground="red", highlightcolor="red")
sym_label = Label(window, text="How many symbols would you like to have?", font=("calibri bold",15), highlightbackground="green", highlightcolor="green",fg="royal blue4", relief="ridge")
sym_field = Entry(window, width=20, bd=5, highlightbackground="green", highlightcolor="green")

res_btn = Button(window, text="GENERATE PASSWORD", width=20, bg="lime green", command=generate_password)
pass_label = Label(window, text="Password:", font=("calibri bold", 20), highlightbackground="purple", highlightcolor="purple", relief="ridge")
pass_field = Entry(window, width=25, bd=5, highlightbackground="purple", highlightcolor="purple")


alpha_label.place(relx=0.35, rely=0.3, anchor='center')
alpha_field.place(relx=0.65, rely=0.3, anchor='center')
num_label.place(relx=0.38, rely=0.4, anchor='center')
num_field.place(relx=0.65, rely=0.4, anchor='center')
sym_label.place(relx=0.38, rely=0.5, anchor='center')
sym_field.place(relx=0.65, rely=0.5, anchor='center')
res_btn.place(relx=0.5, rely=0.6, anchor='center')
pass_label.place(relx=0.35, rely=0.7, anchor='center')
pass_field.place(relx=0.65, rely=0.7, anchor='center')

window.mainloop()
