import os 
import sys
import shutil

def retrieve_folder_path():
    while True:
        folder = input("Enter the folder name: ")
        if os.path.exists(folder):
            return folder
        else:
            print("Folder does not exist. Please enter a valid folder name.")

def main():
    global folder_path 
    if len(sys.argv) < 2:
        folder_path = retrieve_folder_path()
    else:
        folder_path = sys.argv[1]
        if not os.path.exists(folder_path):
            print("Specified folder does not exist.")
            folder_path = retrieve_folder_path()

    print("Folder path:", folder_path)
    return folder_path

def file_type(file):
    image_extensions = ['.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif', '.webp', '.tiff', '.tif', '.bmp', '.heif', '.heic', '.svg', '.svgz']
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.mpeg', '.mpg', '.rm', '.rmvb', '.vob']
    text_extensions = ['.txt', '.doc', '.docx', '.rtf', '.pdf', '.html', '.htm', '.xml', '.csv', '.json', '.log']
    sound_extensions = ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a', '.opus']
    application_extensions = ['.exe', '.dmg', '.apk', '.app', '.deb', '.rpm', '.msi', '.jar', '.bat', '.sh']
    archive_extensions = ['.zip']

    file_extension = os.path.splitext(file)[1]
    if file_extension in image_extensions:
        return "IMAGE"
    elif file_extension in video_extensions:
        return "VIDEO"
    elif file_extension in text_extensions:
        return "TEXT"
    elif file_extension in sound_extensions:
        return "SOUND"
    elif file_extension in application_extensions:
        return "APPLICATION"
    elif file_extension in archive_extensions:
        return "ARCHIVE"
    else:
        return "UNKNOWN-TYPE"


folder_path = main()

folder_contents = os.listdir(folder_path)
images = []
videos = []
text = []
app = []
sound = []
archive = []
unknown_type = []

for file_name in folder_contents:
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_category = file_type(file_name)
        if file_category == "IMAGE":
            images.append(file_name)
        elif file_category == "VIDEO":
            videos.append(file_name)
        elif file_category == "TEXT":
            text.append(file_name)
        elif file_category == "SOUND":
            sound.append(file_name)
        elif file_category == "APPLICATION":
            app.append(file_name)
        elif file_category == "ARCHIVE":
            archive.append(file_name)
        else:
            unknown_type.append(file_name)

images_folder = os.path.join(folder_path, 'images_folder(file_manager)')
videos_folder = os.path.join(folder_path, 'videos_folder(file_manager)')
sound_folder = os.path.join(folder_path, 'sound_folder(file_manager)')
text_folder = os.path.join(folder_path, 'text_folder(file_manager)')
applications_folder = os.path.join(folder_path, 'applications_folder(file_manager)')
archive_folder = os.path.join(folder_path, 'archive_folder(file_manager)')
unknown_folder = os.path.join(folder_path, 'unknown_folder(file_manager)')

def move_files(list_of_files, destination_folder):
    for file_name in list_of_files:
        source_path = os.path.join(folder_path, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)

if images:
    os.makedirs(images_folder, exist_ok=True)
if videos:
    os.makedirs(videos_folder, exist_ok=True)
if sound:
    os.makedirs(sound_folder, exist_ok=True)
if text:
    os.makedirs(text_folder, exist_ok=True)
if app:
    os.makedirs(applications_folder, exist_ok=True)
if archive:
    os.makedirs(archive_folder, exist_ok=True)
if unknown_type:
    os.makedirs(unknown_folder, exist_ok=True)


move_files(images, images_folder)
move_files(videos, videos_folder)
move_files(sound, sound_folder)
move_files(text, text_folder)
move_files(app, applications_folder)
move_files(archive, archive_folder)
move_files(unknown_type, unknown_folder)
