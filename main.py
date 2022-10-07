# Felix Larsson
# TEINF-20
# 25-11-2022
# Travify

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.9.0')

class Trippy(App):
    def build(self):
        return MyRoot()

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(1, 20))

trippy_app = Trippy()
trippy_app.run()