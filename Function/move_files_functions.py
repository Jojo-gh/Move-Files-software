# Import libraries
import os
import shutil

# Types of paths if the source path entered is the same as the destination path
PHOTO = r'\images'
MUSIC = r'\music'
VIDEO = r'\video'
PDF = r'\pdf'
ZIP = r'\zip'
# Extensions of files
PHOTO_EXTENSIONS = '.png', '.jpg', '.jpeg', '.gif', '.svg'
MUSIC_EXTENSIONS = '.mp3'
VIDEO_EXTENSIONS = '.mp4', '.mov', '.avi', '.mkv', '.wmv', '.rmvb'
PDF_EXTENSIONS = '.pdf'
ZIP_EXTENSIONS = '.zip', '.rar', '.7z'

def move_file(source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination):
    """
        Move a file from the source location to the destination folder.

        Parameters:
            source_path: The full path of the file to be moved.
            path_destination: The destination path for the file.

        If the file is found duplicate, the last one detected will be deleted.
    """
    # If the destination folder entered is the same as the source folder, the destination folder will be replaced with a new path in base to type of file
    if (photo_destination == source_path):
        photo_destination = photo_destination + PHOTO

    if (music_destination == source_path):
        music_destination = music_destination + MUSIC

    if (video_destination == source_path):
        video_destination = video_destination + VIDEO

    if (pdf_destination == source_path):
        pdf_destination = pdf_destination + PDF

    if (zip_destination == source_path):
        zip_destination = zip_destination + ZIP

    # Validate folders entered, if don't exists will be created. Return e for the status
    e = validate_folders(source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination)
    # If the function failed to complete, the status return
    if e != 0:
        return e

    # Open directory to read files and folders
    for filename in os.listdir(source_path):
        name, extension = os.path.splitext(os.path.basename(source_path + '/' + filename))
        extension = extension.lower()

        # If the file is a directory
        if os.path.isdir(photo_destination):
            if extension in PHOTO_EXTENSIONS:
                #If the current file is already in the destination folder, it will be deleted.
                if os.path.exists(photo_destination + '/' + filename):
                    print(source_path + '/' + filename)
                    os.remove(source_path + '/' + filename)
                else:
                    shutil.move(source_path + '/' + filename , photo_destination)

        elif os.path.isdir(music_destination):
            if extension in MUSIC_EXTENSIONS:
                if os.path.exists(music_destination + '/' + filename):
                    print(source_path + '/' + filename)
                    os.remove(source_path + '/' + filename)
                else:
                    shutil.move(source_path + '/' + filename , music_destination)

        elif os.path.isdir(video_destination):
            if extension in VIDEO_EXTENSIONS:
                if os.path.exists(video_destination + '/' + filename):
                    print(source_path + '/' + filename)
                    os.remove(source_path + '/' + filename)
                else:
                    shutil.move(source_path + '/' + filename , video_destination)

        elif os.path.isdir(pdf_destination):
            if extension in PDF_EXTENSIONS:
                if os.path.exists(pdf_destination + '/' + filename):
                    print(source_path + '/' + filename)
                    os.remove(source_path + '/' + filename)
                else:
                    shutil.move(source_path + '/' + filename , pdf_destination)

        elif os.path.isdir(zip_destination):
            if extension in ZIP_EXTENSIONS:
                if os.path.exists(zip_destination + '/' + filename):
                    print(source_path + '/' + filename)
                    os.remove(source_path + '/' + filename)
                else:
                    shutil.move(source_path + '/' + filename , zip_destination)

        #If the current file doesn't not meet the above extensions, it is checked to see if it is a directory.
        elif os.path.isdir(source_path + '/' + name):
            new_source_path = source_path + '/' + filename + '/'
            #The function is called recursively to move the internal files.
            move_file(new_source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination)

        # else:
        #     #If it doesn't meet any of the above conditions, it will be moved to the other files folder.
        #     if os.path.exists(DESTINATION_OF_OTHER_FILES + '/' + filename):
        #         print(source_path + filename)
        #         os.remove(source_path + filename)
        #     else:
        #         shutil.move(source_path + filename , DESTINATION_OF_OTHER_FILES)

    return 0

def validate_folders(source_path, photo_destination, music_destination, video_destination, pdf_destination, zip_destination):
    '''
        If the destination folders don't exist, they will be created.
        If the destination folder entered is '' it will be skipped and will not be created
    '''
    while(True):
        #If source_path don't exist, return 1 for the error
            if not os.path.isdir(source_path):
                return 1

            if not os.path.isdir(photo_destination) and photo_destination != '':
                os.mkdir(photo_destination)

            if not os.path.isdir(music_destination) and music_destination != '':
                os.mkdir(music_destination)
            
            if not os.path.isdir(video_destination) and video_destination != '':
                os.mkdir(video_destination)

            if not os.path.isdir(pdf_destination) and pdf_destination != '':
                os.mkdir(pdf_destination)

            if not os.path.isdir(zip_destination) and zip_destination != '':
                os.mkdir(zip_destination)

            # if not os.path.isdir(DESTINATION_OF_OTHER_FILES) and destination_folder != '':
            #     os.mkdir(DESTINATION_OF_OTHER_FILES)

            break

    return 0