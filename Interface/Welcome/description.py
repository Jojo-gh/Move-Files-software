#This is the description of the desktop application

# Libreries
from flet import *
from Interface.Welcome.button import button
# Texts
Description = 'Esta aplicacion permite tomar los archivos de un directorio (incluyendo subdirectorios) y dependiendo de su tipo de archivo moverlo a la carpeta de destino que sea indicada.'
PD_TITLE = 'Puntos a tener en cuenta:'
FIRST_POINT = '- Direcciones obligatorias contienen *'
SECOND_POINT = '- Para omitir un tipo de archivo deje la direccion de destino en blanco.'
THIRD_POINT = '- Ingresar la misma direccion de origen en las direcciones de destino creara una carpeta en dicha direccion con el nombre del tipo de archivo.'
FOURTH_POINT = '- Si usted ingresa una ruta que no sea valida el software no funcionara correctamente.'
FIFTH_POINT = '- Si usted ingresa una ruta valida, y le agrega al final una carpeta no existente el software creara dicha carpeta para luego mover los archivos.'

# main class
class AppDescription(UserControl):
    page = None

    def __init__(self, page:Page):
        self.page = page

        super().__init__()

    def app_description_brand(self):
        return Container(
            content = Text(
                Description,
                size = 14,
                color = 'white'
            )
        )

    def app_pd_section_title(self):
        return Container(
            content = Text(
                PD_TITLE,
                size = 14,
                color = 'white'
            )
        )
    
    def app_first_point(self):
        return Container(
            content = Text(
                FIRST_POINT,
                size = 14,
                color = 'white'
            )
        )

    def app_second_point(self):
        return Container(
            content = Text(
                SECOND_POINT,
                size = 14,
                color = 'white'
            )
        )
    
    def app_third_point(self):
        return Container(
            content = Text(
                THIRD_POINT,
                size = 14,
                color = 'white'
            )
        )

    def app_fourth_point(self):
        return Container(
            content = Text(
                FOURTH_POINT,
                size = 14,
                color = 'white'
            )
        )

    def app_fifth_point(self):
        return Container(
            content = Text(
                FIFTH_POINT,
                size = 14,
                color = 'white'
            )
        )
    
    def build(self):
        return Container(
            expand = True,
            bgcolor = '#87CEEB',
            height = 420,
            padding = padding.only(left = 30, right = 30, top = 10),
            border_radius=border_radius.only(bottom_left = 15, bottom_right = 15),
            content = ResponsiveRow(
                expand = True,
                
                controls = [
                    self.app_description_brand(),
                    self.app_pd_section_title(),
                    self.app_first_point(),
                    self.app_second_point(),
                    self.app_third_point(),
                    self.app_fourth_point(),
                    self.app_fifth_point(),
                    button(self.page)
                ]
            )

        )