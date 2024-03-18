# Libreries
from flet import *
#routing
from flet_route import params, basket
# Modules
from Interface.Form.form import AppForm
from Interface.Form.header import AppHeader

def form_main(page: Page, params: params, basket: basket):
    page.window_width = 580
    page.window_height = 600
    # page.window_height = 760
    page.padding = 20
    page.bgcolor = 'white'
    page.update()

    return View(
        '/form',
        controls=[
            Column(
                expand = True,
                controls = [
                    AppHeader(),
                    # Divider(height = 2, color = 'transparent'),
                    AppForm(page),
                ]
            )
        ]
    )

if __name__ == "__main__":
    
    app(target=main)