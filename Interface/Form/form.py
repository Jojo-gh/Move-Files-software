#This is the body of the desktop application

# Libreries
from flet import *
# Modules
from Interface.Form.button import app_form_button

#   Texts 
# Title of sections
SOURCE_PATH_REQUEST_TEXT = 'Ingrese carpeta donde se encuentran los archivos que desea mover'
DESTINATION_PATH_REQUEST_TEXT = 'Ingrese carpeta donde desea mover los archivos'

# Title of inputs
TITLE_FIRST_INPUT = 'Dirrecion origen *'
TITLE_SECOND_INPUT = 'Direccion para imagenes'
TITLE_THIRD_INPUT = 'Direccion para musica'
TITLE_FOURTH_INPUT = 'Direccion para videos'
TITLE_FIFTH_INPUT = 'Direccion para pdf'
TITLE_SIXTH_INPUT = 'Direccion para archivos zip'

# File type names
SOURCE_PATH_TYPE_NAME = 'origen'
PHOTO_TYPE_NAME = 'image'
MUSIC_TYPE_NAME = 'music'
VIDEO_TYPE_NAME = 'video'
PDF_TYPE_NAME = 'pdf'
ZIP_TYPE_NAME = 'zip'

# Example folder names
PATH_EXAMPLE = r'C:\Users\User\Downloads'
SOURCE_PATH_TYPE = r''
PHOTO_TYPE_FOLDER = r'\Images'
MUSIC_TYPE_FOLDER = r'\Music'
VIDEO_TYPE_FOLDER = r'\Video'
PDF_TYPE_FOLDER = r'\PDF'
ZIP_TYPE_FOLDER = r'\ArchivosZip'


# main class
class AppForm(UserControl):
    page = None
    # path of the directory from which you want to organize the files.
    source_path = None
    # Path to the destination folder
    photo_destination = None
    music_destination = None
    video_destination = None
    pdf_destination = None
    zip_destination = None

    def __init__(self, page:Page):
        self.page = page

        super().__init__()
    
    def app_first_section(self):
        return Container(
            content = Text(
                SOURCE_PATH_REQUEST_TEXT,
                size=15,
                color='black',
                weight='bold'
            )
        )
    
    def app_second_section(self):
        return Container(
            content = Text(
                DESTINATION_PATH_REQUEST_TEXT,
                size=15,
                color='black',
                weight='bold'

            )
        )

    #Inputs of app
    def app_form_input_field(self, folder=''):
        return Container(
            expand=True,
            height=45,
            bgcolor='#ebebeb',
            border_radius=6,
            padding=8,
            content=
                Column(
                    spacing=1,
                    controls=[
                        self.set_input_name(folder),
                        self.set_input(folder)
                    ]
                )
        )
    
    # Header of inputs
    def set_input_name(self, folder):
        if folder == SOURCE_PATH_TYPE_NAME:
            return self.input_name(TITLE_FIRST_INPUT)
        elif folder == PHOTO_TYPE_NAME:
            return self.input_name(TITLE_SECOND_INPUT)
        elif folder == MUSIC_TYPE_NAME:
            return self.input_name(TITLE_THIRD_INPUT)
        elif folder == VIDEO_TYPE_NAME:
            return self.input_name(TITLE_FOURTH_INPUT)
        elif folder == PDF_TYPE_NAME:
            return self.input_name(TITLE_FIFTH_INPUT)
        elif folder == ZIP_TYPE_NAME:
            return self.input_name(TITLE_SIXTH_INPUT)
    
    # Shows the text that is entered
    def input_name(self, name):
        return Text(
            value=name,
            size=9,
            color='black',
            weight='bold'
        )

    # The value entered in the inputs is assigned based on their type
    def set_input(self, folder):
        if folder == SOURCE_PATH_TYPE_NAME:
            return self.source_path
        elif folder == PHOTO_TYPE_NAME:
            return self.photo_destination
        elif folder == MUSIC_TYPE_NAME:
            return self.music_destination
        elif folder == VIDEO_TYPE_NAME:
            return self.video_destination
        elif folder == PDF_TYPE_NAME:
            return self.pdf_destination
        elif folder == ZIP_TYPE_NAME:
            return self.zip_destination

    # Text for the input example
    def inputs(self, type_folder):
        return TextField(
                border_color='transparent',
                height=20,
                text_size=12,
                content_padding=0,
                cursor_color='black',
                cursor_width=1,
                cursor_height =18,
                color='black',
                hint_text= PATH_EXAMPLE + type_folder  # type_folder referring to the type of files
        )

    # main class
    def build(self):
        # Folder from which you intend to organize the files.
        self.source_path = self.inputs(SOURCE_PATH_TYPE)
        # Path to the destination folder
        self.photo_destination = self.inputs(PHOTO_TYPE_FOLDER)
        self.music_destination = self.inputs(MUSIC_TYPE_FOLDER)
        self.video_destination = self.inputs(VIDEO_TYPE_FOLDER)
        self.pdf_destination = self.inputs(PDF_TYPE_FOLDER)
        self.zip_destination = self.inputs(ZIP_TYPE_FOLDER)

        return Container(
            expand=True,
            height=460,
            bgcolor='white',
            border=border.all(1, '#ebebeb'),
            border_radius=8,
            padding=15,
            content=
                Column(
                    expand=True,
                    controls=[
                        # Folder from which you intend to organize the files.

                        self.app_first_section(),
                        Divider(height = 8, color = 'transparent'),
                        Row(
                            controls=[
                                self.app_form_input_field(SOURCE_PATH_TYPE_NAME)
                            ]
                        ),
                        Divider(height = 2, color = 'transparent'),
                        
                        # Path to the destination folder
                        
                        self.app_second_section(),
                        Divider(height = 8, color = 'transparent'),
                        Row(
                            controls=[
                                self.app_form_input_field(PHOTO_TYPE_NAME),
                                self.app_form_input_field(MUSIC_TYPE_NAME)
                            ]
                        ),
                        Divider(height = 8, color = 'transparent'),
                        Row(
                            controls=[
                                self.app_form_input_field(VIDEO_TYPE_NAME),
                                self.app_form_input_field(PDF_TYPE_NAME)
                            ]
                        ),
                        Divider(height = 8, color = 'transparent'),
                        Row(
                            controls=[
                                self.app_form_input_field(ZIP_TYPE_NAME)
                            ]
                        ),
                        
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                app_form_button( self.source_path,
                                                    self.photo_destination,
                                                    self.music_destination,
                                                    self.video_destination,
                                                    self.pdf_destination,
                                                    self.zip_destination,
                                                    self.page
                                )
                            ]
                        )
                    ]
                )
        )