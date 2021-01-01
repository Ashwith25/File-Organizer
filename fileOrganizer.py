import os
import subprocess

try:
    print("Your Current working directory is:", os.getcwd()) #checks your current working directory
    try:
        os.mkdir("SortedDownloads") #creates a new directory if not already present
    except:
        pass

    print("Ctrl+C to exit")

    sourceDirectory = "/home/ashwith/Downloads"
    destinationDirectory = "/home/ashwith/SortedDownloads"
    while 1:
        for files in os.listdir(sourceDirectory):
            filepath = os.path.join(sourceDirectory, files)
            try:
                os.chdir(filepath)
                subprocess.run(["mv", filepath, destinationDirectory])
            except:
                extension = files.split(".")[1]
                try:
                    os.chdir(destinationDirectory)
                    os.mkdir(extension)
                    tempPath = os.path.join(destinationDirectory, extension)
                    subprocess.run(["mv", filepath, tempPath])
                except:
                    tempPath = os.path.join(destinationDirectory, extension)
                    subprocess.run(["mv", filepath, tempPath])
                    
except KeyboardInterrupt:
    print("\nexited")