import flet
from flet import *

#routing
from flet_route import Routing, path
# Modules
from Interface.Welcome.main import welcome
from Interface.Form.main import form_main

def main(page: Page):

    app_routes = [
        path(url = '/', clear=True, view=welcome),
        path(url = '/form', clear=True, view=form_main)
    ]

    Routing(page=page,
            app_routes=app_routes)
    
    page.go(page.route)
    
if __name__ == "__main__":
    flet.app(target=main)