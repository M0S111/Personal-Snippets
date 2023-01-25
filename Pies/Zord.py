import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Zordfish(App):
    def build(self):

        self.layout = GridLayout(rows=3, padding=10)

        self.layout.add_widget(Label(text="Username"))
        self.contentu = TextInput(multiline=False, cursor_blink=True)
        self.username = self.contentu
        self.layout.add_widget(self.username)

        self.layout.add_widget(Label(text="Password"))
        self.contentp = TextInput(multiline=False, cursor_blink=True, password=True)
        self.password = self.contentp
        self.layout.add_widget(self.password)

        self.button = Button(text="Log In")

        self.layout.add_widget(self.button)

        self.button.bind(on_press=self.onButtonPress)

        return self.layout

    def onButtonPress(self, button):

        layout = GridLayout(cols=1, padding=10)

        popupLabel = Label(text="I know you now.")
        
        if self.contentu.text == '' or self.contentp.text == '':
            expcatch = Label(text="Don't screw around.")
            layout.add_widget(expcatch)
            
        else:

            identu = Label(text='Your handle is ' + self.contentu.text)
        
            identp = Label(text='Your password is ' + self.contentp.text)
            
            layout.add_widget(popupLabel)

            layout.add_widget(identu)
        
            layout.add_widget(identp)
        
        closeButton = Button(text="I get it.")

        layout.add_widget(closeButton)

        # Instantiate the modal popup and display

        popup = Popup(title='BEWARE', content=layout)

                # content=(Label(text='This is a demo pop-up')))

        popup.open()

        # Attach close button press with popup.dismiss action

        closeButton.bind(on_press=popup.dismiss)


if __name__ == '__main__':
    Zordfish().run()
