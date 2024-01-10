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

from Shavtzak import Shavtzak

from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar

class GuardsScreen(Screen):
    def __init__(self, shavtzak_instance, **kwargs):
        super(GuardsScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance

        # Create a toolbar for the second screen
        self.toolbar = MDTopAppBar(
            title="Guards Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1),
            right_action_items=[["arrow-right", lambda x: self.back()]]
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Add an entry for the guard's name
        self.guard_entry = MDTextField(
            hint_text="Enter Guard's Name To Add",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            font_size=22,
        )
        self.add_widget(self.guard_entry)

        # Add a button to add the guard
        add_guard_button = MDFlatButton(
            text="Add Guard",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        )
        add_guard_button.bind(on_press=self.add_guard)
        self.add_widget(add_guard_button)

        self.label = MDLabel(

            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            theme_text_color="Secondary"
        )
        self.add_widget(self.label)

        # Add an entry for the guard's name
        self.guard_delete_entry = MDTextField(
            hint_text="Enter Guard's Name To Delete",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            font_size=22,
        )
        self.add_widget(self.guard_delete_entry)

        # Add a button to add the guard
        delete_guard_button = MDFlatButton(
            text="Delete Guard",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.3},
        )
        add_guard_button.bind(on_press=self.delete_guard)
        self.add_widget(delete_guard_button)

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"

    def add_guard(self, instance):
        guard_name = self.guard_entry.text
        if self.shavtzak_instance.addGuard(guard_name):
            self.label.text = "Add Successfully"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)
        else:
            self.label.text = "Existing Guard, Enter Other Guard's Name"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)

        self.guard_entry.text = ""

    def delete_guard(self, instance):
        guard_name = self.guard_delete_entry.text
        if self.shavtzak_instance.deleteGuard(guard_name):
            self.label.text = "Delete Successfully"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)
        else:
            self.label.text = "Not Existing Guard, Enter Other Guard's Name"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)

        self.guard_delete_entry.text = ""