import tkinter as tk
from tkinter import ttk

class Result:
    def __init__(self, root, shavtzak_instance):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Result")
        self.shavtzak_instance = shavtzak_instance
        self.root.configure(bg="lightcyan")

        result_label = tk.Label(root, text="Guard List for Each Position", font=('Raleway', 16, 'bold'), bg="lightcyan", fg="black")
        result_label.pack(pady=10)

        style = ttk.Style()
        style.configure("Result.TListbox", font=('Raleway', 10), selectbackground="lightgray", background="lightcyan")

        self.listbox = tk.Listbox(root, height=15, selectmode=tk.SINGLE, font=('Raleway', 10), bg="lightcyan", selectbackground="lightgray", activestyle="none")
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Create a horizontal scrollbar
        hscrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.listbox.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Configure the listbox to use the scrollbars
        self.listbox.config(xscrollcommand=hscrollbar.set)

        self.shavtzak_instance.createGuardsList()

        for position in self.shavtzak_instance.positionList:
            guard_list = ', '.join(position.guardList)
            item_text = f"{position.name}: {guard_list}"
            self.listbox.insert(tk.END, item_text)

