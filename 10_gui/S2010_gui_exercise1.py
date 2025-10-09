"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

# main_window = tk.Tk()
# main_window.title("My first GUI")
# main_window.geometry("125x180")
#
# frame1 = tk.LabelFrame(main_window, text="Container")
# frame1.grid(column=0, row=0, ipadx=15, ipady=20, pady=10, padx=10)
#
# label1 = tk.Label(frame1, text="Id", pady=10)
# label1.grid(column=0, row=0,)
#
# entry1 = tk.Entry(frame1, width=5, justify="center")
# entry1.grid(column=0, row=1)
# entry1.insert(0, " ")
#
# button1 = tk.Button(frame1, text="Create")
# button1.grid(column=0, row=2)

main_window = tk.Tk()
main_window.title("My first GUI")
main_window.geometry("125x180")

frame1 = tk.LabelFrame(main_window, text="Container")
frame1.grid(column=0, row=0, pady=10, padx=10)

label1 = tk.Label(frame1, text="Id", pady=10, padx=40)
label1.grid(column=0, row=0)

entry1 = tk.Entry(frame1, width=5, justify="center")
entry1.grid(column=0, row=1)
entry1.insert(0, " ")

button1 = tk.Button(frame1, text="Create")
button1.grid(column=0, row=2, pady=15)





if __name__ == "__main__":
    main_window.mainloop()