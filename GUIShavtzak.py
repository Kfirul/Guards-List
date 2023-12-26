import tkinter as tk
from tkinter import messagebox

from GUIGuard import GuardEntryWindow
from GUIPosition import PositionEntryWindow
from GUIShavtzakInfo import Info
from Shavtzak import Shavtzak, Position


class GUIShavtzak:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Shavtzak App")

        # Create Shavtzak instance
        self.shavtzak_instance = Shavtzak(0, 0)

        # Create GUI elements
        self.label = tk.Label(root, text="Shavtzak App", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.addGuardButton = tk.Button(root, text="Add Guard", command=self.open_guard_entry_window)
        self.addGuardButton.pack()

        self.addPositionButton = tk.Button(root, text="Add Position", command=self.open_position_entry_window)
        self.addPositionButton.pack()

        self.printGuardList = tk.Button(root, text="Print Guards List", command=self.shavtzak_instance.printGuardsList)
        self.printGuardList.pack()

        self.printPositionList = tk.Button(root, text="Print Position List", command=self.shavtzak_instance.printPositionsList)
        self.printPositionList.pack()

        self.makeAShavtzak = tk.Button(root, text="Make A Shavtzak", command=self.shavtzak_instance.createGuardsList)
        self.makeAShavtzak.pack()

        self.showGuardsListButton = tk.Button(root, text="Show Info", command=self.show_info)
        self.showGuardsListButton.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def open_guard_entry_window(self):
        guard_entry_window = tk.Toplevel(self.root)
        GuardEntryWindow(guard_entry_window, self.shavtzak_instance)

    def open_position_entry_window(self):
        position_entry_window = tk.Toplevel(self.root)
        PositionEntryWindow(position_entry_window, self.shavtzak_instance)

    def show_info(self):
        info_window = tk.Toplevel(self.root)
        Info(info_window, self.shavtzak_instance)



if __name__ == "__main__":
    root = tk.Tk()
    app = GUIShavtzak(root)
    root.mainloop()