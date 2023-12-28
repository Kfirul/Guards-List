import tkinter as tk
from tkinter import messagebox

class GuardEntryWindow:
    def __init__(self, root, shavtzak_instance):
        # Initialize the Guard Entry Window
        self.root = root
        self.root.geometry("300x150")
        self.root.title("Guard Entry")
        self.root.configure(bg="lightcyan")

        # Store the Shavtzak instance for later use
        self.shavtzak_instance = shavtzak_instance

        # Label for Guard Name entry
        entry_label = tk.Label(self.root, text="Enter Guard Name:", font=('Raleway', 14), bg="lightcyan", fg="black")
        entry_label.pack(pady=5)

        # Entry field for Guard Name
        self.guardName = tk.StringVar()
        entry_field = tk.Entry(self.root, textvariable=self.guardName, font=('Raleway', 14))
        entry_field.pack(pady=5)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.on_guard_entry, font=('Raleway', 14), bg="#20bebe", fg="white")
        submit_button.pack(pady=10)

    def on_guard_entry(self):
        # Callback function for the Submit button
        guard_name = self.guardName.get()

        # Check if the guard name is not empty
        if guard_name:
            # Try to add the guard to the Shavtzak instance
            if self.shavtzak_instance.addGuard(guard_name):
                # Show success message and close the window
                messagebox.showinfo("Guard Added", f"Guard '{guard_name}' added successfully.")
                self.root.destroy()
            else:
                # Show a warning if the name already exists
                messagebox.showwarning("Guard Entry", "This name already exists. Please enter a different name.")
        else:
            # Show a warning if no name is entered
            messagebox.showwarning("Guard Entry", "Please enter a guard name.")


