import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

inputs = []


def refresh_list():
    for widget in list_frame.winfo_children():
        widget.destroy()
    for item in inputs:
        row = ctk.CTkFrame(list_frame)
        row.pack(fill="x", pady=2)

        label = ctk.CTkLabel(row, text=item, font=("Arial", 14))
        label.pack(side="left", padx=10, pady=5)

        remove = ctk.CTkButton(row, text="✕", width=30,
                               fg_color="transparent", hover_color="darkred",
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


root = ctk.CTk()
root.title("Random Picker")
root.geometry("400x600")

title = ctk.CTkLabel(root, text="Random Picker", font=("Arial", 24, "bold"))
title.pack(pady=(20, 10))

input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=10, padx=20, fill="x")

input_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter something...", font=("Arial", 14))
input_entry.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

add_btn = ctk.CTkButton(input_frame, text="Add", width=70, command=add_input)
add_btn.pack(side="left", padx=(5, 10), pady=10)

list_frame = ctk.CTkScrollableFrame(root, label_text="Inputs")
list_frame.pack(pady=10, padx=20, fill="both", expand=True)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 22, "bold"))
result_label.pack(pady=10)

pick_btn = ctk.CTkButton(root, text="Pick Random", font=("Arial", 16),
                         width=200, height=45, command=pick)
pick_btn.pack(pady=5)

clear_btn = ctk.CTkButton(root, text="Clear All", font=("Arial", 12),
                          width=120, fg_color="transparent", border_width=1,
                          command=clear_all)
clear_btn.pack(pady=(5, 20))

root.mainloop()