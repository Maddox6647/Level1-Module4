"""
Log Search using a Id-Name Dictionary
"""
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk
# TODO: Create a dictionary of integers for the keys and strings for the values.
#  Create a GUI app with three buttons. Look at 'log_search_example.png' in this
#  folder for an example of what your program should look like.

people = dict()
window = tk.Tk()

#  Button 1: Add Entry
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      After an ID is entered, use another input dialog to ask the user
#      to enter a name. Add this information as a new entry to your
#      dictionary.

window.title("searching log")
window.geometry("800x900")

def add_entry():

    user_id = simpledialog.askinteger(title="add entry", prompt="enter id number:")

    if user_id is not None:
        name = simpledialog.askstring(title="add entry", prompt="enter name:")

        if name:
            people[user_id] = name
            messagebox.showinfo(title="success", message="entry added")
#  Button 2: Search by ID
#      When this button is clicked, use an input dialog to ask the user
#      to enter an ID number.
#      If that ID exists, display that name to the user.
#      Otherwise, tell the user that that entry does not exist.
def search_entry():

    user_id = simpledialog.askinteger(title="search", prompt="enter id number")
    if user_id in people:
        messagebox.showinfo("result", f"Name: {people[user_id]}")
    else:
        messagebox.showinfo("result", "entry does not exist")
# Button 3: View List
#      When this button is clicked, display the entire list in a message
#      dialog in the following format:
#      ID: 123  Name: Harry Howard
#      ID: 245  Name: Polly Powers
#      ID: 433  Name: Oliver Ortega
#      etc...
def view_list():
    if len(people) == 0:
        messagebox.showinfo("list", "entry does not exist you idiot")
    else:
        text = ""

        for user_id, name in people.items():
            text += f"ID: {user_id}  Name: {name}\n"

        messagebox.showinfo(title="Full List", message=text)
# When this is complete, add a fourth button to your window.
# Button 4: Remove Entry
#      When this button is clicked, prompt the user to enter an ID using
#      an input dialog.
#      If this ID exists in the dictionary, remove it. Otherwise, notify the
#      user that the ID is not in the list.
def remove_entry():

    user_id = simpledialog.askinteger(title="remove", prompt="enter id number")
    if user_id in people:
        del people[user_id]
        messagebox.showinfo(title="removing id", message="good job, the id has been removed")
    else:
        messagebox.showinfo(title="remove", message="this id wasn't in the list, stupid monkey")
# Put the buttons outside of the def and under here:
tk.Button(window, text="Add Entry", command=add_entry).pack(pady=10)

tk.Button(window, text="search by ID", command=search_entry).pack(pady=10)

tk.Button(window, text="viewing list", command=view_list).pack(pady=10)

tk.Button(window, text="removing ID", command=remove_entry).pack(pady=10)

window.mainloop()

