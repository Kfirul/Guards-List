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
            title="Result Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1),
            right_action_items=[["arrow-right", lambda x: self.back()]]
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Create a layout to hold the labels
        layout = BoxLayout(orientation="vertical", spacing=10)

        # Use the printShavtzak function and add labels for each position and guard
        self.display_guards(layout)

        # Add the layout to the screen
        self.add_widget(layout)

    def display_guards(self, layout):
        # Iterate over positions
        for position in self.shavtzak_instance.positionList:
            position_layout = BoxLayout(orientation="vertical", spacing=1)

            # Add label for position
            position_layout.add_widget(MDLabel(text=f"Position: {position.name}", theme_text_color="Primary"))

            # Create ScrollView for guards of this position
            guards_scroll_view = ScrollView(size_hint=(1, 0.95))
            guards_list = MDList()

            guards_label = OneLineListItem(text="Guards List:", theme_text_color="Secondary",font_style="H6")
            guards_list.add_widget(guards_label)

            # Add guards for this position
            for guard in position.guardList:
                item = OneLineListItem(text=f" {guard}", theme_text_color="Primary")
                guards_list.add_widget(item)

            guards_scroll_view.add_widget(guards_list)
            position_layout.add_widget(guards_scroll_view)

            # Add the position layout to the main layout
            layout.add_widget(position_layout)

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"
