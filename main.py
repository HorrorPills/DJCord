import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#open the window UI
class MyGridLayout(GridLayout):
    #initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #Set columns
        self.cols = 3
        #Add widgets
        self.add_widget(Label(text='Name: '))
        #Add input box
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        layout = self(orientation='vertical')
        btn1 = Button(text='Hello')
        btn2 = Button(text='World')
        layout.add_widget(btn1)
        layout.add_widget(btn2)


class DJCord(App):
    def build(self):
        return Label(text="Hello World")
if __name__ == '__main__':
    DJCord().run()
