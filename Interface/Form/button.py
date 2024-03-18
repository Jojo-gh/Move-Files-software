# This is the button of form

# Libreries
from flet import *
# Modules
from Function.move_files_functions import move_file
from Interface.Banner.success_banner import banner, show_banner, close_banner

# Texts
BUTTON_NAME = 'Mover Archivos'
ERROR_SOURCE_PATH = 'Ruta de carpeta origen no existe.'
ANOTHER_ERROR = 'Ingrese una ruta de destino valida'

def move_archives(source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination, page:Page):
    '''
        Calls the move_file function and depending on the result of the operation sends one message or another
    '''
    e = move_file(source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination)
    if e == 1:
        print(ERROR_SOURCE_PATH)
        return
    elif e != 0:
        print(ANOTHER_ERROR)
        return
    print('Done')
    banner(page)
    show_banner(page)

# main class
def app_form_button(source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination, page:Page):
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda _: move_archives(source_path.value, photo_destination.value, music_destination.value, video_destination.value, pdf_destination.value, zip_destination.value, page),
            bgcolor='#081d33',
            color='white',
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12
                    ),
                    Text(
                        'Mover Archivos',
                        size=11,
                        weight='bold'
                    )
                ]
            ),
            style=ButtonStyle(
                shape={
                    '': RoundedRectangleBorder(radius=6),
                },
                color={
                    '': 'white'
                }
            ),
            height=42,
            width=220
        )
    )