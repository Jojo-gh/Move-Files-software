from flet import *
from flet_route import params, basket
from Interface.Welcome.header import  AppHeader
from Interface.Welcome.description import AppDescription

TITLE = 'Bienvenido'

def header():
    return Container(
                expand=False,
                bgcolor='#87CEEB',
                height=60,
                border_radius=border_radius.only(top_left = 15, top_right = 15, bottom_left = 15, bottom_right = 15),
                padding=padding.only(left = 30, right = 30),
                content=ResponsiveRow(
                    expand=True,
                    controls=[
                        Text(
                            TITLE,
                            weight='bold',
                            text_align='CENTER'
                        )
                    ]
                )
            )



def welcome(page: Page, params: params, basket: basket):
    page.window_width=600
    page.window_height=580
    page.padding=20
    page.bgcolor='white'
    page.update()

    return View(
        '/',
        controls=[
            AppHeader(),
            AppDescription(page)
        ]
    )