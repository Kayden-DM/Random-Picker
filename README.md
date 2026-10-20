Random Picker
A GUI Python app built with CustomTkinter that lets you build a list of items and pick one at random.

Concepts Used
CustomTkinter Widgets — uses CTkScrollableFrame, CTkEntry, and CTkButton with a dark theme.

Lambda Closures — lambda i=item: remove_input(i) binds each row's remove button to its specific item.

Widget Rebuilding — refresh_list() destroys and recreates all rows to reflect the current list.

Features
Dynamic List — add items via the entry field and remove any individual item with its ✕ button.

Scrollable Display — the input list lives in a scrollable frame so long lists stay usable.

Random Selection — "Pick Random" highlights a winner with emojis, with a "Clear All" reset option.

Improvements
Enter Key Support — bind <Return> on the entry so users can add items without clicking; the mouse-only flow feels clunky.

Duplicate & Feedback Handling — adding the same item twice is silently allowed, and empty input just returns with no message; show brief feedback.

Remove-by-Identity — inputs.remove(item) removes the first matching value, so duplicates remove the wrong row; store items with unique IDs or index-based removal.
