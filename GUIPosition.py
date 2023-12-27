import tkinter as tk
from tkinter import messagebox
from Position import Position

class PositionEntryWindow:
    def __init__(self, root, shavtzak_instance):
        self.root = root
        self.root.geometry("350x350")
        self.root.title("Position Entry")
        self.root.configure(bg="lightcyan")

        self.shavtzak_instance = shavtzak_instance

        self.positionName = tk.StringVar()
        self.numOfGuards = tk.StringVar()
        self.timeToGuard = tk.StringVar()

        entry_label = tk.Label(root, text="Enter Position Name:", font=('Raleway', 14), bg="lightcyan", fg="black")
        entry_label.pack(pady=10)

        entry_field = tk.Entry(root, textvariable=self.positionName, font=('Raleway', 14))
        entry_field.pack(pady=10)

        entry_label = tk.Label(root, text="Enter Number of Guards:", font=('Raleway', 14), bg="lightcyan", fg="black")
        entry_label.pack(pady=10)

        entry_field = tk.Entry(root, textvariable=self.numOfGuards, font=('Raleway', 14))
        entry_field.pack(pady=10)

        entry_label = tk.Label(root, text="Enter Time to Guard (minutes):", font=('Raleway', 14), bg="lightcyan", fg="black")
        entry_label.pack(pady=10)

        entry_field = tk.Entry(root, textvariable=self.timeToGuard, font=('Raleway', 14))
        entry_field.pack(pady=10)

        submit_button = tk.Button(root, text="Submit", command=self.on_position_entry, font=('Raleway', 14), bg="#20bebe", fg="white")
        submit_button.pack()

    def on_position_entry(self):
        try:
            position_name = self.positionName.get()
            num_of_guards = int(self.numOfGuards.get())
            time_to_guard = int(self.timeToGuard.get())

            # Check if time_to_guard is divisible by 5
            if time_to_guard % 5 != 0:
                messagebox.showwarning("Position Entry", "Time to guard must be divisible by 5. Please enter a valid value.")
                return

            if position_name and num_of_guards >= 0 and time_to_guard >= 0:
                new_position = Position(position_name, num_of_guards, time_to_guard)

                if self.shavtzak_instance.addPosition(new_position):
                    messagebox.showinfo("Position Added", f"Position '{position_name}' added successfully.")
                    self.root.destroy()  # Close the window after submitting

                else:
                    messagebox.showwarning("Position Entry", f"The position '{position_name}' already exists. Please enter a different position name.")

            else:
                messagebox.showwarning("Position Entry", "Invalid input. Please enter valid data.")
        except ValueError:
            messagebox.showwarning("Position Entry", "Invalid input. Please enter valid numeric values.")


