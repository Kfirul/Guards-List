from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar

from MainScreen import MainScreen
from Shavtzak import Shavtzak

class TimeScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(TimeScreen, self).__init__(**kwargs)
        self.shavtzak_instance = None

        # Create a toolbar for the screen
        self.toolbar = MDTopAppBar(
            md_bg_color=(0.2, 0.7, 0.5, 1)
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Create a label to welcome the user
        self.label = MDLabel(
            text="Welcome!\n First set the start hour to guard",

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            theme_text_color="Secondary"
        )
        self.add_widget(self.label)

        # Collect user input for start time
        self.inputTime = MDTextField(
            hint_text="Enter a start time (HH:MM)",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=22,
            input_filter=lambda text, from_undo: text[:5]  # Limit input to first 5 characters
        )
        self.add_widget(self.inputTime)

        # "Set" button to confirm the start time
        set_button = MDFlatButton(
            text="Set",
            font_size=17,
            text_color=(1, 1, 1, 1),
            md_bg_color=(0.2, 0.7, 0.5, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        set_button.bind(on_press=lambda x: self.set_shavtzak_instance(x, screen_manager))
        self.add_widget(set_button)

    def set_shavtzak_instance(self, instance, screen_manager):
        try:
            # Parse the entered time
            entered_time = self.inputTime.text
            parsed_time = self.parse_time(entered_time)

            # Extract the hour and minute
            hour, minute = parsed_time.hour, parsed_time.minute

            # Create or update the Shavtzak instance with the new hour and minute
            self.shavtzak_instance = Shavtzak(hour, minute)

            # Optionally, print or use the Shavtzak instance
            print(f"Shavtzak instance set: Hour={hour}, Minute={minute}")

            # Create and switch to the main screen with the Shavtzak instance
            main_screen = MainScreen(screen_manager, self.shavtzak_instance, name="main_screen")
            screen_manager.add_widget(main_screen)
            self.switch_screen(screen_manager, "main_screen")

        except ValueError:
            # Handle invalid time format
            self.inputTime.text = ""
            print("Invalid time format. Please enter time in HH:MM format.")

    def switch_screen(self, screen_manager, screen_name):
        # Switch to the specified screen
        screen_manager.current = screen_name

    def parse_time(self, time_str):
        # Parse the entered time in HH:MM format and return as named tuple
        from collections import namedtuple

        Time = namedtuple("Time", ["hour", "minute"])
        hour, minute = map(int, time_str.split(":"))
        return Time(hour=hour, minute=minute)
