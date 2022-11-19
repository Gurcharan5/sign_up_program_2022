import tkinter as tk
import random


def random_username():
    random_ascii = random.randint(51, 57)
    random_ascii_2 = random.randint(51, 57)
    random_ascii_3 = random.randint(51, 57)

    forename = forename_entry.get()
    forename = forename[:4]

    surname = surname_entry.get()
    surname = surname[:3]

    random_ascii_values = chr(random_ascii) + chr(random_ascii_2) + chr(random_ascii_3)

    random_username_username = forename + surname + str(random_ascii_values)
    return random_username_username


signup = tk.Tk()
signup.title("Sign Up Page")

forename_label = tk.Label(signup,
                          text="What is your forename?",
                          font=("Ariel", 10))
forename_label.grid(column=1,
                    row=0,
                    padx=75)

forename_entry = tk.Entry(signup,
                          width=30)
forename_entry.grid(column=1,
                    row=1,
                    padx=75)

surname_label = tk.Label(signup,
                         text="What is your surname?",
                         font=("Ariel", 10))
surname_label.grid(column=1,
                   row=2,
                   padx=75)

surname_entry = tk.Entry(signup,
                         width=30)
surname_entry.grid(column=1,
                   row=3,
                   padx=75)

username_label = tk.Label(signup,
                          text="What would you like your username to be?",
                          font=("Ariel", 10))
username_label.grid(column=1,
                    row=4,
                    padx=75)

username_entry = tk.Entry(signup,
                          width=30)
username_entry.grid(column=1,
                    row=5,
                    padx=75)

suggested_username_results = tk.BooleanVar()

suggested_username_checkbox = tk.Checkbutton(signup,
                                             text="Would you like to use a suggested username?",
                                             variable=suggested_username_results,
                                             onvalue=True,
                                             offvalue=False)
suggested_username_checkbox.grid(column=1,
                                 row=6)

suggested_username_label = tk.Label(signup,
                                    text="",
                                    font=("Ariel", 10))
suggested_username_label.grid(column=1,
                              row=7)

if suggested_username_results:
    suggested_username = random_username()
    suggested_username_label.config(text=suggested_username)

signup.mainloop()
