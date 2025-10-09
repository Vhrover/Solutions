""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

def clearentries():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)



main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x250")

container = tk.LabelFrame(main_window, text="Container")
container.grid(column=0, row=0, sticky=tk.N, padx=10)


frame1 = tk.Frame(container)
frame1.grid(column=1, row=1, pady=10, padx=10)


frame2 = tk.Frame(container)
frame2.grid(column=1, row=2, pady=10, padx=10)


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


if __name__ == "__main__":
    main_window.mainloop()