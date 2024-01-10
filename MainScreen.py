from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog

from GuardsScreen import GuardsScreen
from PositionsScreen import PositionsScreen
from ShavtzakScreen import ShavtzakScreen


class PositionDetailScreen(Screen):
    def __init__(self, position, **kwargs):
        super(PositionDetailScreen, self).__init__(**kwargs)
        self.position = position

        self.dialog = MDDialog(
            title=f"Position: {position.name}",
            text=f"Amount of Guards: {position.numOfGuards}\nGuarding Time: {position.guardingTime} minutes",
            buttons=[
                MDRaisedButton(text="Close", on_release=self.close_dialog)
            ]
        )

        self.dialog.get_normal_height()

    def show_dialog(self):
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()

class MainScreen(Screen):
    def __init__(self, screen_manager, shavtzak_instance, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance

        # Create a toolbar for the screen
        self.toolbar = MDTopAppBar(
            title="Main Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1)
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # Create a layout to hold the information
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Add the layout to the screen
        self.add_widget(self.layout)

        # Custom colors for the buttons
        button_color = (0.2, 0.7, 0.5, 1)
        text_color = (0, 0, 0, 1)

        # "Guards" button
        guards_button = MDRaisedButton(
            text="Guards",
            theme_text_color="Custom",
            text_color=text_color,
            md_bg_color=button_color,
            pos_hint={"center_x": 0.35, "center_y": 0.84},
        )
        guards_button.bind(on_press=lambda x: self.switch_to_guards_screen(x, screen_manager))
        self.add_widget(guards_button)

        # "Positions" button
        positions_button = MDRaisedButton(
            text="Positions",
            theme_text_color="Custom",
            text_color=text_color,
            md_bg_color=button_color,
            pos_hint={"center_x": 0.48, "center_y": 0.84},
        )
        positions_button.bind(on_press=lambda x: self.switch_to_positions_screen(x, screen_manager))
        self.add_widget(positions_button)

        # "Make A Shavtzak" button
        shavtzak_button = MDRaisedButton(
            text="Make A Shavtzak",
            theme_text_color="Custom",
            text_color=text_color,
            md_bg_color=button_color,
            pos_hint={"center_x": 0.65, "center_y": 0.84},
        )
        shavtzak_button.bind(on_press=lambda x: self.switch_to_result_screen(x, screen_manager))
        self.add_widget(shavtzak_button)

        # Update information when the screen is shown
        self.bind(on_enter=self.update_info)

    def update_info(self, *args):
        # Clear existing widgets from the layout
        self.layout.clear_widgets()

        # Create horizontal layout for guards list and positions list
        horizontal_layout = BoxLayout(orientation="horizontal", spacing=10)

        # Create vertical layout for guards list on the left
        guards_scroll_view = ScrollView(size_hint=(0.5, 0.8))
        guards_list = MDList()

        guards_label = OneLineListItem(text="Guards List:", theme_text_color="Secondary")
        guards_list.add_widget(guards_label)

        index = 1

        for guard in self.shavtzak_instance.guardList:
            guard = str(index) + ". " + guard
            item = OneLineListItem(text=guard)
            guards_list.add_widget(item)
            index += 1

        guards_scroll_view.add_widget(guards_list)
        horizontal_layout.add_widget(guards_scroll_view)

        # Create vertical layout for positions list on the right
        positions_scroll_view = ScrollView(size_hint=(0.5, 0.8))
        positions_list = MDList()

        positions_label = OneLineListItem(text="Positions List:", theme_text_color="Secondary")
        positions_list.add_widget(positions_label)

        for position in self.shavtzak_instance.positionList:
            item = OneLineListItem(text=position.name, on_release=lambda x, p=position: self.show_position_details(p))
            positions_list.add_widget(item)

        positions_scroll_view.add_widget(positions_list)
        horizontal_layout.add_widget(positions_scroll_view)

        self.layout.add_widget(horizontal_layout)


    def switch_to_guards_screen(self, instance, screen_manager):
        # Switch to the Guards screen
        if not any(isinstance(screen, GuardsScreen) for screen in screen_manager.screens):
            guards_screen = GuardsScreen(self.shavtzak_instance, name="guards_screen")
            screen_manager.add_widget(guards_screen)
        self.switch_screen(screen_manager, "guards_screen")

    def switch_to_positions_screen(self, instance, screen_manager):
        # Switch to the Positions screen
        if not any(isinstance(screen, PositionsScreen) for screen in screen_manager.screens):
            positions_screen = PositionsScreen(self.shavtzak_instance, name="positions_screen")
            screen_manager.add_widget(positions_screen)
        self.switch_screen(screen_manager, "positions_screen")

    def switch_to_result_screen(self, instance, screen_manager):
        # Switch to the Result screen
        if not any(isinstance(screen, ShavtzakScreen) for screen in screen_manager.screens):
            result_screen = ShavtzakScreen(self.shavtzak_instance, name="result_screen")
            screen_manager.add_widget(result_screen)
        self.switch_screen(screen_manager, "result_screen")

    def switch_screen(self, screen_manager, screen_name):
        # Helper method to switch screens
        screen_manager.current = screen_name

    def show_position_details(self, position):
        position_detail_screen = PositionDetailScreen(position)
        position_detail_screen.show_dialog()


