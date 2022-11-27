import os
def file_name_change():
    path = r'F:\Code\DAP Lab\Text'
    
    os.chdir(path)

    filename = os.listdir()
    filename.sort()

    for i in range(len(filename)):
        ind=filename[i].index("1910")
        new_name=filename[i][ind:]

        source=os.path.join(path,filename[i])
        dest=os.path.join(path,new_name)

        os.rename(source, dest)
 
file_name_change()