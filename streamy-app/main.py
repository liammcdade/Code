from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        # Create a button with a callback function
        button = Button(text='Hello, Kivy!', on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        # This function will be called when the button is pressed
        print('Button pressed!')


if __name__ == '__main__':
    MyApp().run()
