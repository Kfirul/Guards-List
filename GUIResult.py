import tkinter as tk
from tkinter import ttk

class Result:
    def __init__(self, root, shavtzak_instance):
        # Initialize the Result Window
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Result")
        self.shavtzak_instance = shavtzak_instance
        self.root.configure(bg="lightcyan")

        # Label for the Result
        result_label = tk.Label(root, text="Guard List for Each Position", font=('Raleway', 16, 'bold'), bg="lightcyan", fg="black")
        result_label.pack(pady=10)

        # Configure style for the listbox
        style = ttk.Style()
        style.configure("Result.TListbox", font=('Raleway', 10), selectbackground="lightgray", background="lightcyan")

        # Create a Listbox widget
        self.listbox = tk.Listbox(root, height=15, selectmode=tk.SINGLE, font=('Raleway', 10), bg="lightcyan", selectbackground="lightgray", activestyle="none")
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create a horizontal scrollbar
        hscrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.listbox.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the listbox to use the horizontal scrollbar
        self.listbox.config(xscrollcommand=hscrollbar.set)

        # Create Guards List for each Position
        self.shavtzak_instance.createGuardsList()

        # Populate the listbox with Position names and associated Guard lists
        for position in self.shavtzak_instance.positionList:
            guard_list = ', '.join(position.guardList)
            item_text = f"{position.name}: {guard_list}"
            self.listbox.insert(tk.END, item_text)

