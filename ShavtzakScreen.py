from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, MDList


class ShavtzakScreen(Screen):
    def __init__(self, shavtzak_instance, **kwargs):
        super(ShavtzakScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance
        self.shavtzak_instance.createGuardsList()

        # Create a toolbar for the screen
        self.toolbar = MDTopAppBar(
            title="Shavtzak Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1),
            right_action_items=[["arrow-right", lambda x: self.back()]]
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Create a layout to hold the information
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        # Add the layout to the screen
        self.add_widget(self.layout)
        self.bind(on_enter=self.update_result)

    def update_result(self, *args):
        self.shavtzak_instance.createGuardsList()
        self.layout.clear_widgets()

        # Create horizontal layout for guards list and positions list
        self.horizontal_layout = BoxLayout(orientation="horizontal", spacing=10)

        # Create vertical layout for positions list on the right
        positions_scroll_view = ScrollView(size_hint=(0.5, 0.9))
        positions_list = MDList()

        positions_label = OneLineListItem(text="Positions List:", theme_text_color="Secondary")
        positions_list.add_widget(positions_label)

        for position in self.shavtzak_instance.positionList:
            item = OneLineListItem(text=position.name)
            item.bind(on_release=lambda x, p=position: self.on_position_click(p, p.name))
            positions_list.add_widget(item)

        positions_scroll_view.add_widget(positions_list)
        self.horizontal_layout.add_widget(positions_scroll_view)

        # Create vertical layout for guards list on the left
        guards_scroll_view = ScrollView(size_hint=(0.5, 0.9))
        self.guards_list = MDList()

        guards_label = OneLineListItem(text="Guards List:", theme_text_color="Secondary")
        self.guards_list.add_widget(guards_label)

        # Create a vertical layout for guards (initially hidden)
        self.guards_layout = ScrollView(size_hint=(0.75, 0.9), opacity=0)
        self.guards_list_inner = MDList()
        self.guards_layout.add_widget(self.guards_list_inner)
        self.horizontal_layout.add_widget(self.guards_layout)

        self.layout.add_widget(self.horizontal_layout)

    def on_position_click(self, position, position_name):
        # Highlight the selected position
        self.highlight_selected_position(position_name)

        # Display guards for the selected position
        self.display_guardsList(position)

    def highlight_selected_position(self, position_name):
        # Iterate over all items and apply formatting
        for item in self.guards_list_inner.children:
            if item.text == position_name:
                item.text = f"[b]{item.text}[/b]"
            else:
                item.text = item.text.replace("[b]", "").replace("[/b]", "")

    def display_guardsList(self, position):
        # Clear existing guards list
        self.guards_list_inner.clear_widgets()

        # Add the position name as the title
        title_item = OneLineListItem(text=f"Guards List for {position.name}", theme_text_color="Secondary",
                                     font_style="H6")
        self.guards_list_inner.add_widget(title_item)

        # Add guards for this position
        for guard in position.guardList:
            item = OneLineListItem(text=f" {guard}", theme_text_color="Primary", divider=None)
            self.guards_list_inner.add_widget(item)

        # Show guards layout
        self.guards_layout.opacity = 1

    def back(self):
        print("Going back to the main screen")
        # Switch back to the main screen
        self.manager.current = "main_screen"
