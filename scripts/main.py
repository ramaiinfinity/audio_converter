#moviepy py module for video editing
from moviepy.editor import *
from pydub import AudioSegment
import shutil
import os

#path to file
path = "/home/shreeram/Downloads"
# file_path = os.listdir(path)
convertedFilesFolder = "/home/shreeram/workspace/audio_converter/scripts/COnverted Files"
#Need to add validation

def mp3filename(file):
    return os.path.splitext(os.path.basename(file.path))[0]+".mp3"

def convvert_to_mp3(filepath) :
    for file in os.scandir(filepath):
        # if file.path.endswith(".mkv") or file.path.endswith(".wav") or file.path.endswith(".webm") or file.path.endswith(".mp4"):
        if file.path.endswith(".wav"):
            convertedFile = mp3filename(file)
            
            print("*"*100)
            print(convertedFile)
            print("Converting:  ",file)

            AudioSegment.from_file(file.path).export(convertedFile,format="mp3")
            shutil.move(convertedFile,convertedFilesFolder)
            
        elif file.path.endswith(".mp4") or file.path.endswith(".mov"):
            
            convertedFile = mp3filename(file)
            
            print("*"*100)
            print(convertedFile)
            print("Converting:  ",file)

            
            videoclip = VideoFileClip(os.path.join(filepath,file))
            audioclip = videoclip.audio

            
            audioclip.write_audiofile(os.path.join(convertedFilesFolder, convertedFile))

            

if __name__ == '__main__':
    if os.listdir(convertedFilesFolder):
        for old_files in os.listdir(convertedFilesFolder):
            os.remove(os.path.join(convertedFilesFolder,old_files))
        print("Folder is Clean.....")
    convvert_to_mp3(path)
