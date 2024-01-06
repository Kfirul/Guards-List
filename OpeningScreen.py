
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

from TimeScreen import TimeScreen
from Shavtzak import Shavtzak

class ShavtzakApp(MDApp):

    def build(self):

        # Create a ScreenManager
        screen_manager = ScreenManager()

        # Create a screen
        screen = Screen(name="opening_screen")
        screen_manager.add_widget(screen)

        # logo
        screen.add_widget(Image(
            source="logo.jpeg",
            pos_hint={"center_x": 0.5, "center_y": 0.55}
        ))

        time_screen = TimeScreen(screen_manager, name="time_screen")
        screen_manager.add_widget(time_screen)

        Clock.schedule_once(lambda dt: self.switch_screen(screen_manager, "time_screen"), 3)

        return screen_manager

    def switch_screen(self, screen_manager, screen_name):
        screen_manager.current = screen_name


if __name__ == '__main__':
    ShavtzakApp().run()
