#This is the header of the desktop application

# Libreries
from flet import *

# Texts
TITLE_HEADER = 'Bienvenido'

#main class
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_brand(self):
        return Container(
            content = Text(
                TITLE_HEADER,
                size = 15,
                color = 'white'
            )
        )
    
    # main class
    def build(self):
        return Container(
            expand = True,
            bgcolor = '#87CEEB',
            height = 60,
            border_radius=border_radius.only(top_left = 15, top_right = 15),
            padding = padding.only(left = 30, right = 30),
            content = Row(
                expand = True,
                alignment = MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    self.app_header_brand(),
                ]
            )

        )