from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):

        self.modes = (
            '%I:%m:%S',
            '%H:%m:%S',
            '%S:',
        )
        self.data = ""

        self.mode = 0

        self.main_box = BoxLayout(orientation='vertical')

        self.button = Button(text='label', font_size=15, font_name='comic.ttf')
        self.main_box.add_widget(self.button)

        self.button.bind(on_press=self.tap)
        Clock.schedule_interval(self.timer, 0.01)

        return self.main_box

    def tap(self, button):
        if self.mode + 1 == len(self.modes):
            self.mode = 0
        else:
            self.mode += 1

    def timer(self, dt):
        self.button.text = self.data
