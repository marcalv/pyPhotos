import os
import sys
from pathlib import Path
from folders import folders as imported_folders
from tinydb import TinyDB, Query
import subprocess


def upload_folder(path):
    files_array = get_folder_files(path)
    
    for file in files_array:
        if file_is_backedup(file):
            print("File already uploaded: "+file)
        else:
            result = upload_file(file)
            if result:
                db_insert(file)

def get_folder_files(folder):
    files_array = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(folder):
        for file in f:
            files_array.append(os.path.join(r, file))
    return files_array

def upload_file(file):
    completedProc = subprocess.run(['python','upload.py','--auth', 'auth.txt',file])
    if completedProc.returncode == 0:
        return True
    else:
        return False

def generate_auth():
    os.system('python upload.py --auth auth.txt')
    return 

def db_insert(file):
    Search = Query()
    if not file_is_backedup(file):
        db.insert({'file': file})

def file_is_backedup(file):
    Search = Query()
    if db.search(Search.file == file) == []:
        return False
    else:
        return True


def upload_folders(folders):
    for folder in folders:
        upload_folder(folder)


def allbackedup(folders):
    for folder in folders:
        for file in get_folder_files(folder):
            db_insert(file)


db = TinyDB('db.json')


if len(sys.argv) == 2:
    run_mode = sys.argv[1]
    if run_mode == 'test':
        upload_file("resources/test.png")
    if run_mode == 'abu':
        allbackedup(imported_folders)
    if run_mode == 'auth':
        generate_auth()
else:
    upload_folders(imported_folders)

