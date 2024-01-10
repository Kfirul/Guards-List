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

from GuardsScreen import GuardsScreen
from InfoScreen import InfoScreen
from PositionsScreen import PositionsScreen
from ShavtzakScreen import ShavtzakScreen
from Shavtzak import Shavtzak

class MainScreen(Screen):
    def __init__(self, screen_manager,shavtzak_instance, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.shavtzak_instance = shavtzak_instance

        self.toolbar = MDTopAppBar(
            title="Menu Screen",
            md_bg_color=(0.2, 0.7, 0.5, 1)
        )
        self.toolbar.pos_hint = {"top": 1}
        self.add_widget(self.toolbar)

        # "Set" button
        guards_button = MDFlatButton(
            text="Guards",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.8},
        )
        guards_button.bind(on_press=lambda x: self.switch_to_guards_screen(x, screen_manager))  # Pass both parameters
        self.add_widget(guards_button)

        # "Set" button
        positions_button = MDFlatButton(
            text="Positions",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.6},
        )
        positions_button.bind(on_press=lambda x: self.switch_to_positions_screen(x, screen_manager))  # Pass both parameters
        self.add_widget(positions_button)

        # "Set" button
        info_button = MDFlatButton(
            text="Info",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        info_button.bind(on_press=lambda x: self.switch_to_info_screen(x, screen_manager))  # Pass both parameters
        self.add_widget(info_button)

        # "Set" button
        shavtzak_button = MDFlatButton(
            text="Make A Shavtzak",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.2},
        )
        shavtzak_button.bind(on_press=lambda x: self.switch_to_result_screen(x, screen_manager))  # Pass both parameters
        self.add_widget(shavtzak_button)

    def switch_to_guards_screen(self, instance, screen_manager):
        if not any(isinstance(screen, GuardsScreen) for screen in screen_manager.screens):
            guards_screen = GuardsScreen(self.shavtzak_instance,name="guards_screen")
            screen_manager.add_widget(guards_screen)

        # Switch to a new screen (you need to implement this method)
        self.switch_screen(screen_manager, "guards_screen")

    def switch_to_positions_screen(self, instance, screen_manager):
        if not any(isinstance(screen, PositionsScreen) for screen in screen_manager.screens):
            positions_screen = PositionsScreen(self.shavtzak_instance, name="positions_screen")
            screen_manager.add_widget(positions_screen)

         # Switch to a new screen (you need to implement this method)
        self.switch_screen(screen_manager, "positions_screen")

    def switch_to_info_screen(self, instance, screen_manager):
        if not any(isinstance(screen, InfoScreen) for screen in screen_manager.screens):
            info_screen = InfoScreen(self.shavtzak_instance, name="info_screen")
            screen_manager.add_widget(info_screen)

        self.switch_screen(screen_manager,"info_screen")

    # Assuming you have a method to switch screens in your main app class
    def switch_to_result_screen(self, instance, screen_manager):
        if not any(isinstance(screen, ShavtzakScreen) for screen in screen_manager.screens):
            result_screen = ShavtzakScreen(self.shavtzak_instance, name="result_screen")
            screen_manager.add_widget(result_screen)

        self.switch_screen(screen_manager, "result_screen")

    def switch_screen(self, screen_manager, screen_name):
        screen_manager.current = screen_name



