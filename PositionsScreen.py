from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar

# Import the Position class from Position module
from Position import Position

class PositionsScreen(Screen):
    def __init__(self, shavtzak_instance, **kwargs):
        super(PositionsScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance

        # Create a toolbar for the second screen
        self.toolbar = MDTopAppBar(
            title="Positions Screen",
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
        self.position_guarding_time_entry = MDTextField(
            hint_text="Enter Guarding Time (in minutes)",
            size_hint=(0.35, None),
            height=50,
            pos_hint={"center_x": 0.25, "center_y": 0.6},
            font_size=22,
        )
        self.add_widget(self.position_guarding_time_entry)

        # Add a button to add the position
        add_position_button = MDFlatButton(
            text="Add Position",
            font_size=17,
            text_color=(0, 0, 0, 1),
            md_bg_color=(0.2, 0.7, 0.5, 1),
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
            text_color=(0, 0, 0, 1),
            md_bg_color=(0.2, 0.7, 0.5, 1),
            pos_hint={"center_x": 0.75, "center_y": 0.5},
        )
        delete_position_button.bind(on_press=self.delete_position)
        self.add_widget(delete_position_button)

        # Add a label to show messages
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Secondary"
        )
        self.add_widget(self.label)

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"

    def add_position(self, instance):
        # Function to add a position
        position_name = self.position_name_entry.text
        position_amount = int(self.position_amount_entry.text)
        position_guarding_time = int(self.position_guarding_time_entry.text)
        position = Position(position_name, position_amount, position_guarding_time)

        # Add position to the shavtzak instance
        if self.shavtzak_instance.addPosition(position):
            self.label.text = "Add Successfully"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)
        else:
            if position_guarding_time % 5 != 0:

                self.label.text = "Enter Guarding Time That Divide in 5"
                Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)
            else:
                self.label.text = "Existing Position, Enter Other Position's Name"
                Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)

        # Clear entry fields
        self.position_name_entry.text = ""
        self.position_amount_entry.text = ""
        self.position_guarding_time_entry.text = ""

    def delete_position(self, instance):
        # Function to delete a position
        position_name = self.position_to_delete_entry.text
        if self.shavtzak_instance.deletePosition(position_name):
            self.label.text = "Delete Successfully"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)
        else:
            self.label.text = "Not Existing Position, Enter Other Position's Name"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', ""), 3)

        # Clear entry field
        self.position_to_delete_entry.text = ""
