import tkinter as tk
from GUIGuard import GuardEntryWindow
from GUIPosition import PositionEntryWindow
from GUIInfo import Info
from GUIResult import Result
from Shavtzak import Shavtzak, Position

class GUIShavtzak:
    def __init__(self, root, startHour, startMinute):
        # Initialize the main Shavtzak GUI
        self.root = root
        self.root.geometry("450x250")
        self.root.resizable(width=False, height=False)
        self.root.title("Shavtzak App")
        self.root.configure(bg="lightcyan")  # Set background color

        # Create Shavtzak instance
        self.shavtzak_instance = Shavtzak(startHour, startMinute)

        # Create GUI elements

        # Label for the Shavtzak App
        self.label = tk.Label(root, text="Shavtzak App", font=('Raleway', 18), bg="lightcyan", fg="black")
        self.label.grid(row=0, column=1, pady=(10, 5))  # Adjusted padding

        # Add Guard button
        self.addGuardButton = tk.Button(root, text="Add Guard", font=('Raleway', 14), command=self.open_guard_entry_window, bg="#20bebe", fg="white")
        self.addGuardButton.grid(row=1, column=0)  # Adjusted padding

        # Delete Guard button
        self.deleteGuardButton = tk.Button(root, text="Delete Guard", font=('Raleway', 14), command=self.shavtzak_instance.deleteGuard, bg="#FF5733", fg="white")
        self.deleteGuardButton.grid(row=2, column=0)  # Adjusted padding

        # Add Position button
        self.addPositionButton = tk.Button(root, text="Add Position", font=('Raleway', 14), command=self.open_position_entry_window, bg="#20bebe", fg="white")
        self.addPositionButton.grid(row=1, column=2)  # Adjusted padding

        # Delete Position button
        self.deletePositionButton = tk.Button(root, text="Delete Position", font=('Raleway', 14), command=self.shavtzak_instance.deletePosition, bg="#FF5733", fg="white")
        self.deletePositionButton.grid(row=2, column=2)  # Adjusted padding

        # Show Info button
        self.showGuardsListButton = tk.Button(root, text="Show Info", font=('Raleway', 14), command=self.show_info,bg="#20bebe", fg="white")
        self.showGuardsListButton.grid(row=6, column=0,pady=(10, 5))  # Adjusted padding

        # Make A Shavtzak button
        self.makeAShavtzak = tk.Button(root, text="Make A Shavtzak", font=('Raleway', 14), command=self.show_result, bg="#20bebe", fg="white")
        self.makeAShavtzak.grid(row=6, column=1,pady=(10, 5))  # Adjusted padding

        # Quit button
        self.quit_button = tk.Button(root, text="Quit", font=('Raleway', 14), command=root.quit, bg="#20bebe", fg="white")
        self.quit_button.grid(row=6, column=2,pady=(10, 5))  # Adjusted padding

    def open_guard_entry_window(self):
        # Open the Guard Entry Window
        guard_entry_window = tk.Toplevel(self.root)
        GuardEntryWindow(guard_entry_window, self.shavtzak_instance)

    def open_position_entry_window(self):
        # Open the Position Entry Window
        position_entry_window = tk.Toplevel(self.root)
        PositionEntryWindow(position_entry_window, self.shavtzak_instance)

    def show_info(self):
        # Show the Information Window
        info_window = tk.Toplevel(self.root)
        Info(info_window, self.shavtzak_instance)

    def show_result(self):
        # Show the Result Window
        result_window = tk.Toplevel(self.root)
        Result(result_window, self.shavtzak_instance)


