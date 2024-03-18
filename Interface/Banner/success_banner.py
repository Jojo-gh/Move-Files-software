# Libraries
from flet import *

# Texts
TEXT_BANNER = 'Se movieron los archivos correctamente'
TEXT_BUTTON = 'Aceptar'

def close_banner(e, page):
        page.banner.open = False
        page.update()
        page.window_close()

def banner(page):
    page.banner = Banner(
        bgcolor=colors.GREEN_300,
        leading=Icon(icons.CLOUD_DONE_OUTLINED, color=colors.GREEN, size=30),
        content=ResponsiveRow(
            expand=True,
            controls = [
            Text(
                TEXT_BANNER,
                size=14,
                color="white"
            )
        ]),
        actions=[
            TextButton(TEXT_BUTTON, on_click= lambda e:close_banner(e, page)),
        ],
    )

def show_banner(page):
    page.banner.open = True
    page.update()