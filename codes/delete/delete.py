import os

def delete_files_in_directory(directory):
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)
                    print(f'Datei gelöscht: {file_path}')
                except Exception as e:
                    print(f'Fehler beim Löschen der Datei {file_path}: {e}')

            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    os.rmdir(dir_path)
                    print(f'Ordner gelöscht: {dir_path}')
                except Exception as e:
                    print(f'Fehler beim Löschen des Ordners {dir_path}: {e}')

        print(f'Alle Dateien und Ordner in "{directory}" wurden erfolgreich gelöscht.')
    else:
        print(f'Das Verzeichnis "{directory}" existiert nicht.')