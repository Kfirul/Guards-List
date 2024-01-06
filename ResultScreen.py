from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList

class ResultScreen(Screen):
    def __init__(self, shavtzak_instance, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance
        self.shavtzak_instance.createGuardsList()

        # Create a toolbar for the second screen
        self.toolbar = MDTopAppBar(
            title="Shavtzak Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1),
            right_action_items=[["arrow-right", lambda x: self.back()]]
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Create a horizontal layout to hold positions
        horizontal_layout = BoxLayout(orientation="horizontal", spacing=10, padding=34)

        # Iterate over positions
        for position in self.shavtzak_instance.positionList:
            # Create a vertical layout for each position
            position_layout = BoxLayout(orientation="vertical", spacing=10, padding=34)

            position_title = OneLineListItem(
                text=f"Position: {position.name}",
                theme_text_color="Primary",
                on_release=lambda x, p=position, l=position_layout: self.toggle_guards_visibility(p, l)
            )

            position_layout.add_widget(position_title)

            # Create ScrollView for guards of this position (initially hidden)
            guards_scroll_view = ScrollView(size_hint=(1, 0.9), opacity=0)
            guards_list = MDList()

            guards_label = OneLineListItem(text="Guards List:", theme_text_color="Secondary", font_style="H6")
            guards_list.add_widget(guards_label)

            # Add guards for this position
            for guard in position.guardList:
                item = OneLineListItem(text=f" {guard}", theme_text_color="Primary", divider=None)
                guards_list.add_widget(item)

            guards_scroll_view.add_widget(guards_list)
            position_layout.add_widget(guards_scroll_view)

            # Add the position layout to the main horizontal layout
            horizontal_layout.add_widget(position_layout)

        # Add the horizontal layout to the screen
        self.add_widget(horizontal_layout)

    def toggle_guards_visibility(self, pressed_position, pressed_position_layout):
        # Toggle the visibility of the ScrollView associated with the selected position
        for position_layout in self.children[0].children:
            for child in position_layout.children:
                if isinstance(child, ScrollView):
                    child.opacity = 1 if position_layout == pressed_position_layout else 0

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"
