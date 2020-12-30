import os
import subprocess
import platform

try:
    system = platform.system()

    print("Your Current working directory is:", os.getcwd()) #checks your current working directory
    try:
        os.mkdir("SortedDownloads") #creates a new directory if not already present
    except:
        pass

    print("Ctrl+C to exit")

    sourceDirectory = "/home/ashwith/Downloads"
    destinationDirectory = "/home/ashwith/SortedDownloads"

    def Automation(command):
        while 1:
            for files in os.listdir(sourceDirectory):
                filepath = os.path.join(sourceDirectory, files)
                try:
                    os.chdir(filepath)
                    subprocess.run([command, filepath, destinationDirectory])
                except:
                    extension = files.split(".")[1]
                    try:
                        os.chdir(destinationDirectory)
                        os.mkdir(extension)
                        tempPath = os.path.join(destinationDirectory, extension)
                        subprocess.run([command, filepath, tempPath])
                    except:
                        tempPath = os.path.join(destinationDirectory, extension)
                        subprocess.run([command, filepath, tempPath])

    if system.lower!="windows":
        Automation("mv")
    else:
        Automation("move")
except KeyboardInterrupt:
    print("\nexited")