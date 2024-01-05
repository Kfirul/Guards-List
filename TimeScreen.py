from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.color_definitions import colors

from MainScreen import MainScreen
from Shavtzak import Shavtzak

class TimeScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(TimeScreen, self).__init__(**kwargs)
        self.shavtzak_instance = None

        self.toolbar = MDTopAppBar()
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.md_bg_color = colors["Teal"]["A700"]

        self.add_widget(self.toolbar)

        # Collect user input
        self.inputTime = MDTextField(
            hint_text="Enter a start time (HH:MM)",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=22,
            input_filter=lambda text, from_undo: text[:5]  # Limit input to first 5 characters
        )
        self.add_widget(self.inputTime)

        # "Set" button
        set_button = MDFlatButton(
            text="Set",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        set_button.bind(on_press=lambda x: self.set_shavtzak_instance(x, screen_manager))  # Pass both parameters
        self.add_widget(set_button)


    def set_shavtzak_instance(self, instance, screen_manager):
        try:
            # Parse the entered time
            entered_time = self.inputTime.text
            parsed_time = self.parse_time(entered_time)

            # Extract the hour and minute
            hour, minute = parsed_time.hour, parsed_time.minute

            # Create or update the Shavtzak instance with the new hour and minute
            self.shavtzak_instance = Shavtzak(hour,minute)

            # Optionally, print or use the Shavtzak instance
            print(f"Shavtzak instance set: Hour={hour}, Minute={minute}")

            main_screen = MainScreen(screen_manager,self.shavtzak_instance, name="main_screen")
            screen_manager.add_widget(main_screen)

            # Switch to a new screen (you need to implement this method)
            self.switch_screen(screen_manager, "main_screen")

        except ValueError:
            print("Invalid time format. Please enter time in HH:MM format.")

    # ... other methods ...

    def switch_screen(self, screen_manager, screen_name):
        screen_manager.current = screen_name

    def parse_time(self, time_str):
        from collections import namedtuple

        Time = namedtuple("Time", ["hour", "minute"])

        hour, minute = map(int, time_str.split(":"))
        return Time(hour=hour, minute=minute)

