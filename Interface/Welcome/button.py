# Libraries
from flet import *

# Texts
BUTTON_NAME = 'Continuar'

def button(page):
    return Container(
        alignment= alignment.center,
        padding = padding.only(top=30),
        content=
            ElevatedButton(
                on_click=lambda _: page.go('/form'),
                bgcolor='#081d33',
                color='white',
                height=42,
                width=220,
                content=ResponsiveRow(
                    controls=[
                        Text(
                            BUTTON_NAME,
                            size=11,
                            weight='bold',
                            text_align='CENTER'
                        )
                    ]
                )
            )
    )