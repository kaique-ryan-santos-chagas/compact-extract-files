import shutil
import zipfile as zip

def compact_folder(folder_name):
    shutil.make_archive('zipfiles/' + folder_name, format='zip', root_dir='zipfiles/' + folder_name)

compact_folder('Videos')


def extract_file(file_name):
    with zip.ZipFile('zipfiles/' + file_name + '.zip', 'r') as file:
        file.extractall('zipfiles/Extracted')

extract_file('Videos')