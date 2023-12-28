import tkinter as tk
from tkinter import messagebox
from GUIShavtzak import GUIShavtzak
from PIL import Image, ImageTk


class OpeningWindow:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.geometry("600x700")
        self.root.title("Shavtzak App - Instructions")

        # Set the background color
        self.root.configure(bg="lightcyan")

        # Load the logo image
        logo = Image.open("logo.jpeg")
        logo = ImageTk.PhotoImage(logo)

        # Create a label to display the logo
        logo_label = tk.Label(self.root, image=logo, bg="lightcyan")
        logo_label.image = logo
        logo_label.pack()

        # Welcome message
        instructions_label = tk.Label(self.root, text="Welcome to Shavtzak App!", font=('Arial', 16, 'bold'), pady=10,
                                      bg="lightcyan", fg="black")
        instructions_label.pack()

        # Sublabel
        sub_label = tk.Label(self.root, text="Follow the instructions below to get started:", font=('Arial', 12),
                             pady=10, bg="lightcyan", fg="black")
        sub_label.pack()

        # Hour entry
        hour_label = tk.Label(self.root, text="Enter Start Hour:", font=('Raleway', 12), bg="lightcyan", fg="black")
        hour_label.pack()

        self.hour_var = tk.StringVar()
        hour_entry = tk.Entry(self.root, textvariable=self.hour_var, font=('Raleway', 12), bg="white")
        hour_entry.pack()

        # Minute entry
        minute_label = tk.Label(self.root, text="Enter Start Minute:", font=('Raleway', 12), bg="lightcyan", fg="black")
        minute_label.pack()

        self.minute_var = tk.StringVar()
        minute_entry = tk.Entry(self.root, textvariable=self.minute_var, font=('Raleway', 12), bg="white")
        minute_entry.pack()

        # OK button
        ok_button = tk.Button(self.root, text="OK", command=self.open_main_window, bg="#20bebe", fg="white",
                              font=('Raleway', 14, 'bold'), pady=10)
        ok_button.pack()

    def open_main_window(self):
        try:
            # Get the values from entry widgets
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())

            # Check if the entered time is valid
            if 0 <= hour < 24 and 0 <= minute < 60:
                # Destroy the current window
                self.root.destroy()

                # Create and run the main application window
                main_window = tk.Tk()
                GUIShavtzak(main_window, startHour=hour, startMinute=minute)
                main_window.mainloop()
            else:
                # Display a warning for invalid time
                messagebox.showwarning("Invalid Time", "Please enter valid values for hour (0-23) and minute (0-59).")
        except ValueError:
            # Display a warning for invalid input
            messagebox.showwarning("Invalid Input", "Please enter valid numeric values for hour and minute.")


if __name__ == "__main__":
    # Create and run the opening window
    root = tk.Tk()
    OpeningWindow(root)
    root.mainloop()
