""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk
from tkinter import ttk


def clearentries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

def read_table(tree):
    count = 0
    for record in data_list:
        if count % 2 == 0:
            tree.insert(parent='', index='end', text='', values=record, tags='evenrow')
        else:
            tree.insert(parent='', index='end', text='', values=record, tags='oddrow')
        count += 1


def edit_record(event, tree):
    index_selected = tree.focus()
    value = tree.item(index_selected, 'values')
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry1.insert(0, value[0])
    entry2.insert(0, value[1])
    entry3.insert(0, value[2])


data_list = []
data_list.append(("1", 1000, "oslo"))
data_list.append(("2", 2000, "chicago"))
data_list.append(("3", 3000, "milano"))
data_list.append(("4", 4000, "amsterdam"))

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#eeeeee", foreground="black", rowheight=24, fieldbackground="#eeeeee")
style.map('Treeview', background=[('selected', "#773333")])


container = tk.LabelFrame(main_window, text="Container")
container.grid(column=0, row=0, sticky=tk.N, padx=10)


frame1 = tk.Frame(container)
frame1.grid(column=1, row=1, pady=10, padx=10)


frame2 = tk.Frame(container)
frame2.grid(column=1, row=2, pady=10, padx=10)

frame3 = tk.Frame(container)
frame3.grid(column=1, row=0)

label1 = tk.Label(frame1, text="Id")
label1.grid(column=1, row=1, pady=10)

entry1 = tk.Entry(frame1, width=5)
entry1.grid(column=1, row=2, padx=10)

label2 = tk.Label(frame1, text="Weight")
label2.grid(column=2, row=1)

entry2 = tk.Entry(frame1, width=8)
entry2.grid(column=2, row=2, padx=10)

label3 = tk.Label(frame1, text="Destination")
label3.grid(column=3, row=1)

entry3 = tk.Entry(frame1)
entry3.grid(column=3, row=2, padx=10)

label4 = tk.Label(frame1, text="Weather")
label4.grid(column=4, row=1)

entry4 = tk.Entry(frame1, width=15)
entry4.grid(column=4, row=2, padx=10)


button1 = tk.Button(frame2, text="Create")
button1.grid(column=1, row=1, padx=10)

button2 = tk.Button(frame2, text="Update")
button2.grid(column=2, row=1, padx=10)

button3 = tk.Button(frame2, text="Delete")
button3.grid(column=3, row=1, padx=10)

button4 = tk.Button(frame2, text="Clear Entry Boxes", command=clearentries)
button4.grid(column=4, row=1, padx=10)


tree_view_scrollbar = tk.Scrollbar(frame3)
tree_view_scrollbar.grid(column=2, row=1, sticky='ns')
tree_view = ttk.Treeview(frame3, yscrollcommand=tree_view_scrollbar.set, selectmode="browse")
tree_view.grid(column=1, row=1)
tree_view_scrollbar.config(command=tree_view.yview)

tree_view['columns'] = ("Id", "Weight", "Destination")
tree_view.column("#0", width=0, stretch=tk.NO)
tree_view.column("Id", anchor=tk.E, width=50)
tree_view.column("Weight", anchor=tk.W, width=90)
tree_view.column("Destination", anchor=tk.W, width=200)

tree_view.heading("#0", text="", anchor=tk.W)
tree_view.heading("Id", text="Id", anchor=tk.CENTER)
tree_view.heading("Weight", text="Weight", anchor=tk.CENTER)
tree_view.heading("Destination", text="Destination", anchor=tk.CENTER)

tree_view.tag_configure('oddrow', background='#ECECEC')
tree_view.tag_configure('evenrow', background='#DEDEDE')

tree_view.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_view))

read_table(tree_view)

if __name__ == "__main__":
    main_window.mainloop()