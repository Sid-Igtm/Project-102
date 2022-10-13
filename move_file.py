import os, shutil

sourcePath = "C:/Users/onyxg/Downloads"
destinationPath = "C:/Users/onyxg/Downloads/docs"

list_files = os.listdir(sourcePath)
print(list_files)

for f in list_files:
    name, ext = os.path.splitext(f)

    if(ext == ""):
        continue 

    if(ext in ['.doc', '.docx', '.txt','.pdf']):
        if(os.path.exists(destinationPath+"/")):
            shutil.move(sourcePath+"/" + f, destinationPath+"/"+ f)
        
        else:
            os.mkdir(destinationPath + "/")
            shutil.move(sourcePath+"/" + f, destinationPath+"/"+ f) 
    


        

    