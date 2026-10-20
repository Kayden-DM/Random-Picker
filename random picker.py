import tkinter as tk
import random

inputs = []


def refresh_list():
    for widget in list_frame.winfo_children():
        widget.destroy()
    for item in inputs:
        row = tk.Frame(list_frame)
        row.pack(fill="x", pady=2)

        label = tk.Label(row, text=item, font=("Arial", 14))
        label.pack(side="left", padx=10, pady=5)

        remove = tk.Button(row, text="✕", width=3,
                           command=lambda i=item: remove_input(i))
        remove.pack(side="right", padx=5)


def add_input():
    item = input_entry.get().strip()
    if item == "":
        return
    inputs.append(item)
    input_entry.delete(0, "end")
    refresh_list()


def remove_input(item):
    inputs.remove(item)
    refresh_list()


def clear_all():
    inputs.clear()
    refresh_list()
    result_label.configure(text="")


def pick():
    if not inputs:
        result_label.configure(text="Add some inputs first!")
        return
    winner = random.choice(inputs)
    result_label.configure(text=f"🎉 {winner} 🎉")


root = tk.Tk()
root.title("Random Picker")
root.geometry("400x600")

title = tk.Label(root, text="Random Picker", font=("Arial", 24, "bold"))
title.pack(pady=(20, 10))

input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=20, fill="x")

input_entry = tk.Entry(input_frame, font=("Arial", 14))
input_entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

add_btn = tk.Button(input_frame, text="Add", width=7, command=add_input)
add_btn.pack(side="left", padx=(5, 10), pady=10)

list_frame = tk.Frame(root)
list_frame.pack(pady=10, padx=20, fill="both", expand=True)

result_label = tk.Label(root, text="", font=("Arial", 22, "bold"))
result_label.pack(pady=10)

pick_btn = tk.Button(root, text="Pick Random", font=("Arial", 16),
                     width=20, height=2, command=pick)
pick_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All", font=("Arial", 12),
                      width=15, command=clear_all)
clear_btn.pack(pady=(5, 20))

root.mainloop()