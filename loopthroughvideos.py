import os
 
# giving directory name
folderdir = 'Enter directory name here'
 
# giving file extensions that you want to search for, such as .mp4, .mkv, etc.
ext = ('.mp4')


# iterating over directory and subdirectory to get files
for path, dirc, files in os.walk(folderdir):
    for name in files:
        if name.endswith(ext):
            print(path + "\\" + name)  # printing file directory
            # running upload script for each file
            os.system('python uploader.py --file "' + path + "\\" + name + '" --title "' + name + '" --privacyStatus unlisted')
            # I set the videos to upload unlisted, but the options are private, public, or unlisted
