import tkinter as tk
from tkinter import messagebox

class GuardEntryWindow:
    def __init__(self, root,shavtzak_instance):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("Guard Entry")

        self.shavtzak_instance = shavtzak_instance

        self.guardName = tk.StringVar()

        self.label = tk.Label(root, text="Enter Guard Name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.guardName)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.on_guard_entry)
        self.submit_button.pack()

    def on_guard_entry(self):
        guard_name = self.guardName.get()

        if guard_name:
            self.shavtzak_instance.addGuard(guard_name)
            messagebox.showinfo("Guard Added", f"Guard '{guard_name}' added successfully.")
            self.root.destroy()  # Close the window after submitting
        else:
            messagebox.showwarning("Guard Entry", "Please enter a guard name.")