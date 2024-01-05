from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar

from Position import Position


class PositionsScreen(Screen):
    def __init__(self, shavtzak_instance, **kwargs):
        super(PositionsScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance

        # Create a toolbar for the second screen
        self.toolbar = MDTopAppBar(
            title="Position Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1),  # Set toolbar background color
            right_action_items=[["arrow-right", lambda x: self.back()]]
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Add an entry for the position's name
        self.position_name_entry = MDTextField(
            hint_text="Enter Position's Name To Add",
            size_hint=(0.35, None),
            height=50,
            pos_hint={"center_x": 0.25, "center_y": 0.8},
            font_size=22,
        )
        self.add_widget(self.position_name_entry)

        # Add an entry for the amount of guards
        self.position_amount_entry = MDTextField(
            hint_text="Enter Amount Of Guards",
            size_hint=(0.35, None),
            height=50,
            pos_hint={"center_x": 0.25, "center_y": 0.7},
            font_size=22,
        )
        self.add_widget(self.position_amount_entry)

        # Add an entry for the time to guard
        self.position_time_to_guard_entry = MDTextField(
            hint_text="Enter Time To Guard",
            size_hint=(0.35, None),
            height=50,
            pos_hint={"center_x": 0.25, "center_y": 0.6},
            font_size=22,
        )
        self.add_widget(self.position_time_to_guard_entry)

        # Add a button to add the position
        add_position_button = MDFlatButton(
            text="Add Position",
            font_size=17,
            pos_hint={"center_x": 0.25, "center_y": 0.5},
        )
        add_position_button.bind(on_press=self.add_position)
        self.add_widget(add_position_button)

        # Add an entry for the time to guard
        self.position_to_delete_entry = MDTextField(
            hint_text="Enter Position's Name To Delete",
            size_hint=(0.35, None),
            height=50,
            pos_hint={"center_x": 0.75, "center_y": 0.8},
            font_size=22,
        )
        self.add_widget(self.position_to_delete_entry)

        # Add a button to add the position
        delete_position_button = MDFlatButton(
            text="Delete Position",
            font_size=17,
            pos_hint={"center_x": 0.75, "center_y": 0.5},
        )
        delete_position_button.bind(on_press=self.delete_position)
        self.add_widget(delete_position_button)

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"

    def add_position(self, instance):
        position_name = self.position_name_entry.text
        position_amount = int(self.position_amount_entry.text)
        position_time_to_guard = int(self.position_time_to_guard_entry.text)
        position = Position(position_name, position_amount, position_time_to_guard)

        self.shavtzak_instance.addPosition(position)
        self.position_name_entry.text = ""
        self.position_amount_entry.text = ""
        self.position_time_to_guard_entry.text = ""

    def delete_position(self, instance):
        position_name = self.position_name_entry.text

        self.shavtzak_instance.deletePosition(position_name)
        self.position_name_entry.text = ""

