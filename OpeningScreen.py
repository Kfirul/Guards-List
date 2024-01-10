from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivymd.app import MDApp

from TimeScreen import TimeScreen
from Shavtzak import Shavtzak

class ShavtzakApp(MDApp):

    def build(self):
        # Create a ScreenManager
        screen_manager = ScreenManager()

        # Create the opening screen
        opening_screen = Screen(name="opening_screen")
        screen_manager.add_widget(opening_screen)

        # Add logo to the opening screen
        opening_screen.add_widget(Image(
            source="logo.jpeg",
            pos_hint={"center_x": 0.5, "center_y": 0.55}
        ))

        # Create the time screen
        time_screen = TimeScreen(screen_manager, name="time_screen")
        screen_manager.add_widget(time_screen)

        # Schedule a switch to the time screen after 1 second
        Clock.schedule_once(lambda dt: self.switch_screen(screen_manager, "time_screen"), 3)

        return screen_manager

    def switch_screen(self, screen_manager, screen_name):
        # Switch to the specified screen
        screen_manager.current = screen_name

# Run the app
if __name__ == '__main__':
    ShavtzakApp().run()
