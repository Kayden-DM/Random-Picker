## Random Picker
A desktop random picker built with CustomTkinter. It lets the user build a list of entries and pick one at random, with buttons to add, remove, and clear items.

## Features
Add Entries — Type into the entry field and click Add to append it to the list.

Scrollable List — Displays all entries in a CTkScrollableFrame, with each item on its own row.

Remove Items — Each row has a ✕ button to delete that entry.

Clear All — Removes every entry and clears the result label.

Random Pick — Uses random.choice() to select a winner and displays it with a 🎉 highlight.

Empty List Handling — Shows "Add some inputs first!" if Pick is pressed with no entries.

Dark Mode UI — CustomTkinter dark appearance with a blue accent theme.

## Technologies Used
text
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Desktop GUI |
| `CTkScrollableFrame` | Holds the scrollable list of entries |
| `random.choice()` | Picks a random winner |
| `lambda` | Binds the correct item to each ✕ button |
| `winfo_children()` | Clears the list widgets on refresh |
| `list` (`inputs`) | Stores all current entries |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install CustomTkinter by running pip install customtkinter.

Save the code as random_picker.py.

Open a terminal in the folder containing the file.

Run python random_picker.py.

Type entries and click Add, press Pick Random to choose one, and use ✕ or Clear All to manage the list.

## Improvements
Prevent duplicate entries — adding the same item twice puts two identical rows in the list, and inputs.remove(item) then only removes the first match; checking for duplicates on add would keep the list clean.

Highlight the chosen item — the winner is only shown in the result label; scrolling the list to the winner and highlighting its row would make the pick clearer when there are many entries.

