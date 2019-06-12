import os, sys
import subprocess
import numpy as np

maxProc = 3 #this is where you enter how many threads you want to spawn
files = []
processes = []
numbers = []
command = "7z.exe a -mx9 -mmt12 "


for i in os.listdir():
    if i.endswith(".tif"):
        files.append(i)

for k in range(len(files)):
    numbers.append(k)

chunks = round((len(numbers))/maxProc)
workList = np.array_split(numbers, chunks)

#build processes
for chunk in range(len(workList)):
    print('wait')
    live = 0
    for item in workList[chunk]:
        print(item)
        command_params = (('"'+files[item]+'.7z" "'+
                       files[item]+'" '+' "'+
                       files[item].replace('.tif', '.prj')+'" "'+
                       files[item].replace('.tif', '.tfw')+'"')
                      )

                                  
        p = subprocess.Popen(command + command_params)
        live = live + 1
       
        if live == maxProc:
            p.wait()

    
