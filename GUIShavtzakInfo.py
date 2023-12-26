import tkinter as tk
from tkinter import messagebox

class Info:
    def __init__(self, root, shavtzak_instance):
        self.root = root
        self.shavtzak_instance = shavtzak_instance
        self.root.geometry("300x300")
        self.root.title("Information")

        # Display Guards List
        guards_label = tk.Label(root, text="Guards List:")
        guards_label.pack(pady=5)

        for guard in self.shavtzak_instance.guardList:
            label = tk.Label(root, text=guard)
            label.pack()

        # Display Positions List
        positions_label = tk.Label(root, text="Positions List:")
        positions_label.pack(pady=5)

        for position in self.shavtzak_instance.positionList:
            label = tk.Label(root, text=f"{position.name}, Amount of Guards: {position.numOfGuards}, Time To Guard: {position.timeToGuard} ")
            label.pack()


