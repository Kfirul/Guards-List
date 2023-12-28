import tkinter as tk
from tkinter import messagebox

class Info:
    def __init__(self, root, shavtzak_instance):
        # Initialize the Information Window
        self.root = root
        self.shavtzak_instance = shavtzak_instance
        self.root.geometry("400x400")
        self.root.title("Information")
        self.root.configure(bg="lightcyan")

        # Label displaying the start time
        start_time_label = tk.Label(self.root, text=f"Start Time: {self.shavtzak_instance.hour:02d}:{self.shavtzak_instance.minute:02d}", font=('Raleway', 14, 'bold'), bg="lightcyan", fg="black")
        start_time_label.pack(pady=10)

        # Label for the Guards List section
        guards_label = tk.Label(self.root, text="Guards List:", font=('Raleway', 12, 'underline'), bg="lightcyan", fg="black")
        guards_label.pack(pady=5)

        # Display each guard in the Guards List
        for guard in self.shavtzak_instance.guardList:
            label = tk.Label(self.root, text=guard, font=('Raleway', 12), bg="lightcyan", fg="black")
            label.pack()

        # Label for the Positions List section
        positions_label = tk.Label(self.root, text="Positions List:", font=('Raleway', 12, 'underline'), bg="lightcyan", fg="black")
        positions_label.pack(pady=5)

        # Display each position in the Positions List with details
        for position in self.shavtzak_instance.positionList:
            label = tk.Label(self.root, text=f"Position: {position.name}\nAmount of Guards: {position.numOfGuards}\nTime To Guard: {position.timeToGuard} minutes", font=('Raleway', 12), bg="lightcyan", fg="black")
            label.pack(pady=5)


