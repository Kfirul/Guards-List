import tkinter as tk
from tkinter import messagebox

class GuardEntryWindow:
    def __init__(self, root, shavtzak_instance):
        self.root = root
        self.root.geometry("300x150")
        self.root.title("Guard Entry")
        self.root.configure(bg="lightcyan")

        self.shavtzak_instance = shavtzak_instance

        entry_label = tk.Label(self.root, text="Enter Guard Name:", font=('Raleway', 14), bg="lightcyan", fg="black")
        entry_label.pack(pady=5)

        self.guardName = tk.StringVar()
        entry_field = tk.Entry(self.root, textvariable=self.guardName, font=('Raleway', 14))
        entry_field.pack(pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.on_guard_entry, font=('Raleway', 14), bg="#20bebe", fg="white")
        submit_button.pack(pady=10)

    def on_guard_entry(self):
        guard_name = self.guardName.get()

        if guard_name:
            if self.shavtzak_instance.addGuard(guard_name):
                messagebox.showinfo("Guard Added", f"Guard '{guard_name}' added successfully.")
                self.root.destroy()  # Close the window after submitting
            else:
                messagebox.showwarning("Guard Entry", "This name already exists. Please enter a different name.")
        else:
            messagebox.showwarning("Guard Entry", "Please enter a guard name.")


