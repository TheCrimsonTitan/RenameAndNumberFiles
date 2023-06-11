import os
import PySimpleGUI as sg

def main():

    #User Input for the directory, the new name they need, and the extension they wany
   # Directory=input("Type the path to the files")
   # NewName=input("What is the new name of the files")
   # Extension=input("What is the extension of the files")

    layout = [

            [sg.Text("Folder of files:"), sg.Input(key="-DIR-"), sg.FolderBrowse()],
            [sg.Text("The new name should be: "), sg.Input(key="-NAME-")],
            [sg.Text("The extensions should be: "), sg.Input(key="-EXT-")],
            [sg.Exit(), sg.Button("Rename Files :)")],

            ]



    window = sg.Window("Mass Rename Files", layout)

    while True:
        event, values = window.read()
        #print(event,values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

    window.close()


"""
    i=0
    for EachFile in os.listdir(Directory):
        #print(EachFile)
        
        #This is the name and path of the file before it was renamed
        SourceFile=Directory+"/"+EachFile
        #print(SourceFile)
        
        DestFile=Directory+"/"+NewName+str(i)+str(Extension)
        print(DestFile)
        
        i+=1
        os.rename(SourceFile, DestFile)
"""

if __name__ == '__main__':
    main()
