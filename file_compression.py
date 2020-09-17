import os
import gzip
import shutil
import time
import schedule

# absolute path to main folder
path = '/var'
# name of main folder
name_folder='log'
# name of new folder
new_name_folder='log_cpr'

########## creation of individual paths #########
path_main_folder=os.path.join(path,name_folder)
path_new_main_folder=os.path.join(path,new_name_folder)
suffix = '.gz'

def compression():
    files = os.listdir(path_main_folder)
    ############# new folder #########################
    if not os.path.exists(path_new_main_folder):
        os.makedirs(path_new_main_folder)
    ############# compression of files in folder #########################
    for f in files:
        path_main_files = os.path.join(path, name_folder, f)
        path_main_files_02 = os.path.join(path, name_folder, f + suffix)
        destination = os.path.join(path, new_name_folder, f + suffix)
        with open(path_main_files, 'rb') as f_in:
            with gzip.open(path_main_files_02, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        ########## moving new files #########################
        shutil.move(path_main_files_02, destination)
        ########## removing old files #########################
        os.remove(path_main_files)

########## timing of repeating #########################
schedule.every(30).day.at("8:00").do(compression)

while True:
    schedule.run_pending()
    time.sleep(1)