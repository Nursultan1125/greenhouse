from kivy.app import App
from kivy.garden.circularlayout import CircularLayout


class MyCircularLayout(CircularLayout):
    pass


class MyCircularLayoutApp(App):
    def build(self):
        return MyCircularLayout()


MyCircularLayoutApp().run()
