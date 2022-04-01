import PySimpleGUI as sg
import os.path
from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join
import glob
import itertools
import timeit


def func(message):
    print(message)

layout1 = [      [
            sg.Input(do_not_clear=False, key = "-INPI-",size=(40, 2)),  sg.Button("Write the Image Sizes", key = "-RUN-",size=(20, 1))
          
          ],
    
    [sg.In("Choose Head Folder",size=(40, 2), enable_events=True, key="-FOLDERHEAD-"), 
            sg.FolderBrowse("Choose Head Folder",size=(20, 1)) ],
           [
               
            sg.In("Choose Body Folder",size=(40, 2), enable_events=True, key="-FOLDERBODY-"), 
            sg.FolderBrowse("Choose Body Folder",size=(20, 1))
           ],
            [
               
            sg.In("Choose Lower Body Folder",size=(40, 2), enable_events=True, key="-FOLDERLOW-"), 
            sg.FolderBrowse("Choose Lower Body Folder",size=(20, 1))
           ],
           [
            sg.In("Choose Background Folder",size=(40, 2), enable_events=True, key="-FOLDERBACK-"), 
            sg.FolderBrowse("Choose Background Folder",size=(20, 1))
           ],
            [
            sg.Button("Generate", key = "-GENBUT-",size=(57, 1))
          ]
 ] 
        
          







        
window = sg.Window('NFT Generator', layout= layout1, margins=(100, 50))

while True:             # Event Loop

    
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    try:
        size = 512, 512
        if event == '-RUN-':
            cmd=values['-INPI-'], 
            if cmd[0].isdigit()==1 and 0<int(cmd[0])<1025:
                size = cmd[0], cmd[0]
                func(cmd[0])
                sg.Popup("Size has been saved")
                
            else :
                sg.Popup("Please give a number between 0 and 1024")
                
                
        elif event == '-FOLDERHEAD-':
            lheads= []
            folder = values['-FOLDERHEAD-']  
            func(folder)
            mHeads = [k for k in listdir(folder) if isfile(join(folder, k))]
            
            for q in mHeads:
                lheads.append(Image.open("{}/{}".format(folder,q)).resize((size), Image.ANTIALIAS)) 
            print(len(lheads))


                
        elif event == '-FOLDERBODY-':
            lbodys = []
            folder = values['-FOLDERBODY-']  
            func(folder)
            mBody = [k for k in listdir(folder) if isfile(join(folder, k))]
            
            for l in mBody:
                lbodys.append(Image.open("{}/{}".format(folder,l)).resize((size), Image.ANTIALIAS))  
            print(len(lbodys))
            
            
        elif event == '-FOLDERLOW-':
            llows = []
            folder = values['-FOLDERLOW-']  
            func(folder)
            mLows = [j for j in listdir(folder) if isfile(join(folder, j))]
            
            for m in mLows:
                llows.append(Image.open("{}/{}".format(folder, m)).resize((size), Image.ANTIALIAS))
            print(len(llows))
            
        elif event == '-FOLDERBACK-':
            lbacks = []
            folder = values['-FOLDERBACK-']  
            func(folder)
            mBacks = [j for j in listdir(folder) if isfile(join(folder, j))]
            
            for l in mBacks:
                lbacks.append(Image.open("{}/{}".format(folder, l)).resize((size), Image.ANTIALIAS))  
            print(len(lbacks))
            
        elif event == '-GENBUT-':
            ltotal = []
            ldegisenler = []
            if len(lheads)*len(lbodys)*len(llows)*len(lbacks) != 0:
                
                ltotal.append(lbacks)
                ltotal.append(lbodys)
                ltotal.append(lheads)
                ltotal.append(llows)
                
                
                iterasyon = list(itertools.product(*ltotal))
        
                for idx, sayi1 in enumerate(iterasyon):
                    temp = sayi1[0].copy()
                    temp.paste(sayi1[1], (0,0), sayi1[1])
                    temp.paste(sayi1[2], (0,0), sayi1[2])
                    temp.paste(sayi1[3], (0,0), sayi1[3])
                    temp.save("generated2/{}.png".format(idx+1),"PNG")

            else:
                sg.Popup("Please give all folder paths correctly")
            

    except:
        func("-")
        
        
window.Close()