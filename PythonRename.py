import os
import PySimpleGUI as sg



def RenameFiles(Directory,NewName,Extension,StartNum):

#    print(NewName)
#    print(Extension)
    i=StartNum
    print(type(i))
    for EachFile in os.listdir(Directory):
        #print(EachFile)
        
        #This is the name and path of the file before it was renamed
        SourceFile=Directory+"/"+EachFile
        #print(SourceFile)
        
        DestFile=Directory+"/"+NewName+" "+ "(" + str(i) + ")" +str(Extension)
       # print(DestFile)
        
        i+=1
        os.rename(SourceFile, DestFile)

def main():

    layout = [

            [sg.Text("Folder of files:"), sg.Input(key="-DIR-"), sg.FolderBrowse()],
            [sg.Text("The new name should be: "), sg.Input(key="-NAME-")],
            [sg.Text("The extensions of the files are: "), sg.Input(key="-EXT-")],
            [sg.Text("What number do you want to start at?"), sg.Input(key="-NUM-")],
            [sg.Exit(), sg.Button("Rename Files :)")],

            ]



    window = sg.Window("Mass Rename Files", layout)

#keep getting unexpected argument in RenameFiles
    while True:
        event, values = window.read()
        #print(event, values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "Rename Files :)":
            RenameFiles(
               
                Directory = values["-DIR-"],
                NewName = values["-NAME-"],
                Extension = values["-EXT-"], 
                StartNum = int(values["-NUM-"]),
            )
    window.close()

if __name__ == '__main__':
    main()
