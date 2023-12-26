import tkinter as tk
from tkinter import messagebox
from GUIShavtzak import GUIShavtzak

class Instructions:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Instructions")

        instructions_label = tk.Label(root, text="Welcome to Shavtzak App!\n\nInstructions:\n1. Set the start time below.\n2. Click 'OK' to open the main window and start using Shavtzak App!")
        instructions_label.pack(pady=10)

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()

        hour_label = tk.Label(root, text="Hour:")
        hour_label.pack(pady=5)

        hour_entry = tk.Entry(root, textvariable=self.hour_var)
        hour_entry.pack(pady=5)

        minute_label = tk.Label(root, text="Minute:")
        minute_label.pack(pady=5)

        minute_entry = tk.Entry(root, textvariable=self.minute_var)
        minute_entry.pack(pady=5)

        ok_button = tk.Button(root, text="OK", command=self.open_main_window)
        ok_button.pack(pady=10)

    def open_main_window(self):
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            if 0 <= hour < 24 and 0 <= minute < 60:
                self.root.destroy()
                main_window = tk.Tk()
                main_window.geometry("500x500")
                main_window.title("Shavtzak App")
                GUIShavtzak(main_window, startHour=hour, startMinute=minute)
                main_window.mainloop()
            else:
                messagebox.showwarning("Invalid Time", "Please enter valid values for hour (0-23) and minute (0-59).")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric values for hour and minute.")

if __name__ == "__main__":
    root = tk.Tk()
    instructions_window = tk.Toplevel(root)
    Instructions(instructions_window)
    root.mainloop()
