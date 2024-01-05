from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog

class PositionDetailScreen(Screen):
    def __init__(self, position, **kwargs):
        super(PositionDetailScreen, self).__init__(**kwargs)
        self.position = position

        self.dialog = MDDialog(
            title=f"Position: {position.name}",
            text=f"Amount of Guards: {position.numOfGuards}\nTime to Guard: {position.timeToGuard} minutes",
            buttons=[
                MDRaisedButton(text="Close", on_release=self.close_dialog)
            ]
        )

        self.dialog.get_normal_height()

    def show_dialog(self):
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()

class InfoScreen(Screen):
    def __init__(self, shavtzak_instance, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance

        # Create a toolbar for the screen
        self.toolbar = MDTopAppBar(
            title="Info Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1),
            right_action_items=[["arrow-right", lambda x: self.back()]]
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)


        # Create a layout to hold the information
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # # Display start hour and minute at the top with smaller font size
        # start_time_label = MDLabel(
        #     text=f"Start Time: {self.shavtzak_instance.hour:02d}:{self.shavtzak_instance.minute:02d}",
        #     theme_text_color="Secondary",
        #     halign="center",
        #     font_style="H4",
        #     font_size=16  # Adjust the font size here
        # )
        # layout.add_widget(start_time_label)

        # Create horizontal layout for guards list and positions list
        horizontal_layout = BoxLayout(orientation="horizontal", spacing=10)

        # Create vertical layout for guards list on the left
        guards_scroll_view = ScrollView(size_hint=(0.5, 0.9))
        guards_list = MDList()

        guards_label = OneLineListItem(text="Guards List:", theme_text_color="Secondary")
        guards_list.add_widget(guards_label)

        for guard in self.shavtzak_instance.guardList:
            item = OneLineListItem(text=guard)
            guards_list.add_widget(item)

        guards_scroll_view.add_widget(guards_list)
        horizontal_layout.add_widget(guards_scroll_view)

        # Create vertical layout for positions list on the right
        positions_scroll_view = ScrollView(size_hint=(0.5, 0.9))
        positions_list = MDList()

        positions_label = OneLineListItem(text="Positions List:", theme_text_color="Secondary")
        positions_list.add_widget(positions_label)

        for position in self.shavtzak_instance.positionList:
            item = OneLineListItem(text=position.name, on_release=lambda x, p=position: self.show_position_details(p))
            positions_list.add_widget(item)

        positions_scroll_view.add_widget(positions_list)
        horizontal_layout.add_widget(positions_scroll_view)

        layout.add_widget(horizontal_layout)

        # Add the layout to the screen
        self.add_widget(layout)

    def show_position_details(self, position):
        position_detail_screen = PositionDetailScreen(position)
        position_detail_screen.show_dialog()

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"
