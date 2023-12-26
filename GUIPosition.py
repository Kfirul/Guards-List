import tkinter as tk
from tkinter import messagebox

from Position import Position


class PositionEntryWindow:
    def __init__(self, root, shavtzak_instance):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("Position Entry")

        self.shavtzak_instance = shavtzak_instance

        self.positionName = tk.StringVar()
        self.numOfGuards = tk.StringVar()
        self.timeToGuard = tk.StringVar()

        self.label = tk.Label(root, text="Enter Position Name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.positionName)
        self.entry.pack(pady=10)

        self.label = tk.Label(root, text="Enter Number of Guards:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.numOfGuards)
        self.entry.pack(pady=10)

        self.label = tk.Label(root, text="Enter Time to Guard (minutes):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.timeToGuard)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.on_position_entry)
        self.submit_button.pack()

    def on_position_entry(self):
        try:
            position_name = self.positionName.get()
            num_of_guards = int(self.numOfGuards.get())
            time_to_guard = int(self.timeToGuard.get())

            if position_name and num_of_guards >= 0 and time_to_guard >= 0:
                new_position = Position(position_name, num_of_guards, time_to_guard)
                self.shavtzak_instance.addPosition(new_position)
                messagebox.showinfo("Position Added", f"Position '{position_name}' added successfully.")
                self.root.destroy()  # Close the window after submitting
            else:
                messagebox.showwarning("Position Entry", "Invalid input. Please enter valid data.")
        except ValueError:
            messagebox.showwarning("Position Entry", "Invalid input. Please enter valid numeric values.")
