import tkinter as tk
from tkinter import messagebox

from GUIGuard import GuardEntryWindow
from GUIPosition import PositionEntryWindow
from GUIInfo import Info
from GUIResult import Result
from Shavtzak import Shavtzak, Position

class GUIShavtzak:
    def __init__(self, root, startHour, startMinute):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Shavtzak App")
        self.root.configure(bg="lightcyan")  # Set background color

        # Create Shavtzak instance
        self.shavtzak_instance = Shavtzak(startHour, startMinute)

        # Create GUI elements
        self.label = tk.Label(root, text="Shavtzak App", font=('Raleway', 18), bg="lightcyan", fg="black")
        self.label.pack(pady=(10, 5))  # Adjusted padding

        self.addGuardButton = tk.Button(root, text="Add Guard",font=('Raleway', 14), command=self.open_guard_entry_window, bg="#20bebe", fg="white")
        self.addGuardButton.pack(pady=5)  # Adjusted padding

        self.addPositionButton = tk.Button(root, text="Add Position",font=('Raleway', 14), command=self.open_position_entry_window, bg="#20bebe", fg="white")
        self.addPositionButton.pack(pady=5)  # Adjusted padding

        self.makeAShavtzak = tk.Button(root, text="Make A Shavtzak",font=('Raleway', 14), command=self.show_result, bg="#20bebe", fg="white")
        self.makeAShavtzak.pack(pady=5)  # Adjusted padding

        self.showGuardsListButton = tk.Button(root, text="Show Info",font=('Raleway', 14), command=self.show_info, bg="#20bebe", fg="white")
        self.showGuardsListButton.pack(pady=5)  # Adjusted padding

        self.quit_button = tk.Button(root, text="Quit",font=('Raleway', 14), command=root.quit, bg="#20bebe", fg="white")
        self.quit_button.pack(pady=(5, 10))  # Adjusted padding

    def open_guard_entry_window(self):
        guard_entry_window = tk.Toplevel(self.root)
        GuardEntryWindow(guard_entry_window, self.shavtzak_instance)

    def open_position_entry_window(self):
        position_entry_window = tk.Toplevel(self.root)
        PositionEntryWindow(position_entry_window, self.shavtzak_instance)

    def show_info(self):
        info_window = tk.Toplevel(self.root)
        Info(info_window, self.shavtzak_instance)

    def show_result(self):
        result_window = tk.Toplevel(self.root)
        Result(result_window, self.shavtzak_instance)
