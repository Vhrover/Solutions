"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""

import tkinter as tk



def calculate():
    global current_number
    global other_number
    global operator

    if operator == '+':
        temp_number = float(current_number) + float(other_number)
        clear()
        current_number = str(temp_number)
        update_entry()
    elif operator == '-':
        temp_number = float(current_number) - float(other_number)
        clear()
        current_number = str(temp_number)
        update_entry()
    elif operator == '*':
        temp_number = float(current_number) * float(other_number)
        clear()
        current_number = str(temp_number)
        update_entry()
    elif operator == '/':
        temp_number = float(current_number) / float(other_number)
        current_number = str(temp_number)
        update_entry()


def clear():
    global current_number
    global other_number
    global is_first
    global has_comma

    current_number = ""
    other_number = ""
    is_first = True
    has_comma = False
    update_entry()


def update_entry():
    global is_first
    global current_number
    global other_number

    result_entry.configure(state="normal")
    result_entry.delete(0, tk.END)
    if is_first:
        result_entry.insert(0, current_number)
    else:
        result_entry.insert(0, other_number)
    result_entry.configure(state="readonly")

def add_number(number):
    global current_number
    global other_number
    global is_first

    if is_first:
        current_number += number
    else:
        other_number += number
    update_entry()



def add_comma():
    global current_number
    global other_number
    global is_first
    global has_comma

    if is_first and not has_comma:
        current_number += "."
        has_comma = True

    elif not is_first and not has_comma:
        other_number += "."

    update_entry()

def change_operator(type):
    global operator
    global is_first
    global has_comma

    if len(operator) == 0:
        has_comma = False
    operator = type
    is_first = False


current_number = ""
other_number = ""
is_first = True
has_comma = False
operator = ""



main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")
main_window.resizable(False, False)

label_frame = tk.LabelFrame(main_window, text="calculator", padx=10, pady=15)
label_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

result_frame = tk.Frame(label_frame)
result_frame.grid(row=1, column=1, padx=10, pady=10)

number_buttons = tk.Frame(label_frame)
number_buttons.grid(row=2, column=1, padx=20, pady=20)

clear_button_frame = tk.Frame(label_frame)
clear_button_frame.grid(row=3, column=1)


result_entry = tk.Entry(result_frame, state=tk.DISABLED, justify=tk.RIGHT)
result_entry.grid(row=2, column=2)

button1 = tk.Button(number_buttons, text="1", width=7, height=3, command=lambda: add_number("1"))
button1.grid(row=1, column=1)

button2 = tk.Button(number_buttons, text="2", width=7, height=3, command=lambda: add_number("2"))
button2.grid(row=1, column=2)

button3 = tk.Button(number_buttons, text="3", width=7, height=3, command=lambda: add_number("3"))
button3.grid(row=1, column=3)

button4 = tk.Button(number_buttons, text="4", width=7, height=3, command=lambda: add_number("4"))
button4.grid(row=2, column=1)

button5 = tk.Button(number_buttons, text="5", width=7, height=3, command=lambda: add_number("5"))
button5.grid(row=2, column=2)

button6 = tk.Button(number_buttons, text="6", width=7, height=3, command=lambda: add_number("6"))
button6.grid(row=2, column=3)

button7 = tk.Button(number_buttons, text="7", width=7, height=3, command=lambda: add_number("7"))
button7.grid(row=3, column=1)

button8 = tk.Button(number_buttons, text="8", width=7, height=3, command=lambda: add_number("8"))
button8.grid(row=3, column=2)

button9 = tk.Button(number_buttons, text="9", width=7, height=3, command=lambda: add_number("9"))
button9.grid(row=3, column=3)

button0 = tk.Button(number_buttons, text="0", width=7, height=3, command=lambda: add_number("0"))
button0.grid(row=4, column=1)

comma_button = tk.Button(number_buttons, text=".", width=7, height=3, command=add_comma)
comma_button.grid(row=4, column=2)

plus_button = tk.Button(number_buttons, text="+", width=7, height=3, command=lambda: change_operator("+"))
plus_button.grid(row=1, column=4)

minus_button = tk.Button(number_buttons, text="-", width=7, height=3, command=lambda: change_operator("-"))
minus_button.grid(row=2, column=4)

multiply_button = tk.Button(number_buttons, text="*", width=7, height=3, command=lambda: change_operator("*"))
multiply_button.grid(row=3, column=4)

divide_button = tk.Button(number_buttons, text="/", width=7, height=3, command=lambda: change_operator("/"))
divide_button.grid(row=4, column=4)

calculate_button = tk.Button(number_buttons, text="=", width=7, height=3, command=calculate)
calculate_button.grid(row=4, column=3)

clear_button = tk.Button(clear_button_frame, text="Clear All", width=14, height=3, command=clear)
clear_button.grid(row=1, column=1, pady=10)


if __name__ == "__main__":
    main_window.mainloop()
