""" Script to create batch file with commands to convert downloaded ts files to mp4
"""

#from subprocess import Popen, PIPE
import os
#import time
import sys


def getCommand(mode : int, filename : str):
    outFilename = filename.replace(".ts", ".mp4")
    commands = [
        # direct copy filename
        f'ffmpeg -i "{filename}" -map 0 -c copy "{outFilename}"',
        # copy video and audio only ignore all other streams, can just 
        f'ffmpeg -hwaccel cuda -i "{filename}" -map 0:v:0 -map 0:a:0 -c copy "{outFilename}"',
        # re-encode the entire thing, will take awhile
        f'ffmpeg -i "{filename}" -c:v libx264 -c:a aac "{outFilename}"',
        # copy audio but encoded video 
        f'ffmpeg -i "{filename}" -c:v libx264 -c:a copy "{outFilename}"'

    ]

    return commands[mode]

def printHelp():
    print("Usage python .\copyVideo.py mode directory")
    print("Mode 0 = direct copy")
    print("Mode 1 = copy video and audio only ignore all other streams")
    print("Mode 2 = re-encode the entire thing, will take awhile")
    print("Mode 3 = copy audio but encoded video")

if __name__ == "__main__":

    args = sys.argv

    if len(args) != 3:
        printHelp()
        exit()

    if not args[1].isdigit() or int(args[1]) not in range(0, 4):
        print("Invalid mode number", args[1])
        printHelp()
        exit()

    mode = int(args[1])
    directory = args[2]
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print("invalid directory name", directory)

    f = open("convert.bat", "w", encoding='utf-8')
    for file in os.listdir(directory):
        if ".ts" in file:
            f.write(getCommand(mode, os.path.join(directory, file)) + '\n')
            # print(file)
