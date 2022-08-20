from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.menu import MDDropDownMenu
from kivy.lang import Builder


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        index = 0
        categories = ['Experience Level', 'How many remote work?', 'Company Size']
        self.btn = Button(text ="Start adding\nvalues",
                   font_size ="15sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
        self.btn.bind(on_press=self.start)
        self.add_widget(Label(text='Enter values to predict salary', font_size="30sp"))
        self.add_widget(self.btn)
    
    def start(self, instance):
        self.values = TextInput(multiline=False)
        self.add_widget(self.values)
        self.remove_widget(self.btn)
        btn = Button(text='Add value',
        font_size='15sp',
        size=(32, 32),
        size_hint=(.3, .2))
        self.add_widget(btn)
    Builder.load_file("design.kv")


class MyApp(MDApp):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()