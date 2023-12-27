import tkinter as tk
from tkinter import messagebox

class Info:
    def __init__(self, root, shavtzak_instance):
        self.root = root
        self.shavtzak_instance = shavtzak_instance
        self.root.geometry("400x400")
        self.root.title("Information")
        self.root.configure(bg="lightcyan")

        start_time_label = tk.Label(self.root, text=f"Start Time: {self.shavtzak_instance.hour:02d}:{self.shavtzak_instance.minute:02d}", font=('Raleway', 14, 'bold'), bg="lightcyan", fg="black")
        start_time_label.pack(pady=10)

        guards_label = tk.Label(self.root, text="Guards List:", font=('Raleway', 12, 'underline'), bg="lightcyan", fg="black")
        guards_label.pack(pady=5)

        for guard in self.shavtzak_instance.guardList:
            label = tk.Label(self.root, text=guard, font=('Raleway', 12), bg="lightcyan", fg="black")
            label.pack()

        positions_label = tk.Label(self.root, text="Positions List:", font=('Raleway', 12, 'underline'), bg="lightcyan", fg="black")
        positions_label.pack(pady=5)

        for position in self.shavtzak_instance.positionList:
            label = tk.Label(self.root, text=f"Position: {position.name}\nAmount of Guards: {position.numOfGuards}\nTime To Guard: {position.timeToGuard} minutes", font=('Raleway', 12), bg="lightcyan", fg="black")
            label.pack(pady=5)


